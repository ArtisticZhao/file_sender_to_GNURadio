# coding: utf-8
import os
import threading
from ctypes import cdll, c_char_p
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


class Call_C_Lib_Task(threading.Thread):
    def __init__(self, path, port, file_no):
        super().__init__()
        self.path = path
        self.port = port
        self.file_no = file_no
        self.libc = None

    def run(self):
        work_path = os.getcwd()
        self.libc = cdll.LoadLibrary(os.path.join(work_path, "senderlib.so"))
        try:
            self.libc.lib_entry(
                c_char_p(bytes(self.path, 'utf8')), self.port, self.file_no)
        except Exception as e:
            print(e)


# def call_c_senderlib(path, port, file_no):
#     work_path = os.getcwd()
#     libc = cdll.LoadLibrary(os.path.join(work_path, "testlib.so"))
#     libc.lib_entry(c_char_p(bytes(path, 'utf8')), port, file_no)

if __name__ == "__main__":
    libc = cdll.LoadLibrary("/home/bg2dgr/code/C/upload/testlib.so")
    libc.lib_entry(
        c_char_p(bytes("/home/bg2dgr/Downloads/rec.zip", 'utf8')), 1500, 20)