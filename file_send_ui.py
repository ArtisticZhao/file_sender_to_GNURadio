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
        Dialog.resize(715, 344)
        self.open_file_button = QtWidgets.QPushButton(Dialog)
        self.open_file_button.setGeometry(QtCore.QRect(350, 40, 71, 27))
        self.open_file_button.setObjectName("open_file_button")
        self.file_path = QtWidgets.QLineEdit(Dialog)
        self.file_path.setGeometry(QtCore.QRect(52, 40, 291, 27))
        self.file_path.setObjectName("file_path")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 44, 66, 17))
        self.label.setObjectName("label")
        self.log_area = QtWidgets.QTextEdit(Dialog)
        self.log_area.setGeometry(QtCore.QRect(10, 206, 411, 121))
        self.log_area.setObjectName("log_area")
        self.server_button = QtWidgets.QPushButton(Dialog)
        self.server_button.setGeometry(QtCore.QRect(320, 136, 101, 27))
        self.server_button.setObjectName("server_button")
        self.transfer_process = QtWidgets.QProgressBar(Dialog)
        self.transfer_process.setGeometry(QtCore.QRect(10, 170, 411, 23))
        self.transfer_process.setProperty("value", 0)
        self.transfer_process.setTextVisible(True)
        self.transfer_process.setObjectName("transfer_process")
        self.send_button = QtWidgets.QPushButton(Dialog)
        self.send_button.setGeometry(QtCore.QRect(350, 100, 71, 27))
        self.send_button.setObjectName("send_button")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(190, 104, 91, 17))
        self.label_5.setObjectName("label_5")
        self.file_num = QtWidgets.QLineEdit(Dialog)
        self.file_num.setGeometry(QtCore.QRect(272, 100, 71, 27))
        self.file_num.setText("")
        self.file_num.setPlaceholderText("")
        self.file_num.setObjectName("file_num")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 74, 51, 20))
        self.label_6.setObjectName("label_6")
        self.delay_us = QtWidgets.QLineEdit(Dialog)
        self.delay_us.setGeometry(QtCore.QRect(63, 70, 51, 27))
        self.delay_us.setPlaceholderText("")
        self.delay_us.setObjectName("delay_us")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(70, 10, 78, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 15, 71, 17))
        self.label_7.setObjectName("label_7")
        self.reset_sys_btn = QtWidgets.QPushButton(Dialog)
        self.reset_sys_btn.setGeometry(QtCore.QRect(630, 10, 71, 27))
        self.reset_sys_btn.setObjectName("reset_sys_btn")
        self.set_mode_btn = QtWidgets.QPushButton(Dialog)
        self.set_mode_btn.setGeometry(QtCore.QRect(630, 40, 71, 27))
        self.set_mode_btn.setObjectName("set_mode_btn")
        self.comboBox_mode = QtWidgets.QComboBox(Dialog)
        self.comboBox_mode.setGeometry(QtCore.QRect(500, 40, 121, 27))
        self.comboBox_mode.setObjectName("comboBox_mode")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.set_seed_btn = QtWidgets.QPushButton(Dialog)
        self.set_seed_btn.setGeometry(QtCore.QRect(630, 180, 71, 27))
        self.set_seed_btn.setObjectName("set_seed_btn")
        self.set_file_no_btn = QtWidgets.QPushButton(Dialog)
        self.set_file_no_btn.setGeometry(QtCore.QRect(580, 70, 121, 27))
        self.set_file_no_btn.setObjectName("set_file_no_btn")
        self.prefile_no = QtWidgets.QLineEdit(Dialog)
        self.prefile_no.setGeometry(QtCore.QRect(530, 70, 41, 27))
        self.prefile_no.setObjectName("prefile_no")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(440, 74, 71, 17))
        self.label_8.setObjectName("label_8")
        self.del_file_no = QtWidgets.QLineEdit(Dialog)
        self.del_file_no.setGeometry(QtCore.QRect(530, 96, 41, 27))
        self.del_file_no.setObjectName("del_file_no")
        self.del_file_btn = QtWidgets.QPushButton(Dialog)
        self.del_file_btn.setGeometry(QtCore.QRect(580, 96, 121, 27))
        self.del_file_btn.setObjectName("del_file_btn")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(440, 100, 71, 17))
        self.label_9.setObjectName("label_9")
        self.set_nid_btn = QtWidgets.QPushButton(Dialog)
        self.set_nid_btn.setGeometry(QtCore.QRect(580, 120, 121, 27))
        self.set_nid_btn.setObjectName("set_nid_btn")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(440, 124, 71, 17))
        self.label_10.setObjectName("label_10")
        self.nid = QtWidgets.QLineEdit(Dialog)
        self.nid.setGeometry(QtCore.QRect(530, 120, 41, 27))
        self.nid.setObjectName("nid")
        self.FTP_start_btn = QtWidgets.QPushButton(Dialog)
        self.FTP_start_btn.setGeometry(QtCore.QRect(440, 150, 101, 27))
        self.FTP_start_btn.setObjectName("FTP_start_btn")
        self.FTP_stop_btn = QtWidgets.QPushButton(Dialog)
        self.FTP_stop_btn.setGeometry(QtCore.QRect(600, 150, 101, 27))
        self.FTP_stop_btn.setObjectName("FTP_stop_btn")
        self.down_gongcan_btn = QtWidgets.QPushButton(Dialog)
        self.down_gongcan_btn.setGeometry(QtCore.QRect(630, 300, 71, 27))
        self.down_gongcan_btn.setObjectName("down_gongcan_btn")
        self.set_ant_btn_3 = QtWidgets.QPushButton(Dialog)
        self.set_ant_btn_3.setGeometry(QtCore.QRect(440, 300, 121, 27))
        self.set_ant_btn_3.setObjectName("set_ant_btn_3")
        self.file_block = QtWidgets.QLineEdit(Dialog)
        self.file_block.setGeometry(QtCore.QRect(440, 240, 181, 27))
        self.file_block.setObjectName("file_block")
        self.down_file_block_btn_4 = QtWidgets.QPushButton(Dialog)
        self.down_file_block_btn_4.setGeometry(QtCore.QRect(620, 240, 81, 27))
        self.down_file_block_btn_4.setObjectName("down_file_block_btn_4")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(440, 15, 71, 17))
        self.label_11.setObjectName("label_11")
        self.cmd_channel = QtWidgets.QComboBox(Dialog)
        self.cmd_channel.setGeometry(QtCore.QRect(500, 10, 121, 27))
        self.cmd_channel.setObjectName("cmd_channel")
        self.cmd_channel.addItem("")
        self.cmd_channel.addItem("")
        self.cmd_channel.addItem("")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(440, 44, 71, 17))
        self.label_14.setObjectName("label_14")
        self.Seed = QtWidgets.QTextEdit(Dialog)
        self.Seed.setGeometry(QtCore.QRect(440, 180, 181, 51))
        self.Seed.setObjectName("Seed")
        self.pushButton_childwindow = QtWidgets.QPushButton(Dialog)
        self.pushButton_childwindow.setGeometry(QtCore.QRect(220, 136, 97, 27))
        self.pushButton_childwindow.setObjectName("pushButton_childwindow")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 100, 171, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_Sender = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_Sender.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Sender.setObjectName("horizontalLayout_Sender")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_Sender.addWidget(self.label_4)
        self.sender_port = QtWidgets.QLineEdit(self.layoutWidget)
        self.sender_port.setMaximumSize(QtCore.QSize(51, 16777215))
        self.sender_port.setPlaceholderText("")
        self.sender_port.setObjectName("sender_port")
        self.horizontalLayout_Sender.addWidget(self.sender_port)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 136, 171, 29))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_GRC = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_GRC.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_GRC.setObjectName("horizontalLayout_GRC")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_GRC.addWidget(self.label_2)
        self.server_port = QtWidgets.QLineEdit(self.layoutWidget1)
        self.server_port.setMaximumSize(QtCore.QSize(51, 16777215))
        self.server_port.setObjectName("server_port")
        self.horizontalLayout_GRC.addWidget(self.server_port)
        self.comboBox_speed = QtWidgets.QComboBox(Dialog)
        self.comboBox_speed.setGeometry(QtCore.QRect(500, 270, 121, 27))
        self.comboBox_speed.setObjectName("comboBox_speed")
        self.comboBox_speed.addItem("")
        self.comboBox_speed.addItem("")
        self.set_speed_btn = QtWidgets.QPushButton(Dialog)
        self.set_speed_btn.setGeometry(QtCore.QRect(630, 270, 71, 27))
        self.set_speed_btn.setObjectName("set_speed_btn")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(440, 274, 71, 17))
        self.label_15.setObjectName("label_15")
        self.checkBox_encrypt = QtWidgets.QCheckBox(Dialog)
        self.checkBox_encrypt.setGeometry(QtCore.QRect(290, 12, 131, 22))
        self.checkBox_encrypt.setObjectName("checkBox_encrypt")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(120, 74, 21, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(160, 74, 51, 20))
        self.label_13.setObjectName("label_13")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(262, 74, 21, 20))
        self.label_16.setObjectName("label_16")
        self.block_timeout = QtWidgets.QLineEdit(Dialog)
        self.block_timeout.setGeometry(QtCore.QRect(210, 70, 51, 27))
        self.block_timeout.setPlaceholderText("")
        self.block_timeout.setObjectName("block_timeout")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(314, 74, 51, 20))
        self.label_17.setObjectName("label_17")
        self.block_num = QtWidgets.QLineEdit(Dialog)
        self.block_num.setGeometry(QtCore.QRect(370, 70, 51, 27))
        self.block_num.setPlaceholderText("")
        self.block_num.setObjectName("block_num")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "file sender"))
        self.open_file_button.setText(_translate("Dialog", "Open..."))
        self.label.setText(_translate("Dialog", "Path"))
        self.server_button.setText(_translate("Dialog", "Start Server"))
        self.send_button.setText(_translate("Dialog", "Send..."))
        self.label_5.setText(_translate("Dialog", "File No. HEX"))
        self.label_6.setText(_translate("Dialog", "包间隔:"))
        self.delay_us.setText(_translate("Dialog", "200"))
        self.comboBox.setItemText(0, _translate("Dialog", "B FTP"))
        self.comboBox.setItemText(1, _translate("Dialog", "A FTP"))
        self.label_7.setText(_translate("Dialog", "数传模式"))
        self.reset_sys_btn.setText(_translate("Dialog", "本机复位"))
        self.set_mode_btn.setText(_translate("Dialog", "设置模式"))
        self.comboBox_mode.setItemText(0, _translate("Dialog", "缓存模式"))
        self.comboBox_mode.setItemText(1, _translate("Dialog", "实时转发模式"))
        self.comboBox_mode.setItemText(2, _translate("Dialog", "数据注入模式"))
        self.set_seed_btn.setText(_translate("Dialog", "Set Seed"))
        self.set_file_no_btn.setText(_translate("Dialog", "设置待操作文件"))
        self.label_8.setText(_translate("Dialog", "文件序号"))
        self.del_file_btn.setText(_translate("Dialog", "删除文件"))
        self.label_9.setText(_translate("Dialog", "文件序号"))
        self.set_nid_btn.setText(_translate("Dialog", "设置nid"))
        self.label_10.setText(_translate("Dialog", "目标nid"))
        self.FTP_start_btn.setText(_translate("Dialog", "FTP开始传输"))
        self.FTP_stop_btn.setText(_translate("Dialog", "FTP结束传输"))
        self.down_gongcan_btn.setText(_translate("Dialog", "下传工参"))
        self.set_ant_btn_3.setText(_translate("Dialog", "切换天线至本机"))
        self.down_file_block_btn_4.setText(_translate("Dialog", "下传文件块"))
        self.label_11.setText(_translate("Dialog", "指令信道"))
        self.cmd_channel.setItemText(0, _translate("Dialog", "AB机均执行"))
        self.cmd_channel.setItemText(1, _translate("Dialog", "A机指令"))
        self.cmd_channel.setItemText(2, _translate("Dialog", "B机指令"))
        self.label_14.setText(_translate("Dialog", "工作模式"))
        self.pushButton_childwindow.setText(_translate("Dialog", "显示工参"))
        self.label_4.setText(_translate("Dialog", "Sender Port"))
        self.sender_port.setText(_translate("Dialog", "5234"))
        self.label_2.setText(_translate("Dialog", "GRC Port"))
        self.server_port.setText(_translate("Dialog", "52001"))
        self.comboBox_speed.setItemText(0, _translate("Dialog", "12kbps"))
        self.comboBox_speed.setItemText(1, _translate("Dialog", "100kbps"))
        self.set_speed_btn.setText(_translate("Dialog", "设置速率"))
        self.label_15.setText(_translate("Dialog", "接收速率"))
        self.checkBox_encrypt.setText(_translate("Dialog", "FTP与指令加密"))
        self.label_12.setText(_translate("Dialog", "ms"))
        self.label_13.setText(_translate("Dialog", "块超时:"))
        self.label_16.setText(_translate("Dialog", "ms"))
        self.block_timeout.setText(_translate("Dialog", "200"))
        self.label_17.setText(_translate("Dialog", "块包数:"))
        self.block_num.setText(_translate("Dialog", "200"))

