# coding:utf-8

###################################
# run with python 3.6 with pyqt5! #
###################################

import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer

from file_send_ui import Ui_Dialog

import functions
import cmd_function

from tcp_core import tcp_server, kiss_frame
from call_c_lib import Call_C_Lib_Task
from shared import settings


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
        # 设置禁止更改窗口大小
        self.setFixedSize(self.width(), self.height())
        # 设置只显示关闭按钮
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
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

        # checkbox functions
        self.ui.comboBox.currentTextChanged.connect(
            lambda: functions.change_channel(self))
        self.ui.cmd_channel.currentTextChanged.connect(
            lambda: functions.cmd_change_channel(self))

    def timer_click(self):
        # if thread run out:
        if self.sender_lib_thread is not None:
            if not self.sender_lib_thread.is_alive():
                self.ui.send_button.setText("send")
                self.sender_lib_thread = None

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

        # call lib
        if self.sender_lib_thread is None:
            self.sender_lib_thread = Call_C_Lib_Task(
                self.ui.file_path.text(), int(self.ui.sender_port.text()),
                int(self.ui.file_num.text()), int(self.ui.delay_us.text()))
            self.sender_lib_thread.start()

            self.ui.send_button.setText("cancel")
        else:
            if self.sender_lib_thread.is_alive():
                print("running! to kill it!!!")
                self.sender_lib_thread.libc.close_socketfd()
                while self.sender_lib_thread.is_alive():
                    continue
                self.ui.send_button.setText("send")
                self.sender_lib_thread = None
            else:
                print("not running")

    def normal_output_written(self, text):
        """ Initial output console length and buffer.
        """
        # Append text to the QTextEdit.
        str_buf = self.ui.log_area.toPlainText()
        str_buf = str_buf + text
        length = len(str_buf)

        # TODO 清空

        self.ui.log_area.setText(str_buf)
        textCursor = self.ui.log_area.textCursor()
        self.ui.log_area.setText(str_buf)
        textCursor.setPosition(length)
        self.ui.log_area.setTextCursor(textCursor)


class EmittingStream(QtCore.QObject):
    '''
    重定向print输出
    '''
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
