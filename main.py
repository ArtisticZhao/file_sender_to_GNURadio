# coding:utf-8

##################################
# run with python 3.6 with pyqt5!#
##################################

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from file_send_ui import Ui_Dialog

import functions


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # setup UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # button functions
        self.ui.open_file_button.clicked.connect(
            lambda: functions.open_file(self))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
