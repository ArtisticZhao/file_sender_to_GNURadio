# coding:utf-8
from socketserver import BaseRequestHandler, TCPServer
import socket
import threading
import time

client_socket = []
shutdown_flag = [False]


class SeverHandler(BaseRequestHandler):
    def setup(self):
        client_socket.append(self.request)  # 保存套接字socket

    def handle(self):
        print('Got connection from', self.client_address, end=' \n')
        close = 0
        while not close and not shutdown_flag[0]:
            msg = self.request.recv(8192)
            print("[message]", end=' ')
            print(msg)
            if not msg:
                break
            if b'bye' in msg:
                close = 1
            self.request.send("receive success\n".encode('utf-8'))

    def finish(self):
        print("client is disconnect!")
        client_socket.remove(self.request)


class tcp_server(threading.Thread):
    def __init__(self, port):
        super().__init__()
        self.serv = None
        self.port = port

    def run(self):
        self.serv = TCPServer(
            ('', self.port), SeverHandler, bind_and_activate=False)
        self.serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                                    True)
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
