# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_send.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 279)
        self.open_file_button = QtWidgets.QPushButton(Dialog)
        self.open_file_button.setGeometry(QtCore.QRect(320, 20, 71, 27))
        self.open_file_button.setObjectName("open_file_button")
        self.file_path = QtWidgets.QLineEdit(Dialog)
        self.file_path.setGeometry(QtCore.QRect(52, 20, 261, 27))
        self.file_path.setObjectName("file_path")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 24, 66, 17))
        self.label.setObjectName("label")
        self.log_area = QtWidgets.QTextEdit(Dialog)
        self.log_area.setGeometry(QtCore.QRect(10, 170, 381, 101))
        self.log_area.setObjectName("log_area")
        self.server_port = QtWidgets.QLineEdit(Dialog)
        self.server_port.setGeometry(QtCore.QRect(80, 96, 51, 27))
        self.server_port.setObjectName("server_port")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 66, 17))
        self.label_2.setObjectName("label_2")
        self.server_button = QtWidgets.QPushButton(Dialog)
        self.server_button.setGeometry(QtCore.QRect(290, 96, 101, 27))
        self.server_button.setObjectName("server_button")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 101, 51, 17))
        self.label_3.setObjectName("label_3")
        self.server_status = QtWidgets.QLabel(Dialog)
        self.server_status.setGeometry(QtCore.QRect(200, 100, 81, 20))
        self.server_status.setObjectName("server_status")
        self.transfer_process = QtWidgets.QProgressBar(Dialog)
        self.transfer_process.setGeometry(QtCore.QRect(10, 133, 381, 23))
        self.transfer_process.setProperty("value", 0)
        self.transfer_process.setTextVisible(True)
        self.transfer_process.setObjectName("transfer_process")
        self.send_button = QtWidgets.QPushButton(Dialog)
        self.send_button.setGeometry(QtCore.QRect(320, 60, 71, 27))
        self.send_button.setObjectName("send_button")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 64, 91, 17))
        self.label_4.setObjectName("label_4")
        self.sender_port = QtWidgets.QLineEdit(Dialog)
        self.sender_port.setGeometry(QtCore.QRect(100, 60, 51, 27))
        self.sender_port.setText("")
        self.sender_port.setPlaceholderText("")
        self.sender_port.setObjectName("sender_port")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(160, 64, 91, 17))
        self.label_5.setObjectName("label_5")
        self.file_num = QtWidgets.QLineEdit(Dialog)
        self.file_num.setGeometry(QtCore.QRect(260, 60, 51, 27))
        self.file_num.setText("")
        self.file_num.setPlaceholderText("")
        self.file_num.setObjectName("file_num")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "file sender"))
        self.open_file_button.setText(_translate("Dialog", "Open..."))
        self.label.setText(_translate("Dialog", "Path"))
        self.label_2.setText(_translate("Dialog", "GRC Port"))
        self.server_button.setText(_translate("Dialog", "Start Server"))
        self.label_3.setText(_translate("Dialog", "Status:"))
        self.server_status.setText(_translate("Dialog", "disconnect"))
        self.send_button.setText(_translate("Dialog", "Send..."))
        self.label_4.setText(_translate("Dialog", "Sender Port"))
        self.label_5.setText(_translate("Dialog", "File Number"))

