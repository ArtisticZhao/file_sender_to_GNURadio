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
        Dialog.resize(715, 540)
        self.open_file_button = QtWidgets.QPushButton(Dialog)
        self.open_file_button.setGeometry(QtCore.QRect(350, 20, 71, 27))
        self.open_file_button.setObjectName("open_file_button")
        self.file_path = QtWidgets.QLineEdit(Dialog)
        self.file_path.setGeometry(QtCore.QRect(52, 20, 291, 27))
        self.file_path.setObjectName("file_path")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 24, 66, 17))
        self.label.setObjectName("label")
        self.log_area = QtWidgets.QTextEdit(Dialog)
        self.log_area.setGeometry(QtCore.QRect(10, 190, 411, 121))
        self.log_area.setObjectName("log_area")
        self.server_port = QtWidgets.QLineEdit(Dialog)
        self.server_port.setGeometry(QtCore.QRect(90, 116, 51, 27))
        self.server_port.setObjectName("server_port")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 66, 17))
        self.label_2.setObjectName("label_2")
        self.server_button = QtWidgets.QPushButton(Dialog)
        self.server_button.setGeometry(QtCore.QRect(320, 116, 101, 27))
        self.server_button.setObjectName("server_button")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 121, 51, 17))
        self.label_3.setObjectName("label_3")
        self.server_status = QtWidgets.QLabel(Dialog)
        self.server_status.setGeometry(QtCore.QRect(210, 120, 81, 20))
        self.server_status.setObjectName("server_status")
        self.transfer_process = QtWidgets.QProgressBar(Dialog)
        self.transfer_process.setGeometry(QtCore.QRect(10, 153, 411, 23))
        self.transfer_process.setProperty("value", 0)
        self.transfer_process.setTextVisible(True)
        self.transfer_process.setObjectName("transfer_process")
        self.send_button = QtWidgets.QPushButton(Dialog)
        self.send_button.setGeometry(QtCore.QRect(350, 80, 71, 27))
        self.send_button.setObjectName("send_button")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 84, 81, 17))
        self.label_4.setObjectName("label_4")
        self.sender_port = QtWidgets.QLineEdit(Dialog)
        self.sender_port.setGeometry(QtCore.QRect(90, 80, 51, 27))
        self.sender_port.setPlaceholderText("")
        self.sender_port.setObjectName("sender_port")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(150, 84, 51, 17))
        self.label_5.setObjectName("label_5")
        self.file_num = QtWidgets.QLineEdit(Dialog)
        self.file_num.setGeometry(QtCore.QRect(200, 80, 143, 27))
        self.file_num.setText("")
        self.file_num.setPlaceholderText("")
        self.file_num.setObjectName("file_num")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(250, 54, 51, 17))
        self.label_6.setObjectName("label_6")
        self.delay_us = QtWidgets.QLineEdit(Dialog)
        self.delay_us.setGeometry(QtCore.QRect(292, 50, 51, 27))
        self.delay_us.setPlaceholderText("")
        self.delay_us.setObjectName("delay_us")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(63, 50, 78, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 55, 41, 17))
        self.label_7.setObjectName("label_7")
        self.reset_sys_btn = QtWidgets.QPushButton(Dialog)
        self.reset_sys_btn.setGeometry(QtCore.QRect(630, 20, 71, 27))
        self.reset_sys_btn.setObjectName("reset_sys_btn")
        self.set_mode_btn = QtWidgets.QPushButton(Dialog)
        self.set_mode_btn.setGeometry(QtCore.QRect(630, 50, 71, 27))
        self.set_mode_btn.setObjectName("set_mode_btn")
        self.comboBox_mode = QtWidgets.QComboBox(Dialog)
        self.comboBox_mode.setGeometry(QtCore.QRect(500, 50, 121, 27))
        self.comboBox_mode.setObjectName("comboBox_mode")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.set_seed_btn = QtWidgets.QPushButton(Dialog)
        self.set_seed_btn.setGeometry(QtCore.QRect(630, 190, 71, 27))
        self.set_seed_btn.setObjectName("set_seed_btn")
        self.set_file_no_btn = QtWidgets.QPushButton(Dialog)
        self.set_file_no_btn.setGeometry(QtCore.QRect(580, 80, 121, 27))
        self.set_file_no_btn.setObjectName("set_file_no_btn")
        self.prefile_no = QtWidgets.QLineEdit(Dialog)
        self.prefile_no.setGeometry(QtCore.QRect(530, 80, 41, 27))
        self.prefile_no.setObjectName("prefile_no")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(440, 84, 71, 17))
        self.label_8.setObjectName("label_8")
        self.del_file_no = QtWidgets.QLineEdit(Dialog)
        self.del_file_no.setGeometry(QtCore.QRect(530, 106, 41, 27))
        self.del_file_no.setObjectName("del_file_no")
        self.del_file_btn = QtWidgets.QPushButton(Dialog)
        self.del_file_btn.setGeometry(QtCore.QRect(580, 106, 121, 27))
        self.del_file_btn.setObjectName("del_file_btn")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(440, 110, 71, 17))
        self.label_9.setObjectName("label_9")
        self.set_nid_btn = QtWidgets.QPushButton(Dialog)
        self.set_nid_btn.setGeometry(QtCore.QRect(580, 130, 121, 27))
        self.set_nid_btn.setObjectName("set_nid_btn")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(440, 134, 71, 17))
        self.label_10.setObjectName("label_10")
        self.nid = QtWidgets.QLineEdit(Dialog)
        self.nid.setGeometry(QtCore.QRect(530, 130, 41, 27))
        self.nid.setObjectName("nid")
        self.FTP_start_btn = QtWidgets.QPushButton(Dialog)
        self.FTP_start_btn.setGeometry(QtCore.QRect(440, 160, 101, 27))
        self.FTP_start_btn.setObjectName("FTP_start_btn")
        self.FTP_stop_btn = QtWidgets.QPushButton(Dialog)
        self.FTP_stop_btn.setGeometry(QtCore.QRect(600, 160, 101, 27))
        self.FTP_stop_btn.setObjectName("FTP_stop_btn")
        self.down_gongcan_btn = QtWidgets.QPushButton(Dialog)
        self.down_gongcan_btn.setGeometry(QtCore.QRect(630, 280, 71, 27))
        self.down_gongcan_btn.setObjectName("down_gongcan_btn")
        self.set_ant_btn_3 = QtWidgets.QPushButton(Dialog)
        self.set_ant_btn_3.setGeometry(QtCore.QRect(440, 280, 121, 27))
        self.set_ant_btn_3.setObjectName("set_ant_btn_3")
        self.file_block = QtWidgets.QLineEdit(Dialog)
        self.file_block.setGeometry(QtCore.QRect(440, 250, 181, 27))
        self.file_block.setObjectName("file_block")
        self.down_file_block_btn_4 = QtWidgets.QPushButton(Dialog)
        self.down_file_block_btn_4.setGeometry(QtCore.QRect(620, 250, 81, 27))
        self.down_file_block_btn_4.setObjectName("down_file_block_btn_4")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(440, 25, 71, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(10, 320, 101, 17))
        self.label_12.setObjectName("label_12")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 340, 691, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(14)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 6, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(130, 320, 201, 22))
        self.checkBox.setObjectName("checkBox")
        self.comboBox_recv_time = QtWidgets.QComboBox(Dialog)
        self.comboBox_recv_time.setGeometry(QtCore.QRect(410, 314, 181, 27))
        self.comboBox_recv_time.setObjectName("comboBox_recv_time")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(340, 320, 71, 21))
        self.label_13.setObjectName("label_13")
        self.cmd_channel = QtWidgets.QComboBox(Dialog)
        self.cmd_channel.setGeometry(QtCore.QRect(500, 20, 121, 27))
        self.cmd_channel.setObjectName("cmd_channel")
        self.cmd_channel.addItem("")
        self.cmd_channel.addItem("")
        self.cmd_channel.addItem("")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(440, 54, 71, 17))
        self.label_14.setObjectName("label_14")
        self.Seed = QtWidgets.QTextEdit(Dialog)
        self.Seed.setGeometry(QtCore.QRect(440, 190, 181, 51))
        self.Seed.setObjectName("Seed")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "file sender"))
        self.open_file_button.setText(_translate("Dialog", "Open..."))
        self.label.setText(_translate("Dialog", "Path"))
        self.server_port.setText(_translate("Dialog", "52001"))
        self.label_2.setText(_translate("Dialog", "GRC Port"))
        self.server_button.setText(_translate("Dialog", "Start Server"))
        self.label_3.setText(_translate("Dialog", "Status:"))
        self.server_status.setText(_translate("Dialog", "disconnect"))
        self.send_button.setText(_translate("Dialog", "Send..."))
        self.label_4.setText(_translate("Dialog", "Sender Port"))
        self.sender_port.setText(_translate("Dialog", "5234"))
        self.label_5.setText(_translate("Dialog", "File No."))
        self.label_6.setText(_translate("Dialog", "Delay:"))
        self.delay_us.setText(_translate("Dialog", "20000"))
        self.comboBox.setItemText(0, _translate("Dialog", "B FTP"))
        self.comboBox.setItemText(1, _translate("Dialog", "A FTP"))
        self.label_7.setText(_translate("Dialog", "Mode"))
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
        self.label_12.setText(_translate("Dialog", "本机工参 01H"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Dialog", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Dialog", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Dialog", "14"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "5"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "6"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "7"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "8"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Dialog", "配置状态"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Dialog", "数字信号强度指示1"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Dialog", "RF接收包计数"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("Dialog", "当前发送文件序号"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Dialog", "工作模式"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Dialog", "数字信号强度指示2"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("Dialog", "RF接收错误包计数"))
        item = self.tableWidget.item(1, 6)
        item.setText(_translate("Dialog", "当前发送文件长度"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Dialog", "通道状态标识1"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("Dialog", "模拟信号强度指示"))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("Dialog", "RF接收执行错误计数"))
        item = self.tableWidget.item(2, 6)
        item.setText(_translate("Dialog", "当前发送文件校验值"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Dialog", "通道状态标识2"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("Dialog", "PCB温度1"))
        item = self.tableWidget.item(3, 4)
        item.setText(_translate("Dialog", "RF接收纠错失败计数"))
        item = self.tableWidget.item(3, 6)
        item.setText(_translate("Dialog", "FTP发送数据块大小"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("Dialog", "通道状态标识3"))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("Dialog", "PCB温度2"))
        item = self.tableWidget.item(4, 4)
        item.setText(_translate("Dialog", "RF最近一条指令"))
        item = self.tableWidget.item(4, 6)
        item.setText(_translate("Dialog", "FTP发送成功包数"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Dialog", "通道状态标识4"))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("Dialog", "保留"))
        item = self.tableWidget.item(5, 4)
        item.setText(_translate("Dialog", "RF指令执行情况"))
        item = self.tableWidget.item(5, 6)
        item.setText(_translate("Dialog", "FTP发送缺失包数"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("Dialog", "+5V接收电流"))
        item = self.tableWidget.item(6, 2)
        item.setText(_translate("Dialog", "CAN发送包计数"))
        item = self.tableWidget.item(6, 4)
        item.setText(_translate("Dialog", "保留"))
        item = self.tableWidget.item(6, 6)
        item.setText(_translate("Dialog", "读取数据包计数"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("Dialog", "+5V接收电压"))
        item = self.tableWidget.item(7, 2)
        item.setText(_translate("Dialog", "CAN接收包计数"))
        item = self.tableWidget.item(7, 4)
        item.setText(_translate("Dialog", "FTP当前接收文件序号\n"
""))
        item = self.tableWidget.item(7, 6)
        item.setText(_translate("Dialog", "注入数据计数"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("Dialog", "+5V发射电流"))
        item = self.tableWidget.item(8, 2)
        item.setText(_translate("Dialog", "CAN错误包计数"))
        item = self.tableWidget.item(8, 4)
        item.setText(_translate("Dialog", "FTP当前接收文件长度"))
        item = self.tableWidget.item(8, 6)
        item.setText(_translate("Dialog", "复位计数"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("Dialog", "+5V发射电压"))
        item = self.tableWidget.item(9, 2)
        item.setText(_translate("Dialog", "CAN执行错误计数"))
        item = self.tableWidget.item(9, 4)
        item.setText(_translate("Dialog", "FTP当前接收文件校验值"))
        item = self.tableWidget.item(9, 6)
        item.setText(_translate("Dialog", "复位标识"))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("Dialog", "+3.3V电流"))
        item = self.tableWidget.item(10, 2)
        item.setText(_translate("Dialog", "CAN最近一条指令"))
        item = self.tableWidget.item(10, 4)
        item.setText(_translate("Dialog", "FTP接收数据块大小"))
        item = self.tableWidget.item(10, 6)
        item.setText(_translate("Dialog", "系统状态标识"))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("Dialog", "+3.3V电压"))
        item = self.tableWidget.item(11, 2)
        item.setText(_translate("Dialog", "CAN指令执行情况"))
        item = self.tableWidget.item(11, 4)
        item.setText(_translate("Dialog", "FTP接收成功包数"))
        item = self.tableWidget.item(11, 6)
        item.setText(_translate("Dialog", "ARM运行时间"))
        item = self.tableWidget.item(12, 0)
        item.setText(_translate("Dialog", "接收频偏1"))
        item = self.tableWidget.item(12, 2)
        item.setText(_translate("Dialog", "RF发送包计数"))
        item = self.tableWidget.item(12, 4)
        item.setText(_translate("Dialog", "FTP接收缺失包数"))
        item = self.tableWidget.item(12, 6)
        item.setText(_translate("Dialog", "AVR运行时间"))
        item = self.tableWidget.item(13, 0)
        item.setText(_translate("Dialog", "接收频偏2"))
        item = self.tableWidget.item(13, 2)
        item.setText(_translate("Dialog", "RF发送抛弃包计数"))
        item = self.tableWidget.item(13, 4)
        item.setText(_translate("Dialog", "目标CAN节点地址"))
        item = self.tableWidget.item(13, 6)
        item.setText(_translate("Dialog", "保留"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.checkBox.setText(_translate("Dialog", "显示最新一包并实时更新"))
        self.label_13.setText(_translate("Dialog", "接收时间"))
        self.cmd_channel.setItemText(0, _translate("Dialog", "AB机均执行"))
        self.cmd_channel.setItemText(1, _translate("Dialog", "A机指令"))
        self.cmd_channel.setItemText(2, _translate("Dialog", "B机指令"))
        self.label_14.setText(_translate("Dialog", "工作模式"))

