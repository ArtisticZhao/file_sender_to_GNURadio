# coding:utf-8
from socketserver import BaseRequestHandler, ThreadingTCPServer
import socket
import threading
import time

from KISS import KISS_Decoder, KISS_Encoder_One_Frame
from KISS import KISS_encode_queue, KISS_frame

client_socket = []
shutdown_flag = [False]  # TODO may cause some errors!!! Where stop server!

socketer_dict = dict()
'''
流程说明:
如果给GNU Radio发消息(消息源可能是"HCR"或者是"软件前面板"), 需要加入打帧器队列当中,
GRC_Handler的send函数必须由打帧器触发
'''


class HCR_Handler(BaseRequestHandler):
    '''
    监听胡学姐
    '''

    def setup(self):
        # 这个timeout的设置非常有必要, 能够解决不能退出线程的问题
        self.request.settimeout(1)
        client_socket.append(self.request)  # 保存套接字socket
        self.kiss_encoder = KISS_Encoder_One_Frame()

    def handle(self):
        print('[HCR] Got connection from', self.client_address, end=' \n')
        socketer_dict['to_HCR'] = self.request
        while not shutdown_flag[0]:
            try:
                msg = self.request.recv(8192)
            except socket.timeout:
                continue
            if not msg:
                break
            # encode KISS
            # msg = self.kiss_encoder.encode(msg)
            # self.request.send("receive success\n".encode('utf-8'))
            # 通知打帧器
            for each in msg:
                KISS_encode_queue.put(each)
            # socketer_dict['to_GRC'].send(msg)

    def finish(self):
        print("client is disconnect!")
        client_socket.remove(self.request)


class GRC_Handler(BaseRequestHandler):
    '''
    监听GNU Radio
    '''

    def setup(self):
        # 这个timeout的设置非常有必要, 能够解决不能退出线程的问题
        self.request.settimeout(1)
        client_socket.append(self.request)  # 保存套接字socket
        self.kiss_decoder = KISS_Decoder()

        # 打帧器
        self.KISS_frame = KISS_frame()
        self.KISS_frame.set_sender(self.request)
        self.KISS_frame.start()

    def handle(self):
        print('[GRC] Got connection from', self.client_address, end=' \n')

        socketer_dict['to_GRC'] = self.request
        while not shutdown_flag[0]:
            try:
                msg = self.request.recv(8192)
            except socket.timeout:
                continue
            if not msg:
                break
            # decode KISS
            smsg = self.kiss_decoder.AppendStream(msg)
            # print(smsg)
            # self.request.send("receive success\n".encode('utf-8'))
            # 转发给HCR
            if smsg is not None:
                socketer_dict['to_HCR'].send(smsg)
        # 结束打帧器线程
        self.KISS_frame.shutdown()

    def finish(self):
        print("client is disconnect!")
        client_socket.remove(self.request)


class tcp_server(threading.Thread):
    def __init__(self, port, mode):  # mode = 'grc' or 'hcr'
        super().__init__()
        self.serv = None
        self.port = port
        self.mode = mode

    def run(self):
        if self.mode == 'grc':
            self.serv = ThreadingTCPServer(
                ('', self.port), GRC_Handler, bind_and_activate=False)
            self.serv.socket.settimeout(0.1)  # 设置超时, 以便能够退出线程
            self.serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                                        True)  # 设置端口重用, 以便异常socket断开后的重建

        elif self.mode == 'hcr':
            self.serv = ThreadingTCPServer(
                ('', self.port), HCR_Handler, bind_and_activate=False)
            self.serv.socket.settimeout(0.1)  # 设置超时, 以便能够退出线程
            self.serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                                        True)  # 设置端口重用, 以便异常socket断开后的重建

        else:
            print("error")
            return
        # Bind and activate
        self.setName("tcp_server " + self.mode)
        self.serv.server_bind()
        self.serv.server_activate()
        self.serv.serve_forever()

    def send_data(self, data):
        '''
            Args:
                data: bytes data
        '''
        if self.is_alive():
            for client in client_socket:
                client.sendall(data)

    def shutdown(self):
        for client in client_socket:
            client.shutdown(1)
        shutdown_flag[0] = True
        self.serv.socket.close()
        self.serv.shutdown()
        self.serv.server_close()


if __name__ == '__main__':
    ser = tcp_server(20000)
    ser.start()
    print("listening")
    time.sleep(10)
    print("sending")
    ser.send_data("test sending".encode('utf-8'))
    # print("shuting")
    # ser.serv.shutdown()
