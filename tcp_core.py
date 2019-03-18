# coding:utf-8
from socketserver import BaseRequestHandler, ThreadingTCPServer
import socket
import threading
import time

from KISS import KISS_Decoder, KISS_Encoder_One_Frame

client_socket = []
shutdown_flag = [False]  # TODO may cause some errors!!! Where stop server!

socketer_dict = dict()


class HCR_Handler(BaseRequestHandler):
    def setup(self):
        client_socket.append(self.request)  # 保存套接字socket
        self.kiss_encoder = KISS_Encoder_One_Frame()

    def handle(self):
        print('[HCR] Got connection from', self.client_address, end=' \n')
        close = 0
        socketer_dict['to_HCR'] = self.request
        while not close and not shutdown_flag[0]:
            msg = self.request.recv(8192)
            if not msg:
                break
            if b'bye' in msg:
                close = 1
            # encode KISS
            msg = self.kiss_encoder.encode(msg)
            # self.request.send("receive success\n".encode('utf-8'))
            # 转发
            socketer_dict['to_GRC'].send(msg)

    def finish(self):
        print("client is disconnect!")
        client_socket.remove(self.request)


class GRC_Handler(BaseRequestHandler):
    def setup(self):
        client_socket.append(self.request)  # 保存套接字socket
        self.kiss_decoder = KISS_Decoder()

    def handle(self):
        print('[GRC] Got connection from', self.client_address, end=' \n')
        close = 0
        socketer_dict['to_GRC'] = self.request
        while not close and not shutdown_flag[0]:
            msg = self.request.recv(8192)
            if not msg:
                break
            if b'bye' in msg:
                close = 1
            # decode KISS
            msg = self.kiss_decoder.AppendStream(msg)

            # self.request.send("receive success\n".encode('utf-8'))
            # 转发
            socketer_dict['to_HCR'].send(msg)

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
            self.serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                                        True)
        elif self.mode == 'hcr':
            self.serv = ThreadingTCPServer(
                ('', self.port), HCR_Handler, bind_and_activate=False)
            self.serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                                        True)
        else:
            print("error")
            return
        # Bind and activate
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
