# coding: utf-8
import os
from ctypes import cdll, c_char_p, c_float, c_int

from PyQt5.QtCore import pyqtSignal, QThread
'''
import inspect
import ctypes
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,
                                                     ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)
'''


class AES_C_Lib(object):
    def __init__(self):
        work_path = os.getcwd()
        self.libc = cdll.LoadLibrary(os.path.join(work_path, "aes.so"))

    def encrypt(self, b_data):
        assert isinstance(b_data, bytes), \
            "TYPE ERROR at AES_C_Lib.encrypt"
        d_len = len(b_data)
        b_out = bytes(208)
        self.libc.encrypt_cbc(c_char_p(b_out), c_char_p(b_data), d_len)
        print('[DEBUG] encrypt len is ' + str(d_len))
        return b_out

    def decrypt(self, b_data):
        assert isinstance(b_data, bytes), \
            "TYPE ERROR at AES_C_Lib.encrypt"
        d_len = len(b_data)
        b_out = bytes(208)
        self.libc.decrypt_cbc(c_char_p(b_out), c_char_p(b_data), d_len)
        print('[DEBUG] decrypt len is ' + str(d_len))
        return b_out


class Call_C_Lib_Task(QThread):
    file_send_ok = pyqtSignal(int)  # 成功发送文件的信号

    def __init__(self, path, port, file_no, d_time, b_num, timeout):
        super().__init__()
        self.path = path
        self.port = port
        self.file_no = file_no
        self.d_time = d_time
        self.b_num = b_num
        self.timeout = timeout
        self.libc = None

    def run(self):
        work_path = os.getcwd()
        self.libc = cdll.LoadLibrary(os.path.join(work_path, "upload_lib.so"))
        try:
            # 设置函数返回值类型
            self.libc.lib_entry.restype = c_int
            self.libc.process.restype = c_float
            res = self.libc.lib_entry(
                c_char_p(bytes(self.path, 'utf8')), self.port, self.file_no,
                self.d_time, self.timeout, self.b_num)
            self.file_send_ok.emit(res)

        except Exception as e:
            print(e)


# def call_c_senderlib(path, port, file_no):
#     work_path = os.getcwd()
#     libc = cdll.LoadLibrary(os.path.join(work_path, "testlib.so"))
#     libc.lib_entry(c_char_p(bytes(path, 'utf8')), port, file_no)

if __name__ == "__main__":
    libc = cdll.LoadLibrary("/home/bg2dgr/code/C/upload/testlib.so")
    libc.lib_entry(
        c_char_p(bytes("/home/bg2dgr/Downloads/rec.zip", 'utf8')), 1500, 20,
        50000)
