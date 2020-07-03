# coding:utf-8

###################################
# run with python 3.6 with pyqt5! #
###################################

import sys
from math import isnan

import configparser

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, pyqtSlot

from ui.file_send_ui import Ui_Dialog
from ui.status_ui import Ui_Form

import functions
import cmd_function

from tcp_core import tcp_server, kiss_frame, shutdown_flag
from c_lib.call_c_lib import Call_C_Lib_Task
from shared import settings, status, cmd_code
from ui.LedIndicatorWidget import LedIndicator
from db_handler import DBHandle


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # objects
        self.hcr_tcp_server = None
        self.grc_tcp_server = None
        self.sender_lib_thread = None

        # setup UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 设置状态指示灯控件
        self.LED_sender = LedIndicator(self)
        self.ui.horizontalLayout_Sender.addWidget(self.LED_sender)
        self.LED_sender.setFixedSize(20, 20)
        self.LED_sender.setDisabled(True)  # 禁止手动更改状态
        self.LED_GRC = LedIndicator(self)
        self.ui.horizontalLayout_GRC.addWidget(self.LED_GRC)
        self.LED_GRC.setFixedSize(20, 20)
        self.LED_GRC.setDisabled(True)  # 禁止手动更改状态

        self.load_ini()
        # 设置禁止更改窗口大小
        self.setFixedSize(self.width(), self.height())
        # 设置只显示关闭按钮
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        # child windows
        self.status_window = StatusForm()
        self.status_window.show()

        # a timer to update status
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.timer_click)  # 计时结束调用operate()方法
        self.timer.start(500)  # 设置计时间隔500ms并启动
        # Setup console output, emmit stdout
        sys.stdout = EmittingStream(textWritten=self.normal_output_written)

        # button functions
        self.ui.open_file_button.clicked.connect(
            lambda: functions.open_file(self))
        self.ui.server_button.clicked.connect(self.start_stop_server)
        self.ui.send_button.clicked.connect(self.sending)
        self.ui.reset_sys_btn.clicked.connect(
            lambda: cmd_function.cmd_reset(self))
        self.ui.set_mode_btn.clicked.connect(
            lambda: cmd_function.cmd_set_mod(self))
        self.ui.set_file_no_btn.clicked.connect(
            lambda: cmd_function.cmd_set_pre_file(self))
        self.ui.del_file_btn.clicked.connect(
            lambda: cmd_function.cmd_del_file(self))
        self.ui.set_nid_btn.clicked.connect(
            lambda: cmd_function.cmd_set_nid(self))

        self.ui.FTP_start_btn.clicked.connect(
            lambda: cmd_function.cmd_ftp_start(self))
        self.ui.FTP_stop_btn.clicked.connect(
            lambda: cmd_function.cmd_ftp_stop(self))

        self.ui.set_seed_btn.clicked.connect(
            lambda: cmd_function.cmd_set_seed(self))
        self.ui.down_file_block_btn_4.clicked.connect(
            lambda: cmd_function.cmd_get_file_block(self))
        self.ui.set_ant_btn_3.clicked.connect(
            lambda: cmd_function.cmd_switch_antenna(self))
        self.ui.down_gongcan_btn.clicked.connect(
            lambda: cmd_function.cmd_get_status(self))
        self.ui.set_speed_btn.clicked.connect(
            lambda: cmd_function.cmd_set_speed(self))
        self.ui.set_sat_block.clicked.connect(
            lambda: cmd_function.cmd_set_sat_block_num(self))
        self.ui.rf_gongcan_btn.clicked.connect(
            lambda: cmd_function.cmd_gongcan_download_time(self))
        self.ui.set_hex_btn.clicked.connect(
            lambda: cmd_function.cmd_send_hex(self)
        )

        self.ui.pushButton_childwindow.clicked.connect(self.status_window.show)

        # comboBox functions
        self.ui.comboBox.currentTextChanged.connect(
            lambda: functions.change_channel(self))
        self.ui.cmd_channel.currentTextChanged.connect(
            lambda: functions.cmd_change_channel(self))

        # checkbox functions
        self.ui.checkBox_encrypt.stateChanged.connect(
            lambda: functions.encrypt_status_changed(self))

        # lineedit functions
        # self.ui.delay_us.textChanged.connect(
        #     lambda: functions.change_timeout(self))
        self.ui.craft_id.editingFinished.connect(
            lambda: functions.change_craft_id(self))

        # GRC状态改变
        self.LED_GRC.toggled.connect(
            lambda: self.status_window.set_signal(self.grc_tcp_server))

        # 读取AES_key
        functions.open_aes_key(self)

    def closeEvent(self, event):
        # 窗口关闭事件
        if self.ui.server_button.text() == 'Start Server':
            # 没有程序执行, 可以关闭!
            kiss_frame.shutdown()
            self.status_window.db_handler.commit_all()  # 输入数据库
            self.status_window.close()
            # 存储数据库

            event.accept()  # 关闭窗口
        else:
            reply = QtWidgets.QMessageBox.question(
                self, u'警告', u'TCP Server已经启动, 确认退出?',
                QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                # 关闭服务器
                self.start_stop_server()
                self.status_window.db_handler.commit_all()  # 输入数据库
                self.status_window.close()
                event.accept()  # 关闭窗口
            else:
                event.ignore()  # 忽视点击X事件

    def timer_click(self):
        # if thread run out:
        if self.sender_lib_thread is not None:
            if not self.sender_lib_thread.isRunning():
                self.ui.send_button.setText("send")
                self.sender_lib_thread = None
                self.ui.transfer_process.setValue(100)
            else:
                # 刷新进度
                fprocess = self.sender_lib_thread.libc.process()
                if isnan(fprocess):  # 胡学姐的程序里面最开始的时候会返回nan
                    fprocess = 0
                self.ui.transfer_process.setValue(int(fprocess * 100))
        # 刷新状态
        self.LED_sender.setChecked(status['HCR_Online'])
        self.LED_GRC.setChecked(status['GRC_Online'])

    def load_ini(self):
        cf = configparser.ConfigParser()
        cf.read("data/config.ini")
        self.ui.craft_id.setText(cf.get("init", "ID"))
        self.ui.delay_us.setText(cf.get("init", "PacketTime"))
        self.ui.file_path.setText(cf.get("init", "Path"))
        self.ui.block_timeout.setText(cf.get("init", "BlockTime"))
        self.ui.block_num.setText(cf.get("init", "BlockNum"))
        self.ui.sender_port.setText(cf.get("init", "SenderPort"))
        self.ui.server_port.setText(cf.get("init", "GrcPort"))
        self.ui.prefile_no.setText(cf.get("init", "PrefileNo"))
        self.ui.del_file_no.setText(cf.get("init", "DelFileNo"))
        self.ui.nid.setText(cf.get("init", "NID"))
        self.ui.sat_block_num.setText(cf.get("init", "SatBlockNum"))
        self.ui.file_block.setText(cf.get("init", "FileBlock"))

    def refresh_status(self, str):
        self.ui.server_status.setText(str)

    def start_stop_server(self):
        if (self.ui.server_button.text() == 'Start Server'):
            # load settings
            # mode
            functions.change_channel(self)  # update mode
            print("debug: virtual_channel_id= " +
                  str(settings['virtual_channel_id']))
            # 启动server
            self.ui.server_button.setDisabled(True)
            # TODO 如果不加这句在stopserver之后再起启动线程将无法同意客户端的连接  应该优化到类内部
            shutdown_flag[0] = False
            # hcr server start!
            self.hcr_tcp_server = tcp_server(
                int(self.ui.sender_port.text()), 'hcr')
            self.hcr_tcp_server.start()
            print("start [hcr] tcp server at port: " +
                  self.ui.sender_port.text())
            # grc server start!
            self.grc_tcp_server = tcp_server(
                int(self.ui.server_port.text()), 'grc')
            self.grc_tcp_server.start()
            print("start [grc] tcp server at port: " +
                  self.ui.server_port.text())
            self.ui.server_button.setText("Stop Server")
            self.ui.server_button.setEnabled(True)
        else:
            # stop server
            self.ui.server_button.setDisabled(True)
            self.hcr_tcp_server.shutdown()
            self.grc_tcp_server.shutdown()
            kiss_frame.shutdown()
            print("tcp server shutdown")
            self.ui.server_button.setText("Start Server")
            self.ui.server_button.setEnabled(True)

    def sending(self, parameter_list):
        # do input check
        if self.ui.file_path.text() == '':
            print("[ERROR] please SELECT a file")
            return
        # update timeout value
        timeout = int(self.ui.delay_us.text())
        settings['timeout'] = timeout * 1.5 / 1000
        print('timeout changed: ' + str(settings['timeout']) + 's')
        # call lib
        if self.sender_lib_thread is None:
            if not status['GRC_Online']:
                print("[ERROR] GRC is NOT Online!")
                return
            print('[DEBUG] 块超时时间(ms)' + self.ui.block_timeout.text())
            print('[DEBUG] 块包数:' + self.ui.block_num.text())
            print('[DEBUG] 包间隔(ms):' + self.ui.delay_us.text())
            self.sender_lib_thread = Call_C_Lib_Task(
                self.ui.file_path.text(), int(self.ui.sender_port.text()),
                int(self.ui.file_num.text(), 16), int(self.ui.delay_us.text()),
                int(self.ui.block_num.text()), int(
                    self.ui.block_timeout.text()))
            self.sender_lib_thread.start()
            # connect slot
            self.sender_lib_thread.file_send_ok.connect(self.file_send_res)
            self.ui.send_button.setText("cancel")
        else:
            if self.sender_lib_thread.isRunning():
                print("running! to kill it!!!")
                self.sender_lib_thread.libc.close_socketfd()
                while self.sender_lib_thread.isRunning():
                    continue
                self.ui.send_button.setText("send")
                # 解除槽链接
                self.sender_lib_thread.file_send_ok.disconnect(
                    self.file_send_res)
                self.sender_lib_thread = None
            else:
                print("not running")

    @pyqtSlot(int)
    def file_send_res(self, res):
        if res == 0:
            # send OK!
            QtWidgets.QMessageBox.information(self, "文件传输结果", "文件传输成功!")
        elif res == 2:
            QtWidgets.QMessageBox.information(self, "文件传输结果", "传输已取消!")
        else:
            QtWidgets.QMessageBox.information(self, "文件传输结果", "文件传输失败!")

    def normal_output_written(self, text):
        """ Initial output console length and buffer.
        """
        # Append text to the QTextEdit.
        cursor = self.ui.log_area.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.log_area.setTextCursor(cursor)
        self.ui.log_area.ensureCursorVisible()


class StatusForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # setup UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # 自动列宽
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents)
        # 创建数据库链接
        self.db_handler = DBHandle()

        self.ui.pushButton_refresh.clicked.connect(self.refresh_db_list)
        self.ui.pushButton_inquire.clicked.connect(self.refresh_status)

    def set_signal(self, obj):
        # 槽
        obj.dataChanged.connect(self.update_status)

    def refresh_db_list(self):
        # 先存数据库
        self.db_handler.commit_all()
        if self.ui.comboBox_sat.currentText() == 'A机':
            rlist = self.db_handler.get_all('A_status')
        else:
            rlist = self.db_handler.get_all('B_status')
        self.ui.comboBox_recv_time.clear()
        for each in rlist:
            self.ui.comboBox_recv_time.addItem(each[0])

    def refresh_status(self):
        if not self.isVisible:  # 当窗口隐藏的时候不刷新
            return
        if self.ui.comboBox_sat.currentText() == 'A机':
            table_name = 'A_status'
        else:
            table_name = 'B_status'
        d_status = self.db_handler.get_a_log(
            table_name, self.ui.comboBox_recv_time.currentText())
        if table_name == 'A_status':
            table = self.ui.tableWidget
        else:
            table = self.ui.tableWidget_2
        # 根据查询结果更新内容
        for j in range(0, table.columnCount(), 2):
            for i in range(0, table.rowCount()):
                val = d_status.get(table.item(i, j).text())
                table.setItem(i, j + 1, QtWidgets.QTableWidgetItem(val))

    @pyqtSlot(dict)
    def update_status(self, s_dict):
        try:
            sat = s_dict.pop('sat')  # 辅助内容, 只在此函数中作用, 删除防止存储
            craft_id = s_dict.pop('craft_id')  # 删除防止存储
        except KeyError:
            print('[DEBUG] no sat')
        # 存储
        if sat == cmd_code['cmd_A']:
            # A 星
            self.db_handler.insert_a_log('A_status', s_dict)
        else:
            # B 星
            self.db_handler.insert_a_log('B_status', s_dict)
        # 更新航天器ID
        self.ui.lineEdit.setText(str(hex(craft_id)))
        # 更新工参
        if self.ui.checkBox_realtime.isChecked():
            # 更新时间
            self.ui.comboBox_recv_time.addItem(s_dict['recv_time'])  # 添加
            self.ui.comboBox_recv_time.setCurrentIndex(
                self.ui.comboBox_recv_time.findText(s_dict['recv_time']))
            if sat == cmd_code['cmd_A']:
                # A 星
                self.ui.comboBox_sat.setCurrentIndex(0)
            else:
                # B 星
                self.ui.comboBox_sat.setCurrentIndex(1)
            if sat == cmd_code['cmd_A']:
                table = self.ui.tableWidget
            else:
                table = self.ui.tableWidget_2
            for j in range(0, table.columnCount(), 2):
                for i in range(0, table.rowCount()):
                    val = s_dict.get(table.item(i, j).text())
                    table.setItem(
                        i, j + 1, QtWidgets.QTableWidgetItem(val))

    def closeEvent(self, event):
        # 窗口关闭事件
        self.hide()
        event.ignore()  # 忽视点击X事件


class EmittingStream(QtCore.QObject):
    '''
    重定向print输出
    '''
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
