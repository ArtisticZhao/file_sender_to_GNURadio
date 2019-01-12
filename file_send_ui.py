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
        Dialog.resize(400, 300)
        self.open_file_button = QtWidgets.QPushButton(Dialog)
        self.open_file_button.setGeometry(QtCore.QRect(320, 30, 71, 27))
        self.open_file_button.setObjectName("open_file_button")
        self.file_path = QtWidgets.QLineEdit(Dialog)
        self.file_path.setGeometry(QtCore.QRect(52, 30, 261, 27))
        self.file_path.setObjectName("file_path")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 34, 66, 17))
        self.label.setObjectName("label")
        self.log_area = QtWidgets.QTextEdit(Dialog)
        self.log_area.setGeometry(QtCore.QRect(10, 160, 381, 121))
        self.log_area.setObjectName("log_area")
        self.server_port = QtWidgets.QLineEdit(Dialog)
        self.server_port.setGeometry(QtCore.QRect(80, 70, 51, 27))
        self.server_port.setObjectName("server_port")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 74, 66, 17))
        self.label_2.setObjectName("label_2")
        self.server_button = QtWidgets.QPushButton(Dialog)
        self.server_button.setGeometry(QtCore.QRect(290, 70, 101, 27))
        self.server_button.setObjectName("server_button")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 74, 51, 17))
        self.label_3.setObjectName("label_3")
        self.server_status = QtWidgets.QLabel(Dialog)
        self.server_status.setGeometry(QtCore.QRect(200, 74, 81, 20))
        self.server_status.setObjectName("server_status")
        self.transfer_process = QtWidgets.QProgressBar(Dialog)
        self.transfer_process.setGeometry(QtCore.QRect(10, 120, 301, 23))
        self.transfer_process.setProperty("value", 0)
        self.transfer_process.setTextVisible(True)
        self.transfer_process.setObjectName("transfer_process")
        self.send_button = QtWidgets.QPushButton(Dialog)
        self.send_button.setGeometry(QtCore.QRect(320, 117, 71, 27))
        self.send_button.setObjectName("send_button")

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

