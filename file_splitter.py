# coding:utf-8
'''
文件分割类,提供文件读取,分割, 加头等功能
'''


class File_Splitor(object):
    def __init__(self):
        self.file = None
        self.send_list = []  # 发送队列, 用于存储分割且加好包头包尾的内容

    def load_file(self, path):
        if self.file is not None:
            self.file.close()

        with open(path, 'rb') as opened_file:
            self.file = opened_file
