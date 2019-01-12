# coding:utf-8

###################################
# run with python 3.6 with pyqt5! #
###################################

import sys

from PyQt5 import QtWidgets, QtCore
from file_send_ui import Ui_Dialog

import functions
from tcp_core import tcp_server


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # objects
        self.tcp_server = None

        # setup UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Setup console output, emmit stdout
        sys.stdout = EmittingStream(textWritten=self.normal_output_written)

        # button functions

        self.ui.open_file_button.clicked.connect(
            lambda: functions.open_file(self))
        self.ui.server_button.clicked.connect(self.start_stop_server)

    def refresh_status(self, str):
        self.ui.server_status.setText(str)

    def start_stop_server(self):
        if (self.ui.server_button.text() == 'Start Server'):
            # 启动server
            self.ui.server_button.setDisabled(True)
            self.tcp_server = tcp_server(int(self.ui.server_port.text()))
            self.tcp_server.start()
            print("start tcp server at port: " + self.ui.server_port.text())
            self.ui.server_button.setText("Stop Server")
            self.ui.server_button.setEnabled(True)
        else:
            # stop server
            self.ui.server_button.setDisabled(True)
            self.tcp_server.shutdown()
            print("tcp server shutdown")
            self.ui.server_button.setText("Start Server")
            self.ui.server_button.setEnabled(True)

    def normal_output_written(self, text):
        """ Initial output console length and buffer.
        """
        # Append text to the QTextEdit.
        str_buf = self.ui.log_area.toPlainText()
        str_buf = str_buf + text
        length = len(str_buf)

        maxLength = 3000
        if (length > maxLength):
            str_buf.remove(0, length - maxLength)

        self.ui.log_area.setText(str_buf)
        textCursor = self.ui.log_area.textCursor()
        self.ui.log_area.setText(str_buf)
        textCursor.setPosition(length)
        self.ui.log_area.setTextCursor(textCursor)


# class Signal(QtCore.QObject):
#     server_refresh_Signal = pyqtSignal(str)

#     def __init__(self):
#         self.parent = None

#     def set_parent(self, obj):
#         self.parent = obj

#     def set_connection(self):
#         self.server_refresh_Signal.connect(self.parent.refresh_status)

# signals = Signal()


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
