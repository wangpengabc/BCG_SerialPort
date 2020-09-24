# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\13126\Desktop\BCG_serialport\SerialPortWp.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1125, 434)
        self.groupBox_receiveArea = QtWidgets.QGroupBox(Form)
        self.groupBox_receiveArea.setGeometry(QtCore.QRect(40, 20, 441, 271))
        self.groupBox_receiveArea.setObjectName("groupBox_receiveArea")
        self.radioButton_receiveArea_hexOascii = QtWidgets.QRadioButton(self.groupBox_receiveArea)
        self.radioButton_receiveArea_hexOascii.setGeometry(QtCore.QRect(360, 10, 51, 19))
        self.radioButton_receiveArea_hexOascii.setChecked(True)
        self.radioButton_receiveArea_hexOascii.setObjectName("radioButton_receiveArea_hexOascii")
        self.textBrowser_receive = QtWidgets.QTextBrowser(self.groupBox_receiveArea)
        self.textBrowser_receive.setGeometry(QtCore.QRect(20, 30, 411, 231))
        self.textBrowser_receive.setObjectName("textBrowser_receive")
        self.groupBox_sendArea = QtWidgets.QGroupBox(Form)
        self.groupBox_sendArea.setGeometry(QtCore.QRect(40, 300, 441, 81))
        self.groupBox_sendArea.setObjectName("groupBox_sendArea")
        self.textEdit_sendArea = QtWidgets.QTextEdit(self.groupBox_sendArea)
        self.textEdit_sendArea.setGeometry(QtCore.QRect(20, 40, 411, 31))
        self.textEdit_sendArea.setObjectName("textEdit_sendArea")
        self.radioButton_sendArea_hexOascii = QtWidgets.QRadioButton(self.groupBox_sendArea)
        self.radioButton_sendArea_hexOascii.setGeometry(QtCore.QRect(260, 10, 51, 19))
        self.radioButton_sendArea_hexOascii.setChecked(True)
        self.radioButton_sendArea_hexOascii.setObjectName("radioButton_sendArea_hexOascii")
        self.pushButton_sendArea_send = QtWidgets.QPushButton(self.groupBox_sendArea)
        self.pushButton_sendArea_send.setGeometry(QtCore.QRect(350, 10, 61, 28))
        self.pushButton_sendArea_send.setObjectName("pushButton_sendArea_send")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(510, 70, 61, 31))
        self.label.setObjectName("label")
        self.pushButton_comRefresh = QtWidgets.QPushButton(Form)
        self.pushButton_comRefresh.setGeometry(QtCore.QRect(580, 70, 91, 28))
        self.pushButton_comRefresh.setObjectName("pushButton_comRefresh")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(510, 110, 61, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox_comPort = QtWidgets.QComboBox(Form)
        self.comboBox_comPort.setGeometry(QtCore.QRect(580, 110, 87, 31))
        self.comboBox_comPort.setObjectName("comboBox_comPort")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(510, 160, 61, 31))
        self.label_3.setObjectName("label_3")
        self.comboBox_comBaudRate = QtWidgets.QComboBox(Form)
        self.comboBox_comBaudRate.setGeometry(QtCore.QRect(580, 160, 87, 31))
        self.comboBox_comBaudRate.setObjectName("comboBox_comBaudRate")
        self.comboBox_comBaudRate.addItem("")
        self.comboBox_comBaudRate.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(510, 210, 61, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton_comOpen = QtWidgets.QPushButton(Form)
        self.pushButton_comOpen.setGeometry(QtCore.QRect(580, 210, 91, 28))
        self.pushButton_comOpen.setObjectName("pushButton_comOpen")
        self.pushButton_comClose = QtWidgets.QPushButton(Form)
        self.pushButton_comClose.setGeometry(QtCore.QRect(580, 260, 91, 28))
        self.pushButton_comClose.setObjectName("pushButton_comClose")
        self.label_comInductor = QtWidgets.QLabel(Form)
        self.label_comInductor.setGeometry(QtCore.QRect(520, 260, 41, 31))
        self.label_comInductor.setLineWidth(3)
        self.label_comInductor.setObjectName("label_comInductor")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphWidget = PlotWidget(Form)
        self.graphWidget.setGeometry(QtCore.QRect(710, 60, 391, 291))
        self.graphWidget.setObjectName("graphWidget")
        self.pushButton_clearFigure = QtWidgets.QPushButton(Form)
        self.pushButton_clearFigure.setGeometry(QtCore.QRect(720, 380, 151, 28))
        self.pushButton_clearFigure.setObjectName("pushButton_clearFigure")
        self.label_size = QtWidgets.QLabel(Form)
        self.label_size.setGeometry(QtCore.QRect(580, 370, 101, 31))
        self.label_size.setLineWidth(3)
        self.label_size.setObjectName("label_size")
        self.layoutWidget.raise_()
        self.groupBox_sendArea.raise_()
        self.groupBox_receiveArea.raise_()
        self.label.raise_()
        self.pushButton_comRefresh.raise_()
        self.label_2.raise_()
        self.comboBox_comPort.raise_()
        self.label_3.raise_()
        self.comboBox_comBaudRate.raise_()
        self.label_4.raise_()
        self.pushButton_comOpen.raise_()
        self.pushButton_comClose.raise_()
        self.label_comInductor.raise_()
        self.graphWidget.raise_()
        self.pushButton_clearFigure.raise_()
        self.label_size.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_receiveArea.setTitle(_translate("Form", "receive"))
        self.radioButton_receiveArea_hexOascii.setText(_translate("Form", "hex"))
        self.groupBox_sendArea.setTitle(_translate("Form", "send"))
        self.radioButton_sendArea_hexOascii.setText(_translate("Form", "hex"))
        self.pushButton_sendArea_send.setText(_translate("Form", "send"))
        self.label.setText(_translate("Form", "串口刷新"))
        self.pushButton_comRefresh.setText(_translate("Form", "refresh"))
        self.label_2.setText(_translate("Form", "可用串口"))
        self.label_3.setText(_translate("Form", "波特率"))
        self.comboBox_comBaudRate.setItemText(0, _translate("Form", "9600"))
        self.comboBox_comBaudRate.setItemText(1, _translate("Form", "115200"))
        self.label_4.setText(_translate("Form", "串口操作"))
        self.pushButton_comOpen.setText(_translate("Form", "open"))
        self.pushButton_comClose.setText(_translate("Form", "close"))
        self.label_comInductor.setText(_translate("Form", "Close"))
        self.pushButton_clearFigure.setText(_translate("Form", "clear Figure"))
        self.label_size.setText(_translate("Form", "0"))
from pyqtgraph import PlotWidget
