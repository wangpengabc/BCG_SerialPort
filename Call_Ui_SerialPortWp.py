import binascii
import gc
import os
import re
import sys
import time
import datetime
from threading import Timer
import tracemalloc
import numpy as np

from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtWidgets import  *
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from Ui_SerialPortWp import Ui_Form


class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)


class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        self.datecount = 0

        self.setupUi(self)

        self.CreateItems()

        self.CreateSignalSlot()

        self.rx_data_flash = bytearray()
        # self.rx_data_flash = b''
        self.x = [0 for _ in range(1000)]
        self.y = [0 for _ in range(1000)]
        self.z = [0 for _ in range(1000)]
        self.graphWidget.setXRange(0, 1000, padding=0)

        self.data_line_x = self.graphWidget.plot(self.x, pen='r')
        self.data_line_y = self.graphWidget.plot(self.y, pen='g')
        self.data_line_z = self.graphWidget.plot(self.z, pen='b')

    def create_text(self):
        timestr = time.strftime("%Y-%m-%d-%H-%M-%S")    # read the current time
        file = "\data\data_"+timestr+".txt"
        path = os.getcwd() + file
        self.f = open(path, 'w+')   # create file
        self.datecount = 0
        self.f.write(str(datetime.datetime.now()) + '\n')
        self.f.write("axis_x\taxis_y\taxis_z\n")    # set the keys in text file

    def update_graph_widget(self):
        self.data_line_x.setData(self.x)

        self.data_line_y.setData(self.y)

        self.data_line_z.setData(self.z)

    def CreateItems(self):
        self.com = QSerialPort()
        # self.timer = QTimer()
        # self.

    def CreateSignalSlot(self):
        self.pushButton_comRefresh.clicked.connect(self.pushButton_comRefresh_clicked)
        self.pushButton_comOpen.clicked.connect(self.pushButton_comOpen_clicked)
        self.pushButton_comClose.clicked.connect(self.pushButton_comClose_clicked)
        self.pushButton_sendArea_send.clicked.connect(self.pushButton_sendArea_send_clicked)
        self.com.readyRead.connect(self.Com_Receive_Data)
        self.pushButton_clearFigure.clicked.connect(self.clear_figure)

    def clear_figure(self):
        self.x = [0 for _ in range(1000)]
        self.y = [0 for _ in range(1000)]
        self.z = [0 for _ in range(1000)]
        self.data_line_x.setData([0 for _ in range(1000)], clear=True)
        self.data_line_y.setData([0 for _ in range(1000)], clear=True)
        self.data_line_z.setData([0 for _ in range(1000)], clear=True)

    def pushButton_comRefresh_clicked(self):
        self.comboBox_comPort.clear()
        com = QSerialPort()
        comlist = QSerialPortInfo.availablePorts()
        for info in comlist:
            com.setPort(info)
            if com.open(QSerialPort.ReadWrite):
                self.comboBox_comPort.addItem(info.portName())
                com.close()

    def pushButton_comOpen_clicked(self):
        comName = self.comboBox_comPort.currentText()
        comBaud = int(self.comboBox_comBaudRate.currentText())
        self.com.setPortName(comName)
        self.com.setBaudRate(comBaud)
        try:
            if not self.com.open(QSerialPort.ReadWrite):
                QMessageBox.critical(self, "严重错误", "串口打开失败")
                return
        except:
            QMessageBox.critical(self, "严重错误", "串口打开失败")
            return

        self.pushButton_comRefresh.setEnabled(False)
        self.pushButton_sendArea_send.setEnabled(True)
        self.pushButton_comClose.setEnabled(True)
        self.pushButton_comOpen.setEnabled(False)
        self.comboBox_comPort.setEnabled(False)
        self.comboBox_comBaudRate.setEnabled(False)
        self.label_comInductor.setText("Open")

        self.rx_data_flash = bytearray()
        # self.rx_data_flash = b''
        # create text file
        self.create_text()

        # open timer to deal with the received data from com
        # self.time = RepeatingTimer(0.2, self.Com_Receive_Data)
        # self.time.start()

    def pushButton_comClose_clicked(self):
        self.com.close()
        self.pushButton_comRefresh.setEnabled(True)
        self.pushButton_sendArea_send.setEnabled(False)
        self.pushButton_comClose.setEnabled(False)
        self.pushButton_comOpen.setEnabled(True)
        self.comboBox_comPort.setEnabled(True)
        self.comboBox_comBaudRate.setEnabled(True)
        self.label_comInductor.setText("Close")

        # close file
        self.f.write('\n' + str(datetime.datetime.now()))
        self.f.write('\n' + str(self.datecount))
        self.f.close()

        # self.time.cancel()

    def pushButton_sendArea_send_clicked(self):
        tx_Data = self.textEdit_sendArea.toPlainText()

        if self.radioButton_sendArea_hexOascii.isChecked() is False:
            try:
                self.com.write(tx_Data.encode("UTF-8"))
            except:
                QMessageBox.critical(self, "错误", "发送编码错误")
                return

        else:
            Data = tx_Data.replace(" ", "")
            if len(tx_Data)%2 == 1:
                Data = Data[0:len(tx_Data)-1]

            if Data.isalnum() is False:
                QMessageBox.critical(self, "错误", "存在非字符")
                return
            try:
                Data = binascii.a2b_hex(Data)
            except:
                QMessageBox.critical(self, "错误", "存在非16进制的数")
                return
            try:
                self.com.write(Data)
            except:
                QMessageBox.critical(self, "错误", "发送失败")
                return

    def Com_Receive_Data(self):
        # if self.com.bytesAvailable() < 500:
        #     return 1
        rx_data = bytes(self.com.readAll())

        # try:
        #     rx_data = bytes(self.com.readAll())
        #     self.com.clear()
        # except:
        #     QMessageBox.critical(self, "错误", "读取错误")
        #
        # # if rx_data is not b'':
        # if self.radioButton_sendArea_hexOascii.isChecked() is False:
        #     try:
        #         self.textBrowser_receive.insertPlainText(rx_data.decode('UTF-8'))
        #     except:
        #         pass
        # else:
        #     Data = binascii.b2a_hex(rx_data).decode('ascii')
        #
        #     # re 正则表达式 (.{2}) 匹配两个字母
        #     hexStr = ' 0x'.join(re.findall('(.{2})', Data))
        #     # 补齐第一个 0x
        #     hexStr = '0x' + hexStr
        #     self.textBrowser_receive.insertPlainText(hexStr)
        #     self.textBrowser_receive.insertPlainText(' ')

            # 更新figure， 并保存数据到txt文件
            # 将接收到的数据放到一个数组中，存够8个再进行处理.
            # 如果不建立缓存区，会出现一组数据分两次进入接收处理函数，会出现数据丢失
        self.rx_data_flash += rx_data
        rx_data_len = len(self.rx_data_flash)

        del rx_data

        if rx_data_len >= 100:
            self.deal_rx_data()

    def deal_rx_data(self):
        data = binascii.b2a_hex(self.rx_data_flash).decode('ascii')

        ptn = r"aaaaaaabaf[\w]{12}abaf0000"

        if re.search(ptn, data) is None:
            self.rx_data_flash = bytearray()
            gc.collect()
            return 1

        start_idx = re.search(ptn, data).span()[0]
        data_re_array = re.findall(ptn, data)
        data_re_len = len(data_re_array)

        for i in range(data_re_len):
            data_tmp = binascii.a2b_hex(data_re_array[i])
            rx_data_x_int = int.from_bytes(data_tmp[5:7], "big", signed=True)  # convert bytes type to int
            rx_data_y_int = int.from_bytes(data_tmp[7:9], "big", signed=True)
            rx_data_z_int = int.from_bytes(data_tmp[9:11], "big", signed=True)

            self.x = self.x[1:]     # shift the existing list
            self.x.append(rx_data_x_int)    # append to the list

            self.y = self.y[1:]
            self.y.append(rx_data_y_int)

            self.z = self.z[1:]
            self.z.append(rx_data_z_int)

            self.update_graph_widget()  # update the figure

            # save data to txt file
            self.f.write(str(rx_data_x_int) + '\t')
            self.f.write(str(rx_data_y_int) + '\t')
            self.f.write(str(rx_data_z_int) + '\n')

            self.datecount += 1

        self.rx_data_flash = self.rx_data_flash[(int(start_idx/2) + data_re_len*15):]
        gc.collect()

        size_of_rx = str(len(self.rx_data_flash))
        self.label_size.setText(size_of_rx)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
