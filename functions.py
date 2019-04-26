# coding:utf-8
'''
定义按钮等功能
'''
from PyQt5.QtWidgets import QFileDialog
from zlib import crc32
from shared import settings, cmd_code


def open_file(parent):

    file_path, filetype = QFileDialog.getOpenFileName(
        parent, "select file", "./",
        "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔

    print('openfile: ' + file_path)
    # with open(file_path, 'rb') as opened_file:
    #     slice(opened_file, 20, 0xc0)
    with open(file_path, 'rb') as f:
        crc_code = crc32(f.read())
    parent.ui.file_num.setText(str(crc_code))
    parent.ui.file_path.setText(file_path)  # 更新显示信息


def change_channel(parent):
    # load settings
    # mode
    if parent.ui.comboBox.currentText() == 'A FTP':
        settings['virtual_channel_id'] = 3
    elif parent.ui.comboBox.currentText() == 'B FTP':
        settings['virtual_channel_id'] = 4


def cmd_change_channel(parent):
    # load cmd channels
    if parent.ui.cmd_channel.currentIndex() == 0:
        settings['cmd_channel_id'] = cmd_code['cmd_AB']
    elif parent.ui.cmd_channel.currentIndex() == 1:
        settings['cmd_channel_id'] = cmd_code['cmd_A']
    elif parent.ui.cmd_channel.currentIndex() == 2:
        settings['cmd_channel_id'] = cmd_code['cmd_B']
    print('[DEBUG] cmd channel id is ' + str(settings['cmd_channel_id']))
