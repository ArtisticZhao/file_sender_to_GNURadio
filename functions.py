# coding:utf-8
'''
定义按钮等功能
'''
from PyQt5.QtWidgets import QFileDialog
from slice import slice


def open_file(parent):

    file_path, filetype = QFileDialog.getOpenFileName(
        parent, "select file", "./",
        "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔

    print('openfile: ' + file_path)
    with open(file_path, 'rb') as opened_file:
        slice(opened_file, 20, 0xc0)

    parent.ui.file_path.setText(file_path)
