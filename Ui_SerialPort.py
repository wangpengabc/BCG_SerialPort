# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\AllPrj\PyQt5prj\MySerialPort_universal\SerialPort.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(704, 562)
        font = QtGui.QFont()
        font.setFamily("方正兰亭中黑_GBK")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Form.setMouseTracking(False)
        Form.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 25, 25);\n"
"font: 9pt \"方正兰亭中黑_GBK\";")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 355, 54, 12))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.Send_Button = QtWidgets.QPushButton(Form)
        self.Send_Button.setGeometry(QtCore.QRect(330, 350, 75, 23))
        self.Send_Button.setObjectName("Send_Button")
        self.ClearButton = QtWidgets.QPushButton(Form)
        self.ClearButton.setGeometry(QtCore.QRect(330, 40, 75, 23))
        self.ClearButton.setObjectName("ClearButton")
        self.textEdit_Recive = QtWidgets.QTextEdit(Form)
        self.textEdit_Recive.setGeometry(QtCore.QRect(40, 70, 361, 251))
        self.textEdit_Recive.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.textEdit_Recive.setObjectName("textEdit_Recive")
        self.textEdit_Send = QtWidgets.QTextEdit(Form)
        self.textEdit_Send.setGeometry(QtCore.QRect(40, 385, 361, 151))
        self.textEdit_Send.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.textEdit_Send.setObjectName("textEdit_Send")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(440, 100, 221, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Com_Baud_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Com_Baud_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Com_Baud_Label.setObjectName("Com_Baud_Label")
        self.gridLayout.addWidget(self.Com_Baud_Label, 1, 0, 1, 1)
        self.Com_Close_Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Com_Close_Button.setDefault(False)
        self.Com_Close_Button.setObjectName("Com_Close_Button")
        self.gridLayout.addWidget(self.Com_Close_Button, 4, 1, 1, 1)
        self.Com_Name_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Com_Name_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Com_Name_Label.setObjectName("Com_Name_Label")
        self.gridLayout.addWidget(self.Com_Name_Label, 2, 0, 1, 1)
        self.Com_Name_Combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.Com_Name_Combo.setObjectName("Com_Name_Combo")
        self.gridLayout.addWidget(self.Com_Name_Combo, 2, 1, 1, 1)
        self.Com_Refresh_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Com_Refresh_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Com_Refresh_Label.setObjectName("Com_Refresh_Label")
        self.gridLayout.addWidget(self.Com_Refresh_Label, 0, 0, 1, 1)
        self.Com_Refresh_Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Com_Refresh_Button.setObjectName("Com_Refresh_Button")
        self.gridLayout.addWidget(self.Com_Refresh_Button, 0, 1, 1, 1)
        self.Com_State_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Com_State_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Com_State_Label.setObjectName("Com_State_Label")
        self.gridLayout.addWidget(self.Com_State_Label, 3, 0, 1, 1)
        self.Com_Baud_Combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.Com_Baud_Combo.setEditable(True)
        self.Com_Baud_Combo.setDuplicatesEnabled(False)
        self.Com_Baud_Combo.setModelColumn(0)
        self.Com_Baud_Combo.setObjectName("Com_Baud_Combo")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.gridLayout.addWidget(self.Com_Baud_Combo, 1, 1, 1, 1)
        self.Com_Open_Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Com_Open_Button.setObjectName("Com_Open_Button")
        self.gridLayout.addWidget(self.Com_Open_Button, 3, 1, 1, 1)
        self.Com_isOpenOrNot_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Com_isOpenOrNot_Label.setText("")
        self.Com_isOpenOrNot_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Com_isOpenOrNot_Label.setObjectName("Com_isOpenOrNot_Label")
        self.gridLayout.addWidget(self.Com_isOpenOrNot_Label, 4, 0, 1, 1)
        self.hexSending_checkBox = QtWidgets.QCheckBox(Form)
        self.hexSending_checkBox.setGeometry(QtCore.QRect(240, 345, 91, 31))
        self.hexSending_checkBox.setObjectName("hexSending_checkBox")
        self.hexShowing_checkBox = QtWidgets.QCheckBox(Form)
        self.hexShowing_checkBox.setGeometry(QtCore.QRect(240, 40, 81, 20))
        self.hexShowing_checkBox.setObjectName("hexShowing_checkBox")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(430, 350, 251, 181))
        self.calendarWidget.setStyleSheet("alternate-background-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.calendarWidget.setObjectName("calendarWidget")
        self.Time_Label = QtWidgets.QLabel(Form)
        self.Time_Label.setGeometry(QtCore.QRect(460, 310, 181, 21))
        font = QtGui.QFont()
        font.setFamily("方正兰亭中黑_GBK")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Time_Label.setFont(font)
        self.Time_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Time_Label.setObjectName("Time_Label")
        self.About_Button = QtWidgets.QPushButton(Form)
        self.About_Button.setGeometry(QtCore.QRect(440, 40, 221, 31))
        font = QtGui.QFont()
        font.setFamily("方正兰亭中黑_GBK")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.About_Button.setFont(font)
        self.About_Button.setObjectName("About_Button")

        self.retranslateUi(Form)
        self.ClearButton.clicked.connect(self.textEdit_Recive.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "接收区"))
        self.label_2.setText(_translate("Form", "发送区"))
        self.Send_Button.setText(_translate("Form", "发送"))
        self.ClearButton.setText(_translate("Form", "清除"))
        self.textEdit_Recive.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'方正兰亭中黑_GBK\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.Com_Baud_Label.setText(_translate("Form", "波特率"))
        self.Com_Close_Button.setText(_translate("Form", "Close"))
        self.Com_Name_Label.setText(_translate("Form", "串口选择"))
        self.Com_Refresh_Label.setText(_translate("Form", "串口搜索"))
        self.Com_Refresh_Button.setText(_translate("Form", "刷新"))
        self.Com_State_Label.setText(_translate("Form", "串口操作"))
        self.Com_Baud_Combo.setCurrentText(_translate("Form", "1200"))
        self.Com_Baud_Combo.setItemText(0, _translate("Form", "1200"))
        self.Com_Baud_Combo.setItemText(1, _translate("Form", "2400"))
        self.Com_Baud_Combo.setItemText(2, _translate("Form", "4800"))
        self.Com_Baud_Combo.setItemText(3, _translate("Form", "9600"))
        self.Com_Baud_Combo.setItemText(4, _translate("Form", "14400"))
        self.Com_Baud_Combo.setItemText(5, _translate("Form", "19200"))
        self.Com_Baud_Combo.setItemText(6, _translate("Form", "38400"))
        self.Com_Baud_Combo.setItemText(7, _translate("Form", "43000"))
        self.Com_Baud_Combo.setItemText(8, _translate("Form", "57600"))
        self.Com_Baud_Combo.setItemText(9, _translate("Form", "76800"))
        self.Com_Baud_Combo.setItemText(10, _translate("Form", "115200"))
        self.Com_Baud_Combo.setItemText(11, _translate("Form", "128000"))
        self.Com_Baud_Combo.setItemText(12, _translate("Form", "230400"))
        self.Com_Baud_Combo.setItemText(13, _translate("Form", "256000"))
        self.Com_Baud_Combo.setItemText(14, _translate("Form", "460800"))
        self.Com_Baud_Combo.setItemText(15, _translate("Form", "921600"))
        self.Com_Baud_Combo.setItemText(16, _translate("Form", "1382400"))
        self.Com_Open_Button.setText(_translate("Form", "Open"))
        self.hexSending_checkBox.setText(_translate("Form", "16进制发送"))
        self.hexShowing_checkBox.setText(_translate("Form", "16进制显示"))
        self.Time_Label.setText(_translate("Form", "Time"))
        self.About_Button.setText(_translate("Form", "Made by PyQt5 - 查看源代码"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
