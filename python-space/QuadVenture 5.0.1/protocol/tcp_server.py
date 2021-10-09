import threading
from socket import *

import PyQt5.QtCore as poc

import protocol.protocol_info as protocol


class tcp_server(poc.QObject):
    listen_signal = poc.pyqtSignal(bytes)

    def __init__(self):

        super().__init__()
        self.address = '192.168.0.116'  # 监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
        self.port = 5000  # 监听自己的哪个端口
        self.BUFFSIZE = 1024 * 1024 * 1024 * 3  # 接收从客户端发来的数据的缓存区大小
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((self.address, self.port))
        self.socket.listen(2)  # 最大连接数
        self.client_socket = None
        self.y = []

        # self.scan_time = 0
        # self.scan_frequency = 0
        self.count = 0

    def action_response(self, message):
        print(message)

    def default(self, message):
        print('啥也不是')

    def matching_dict(self, code, message):
        print(protocol.DATA_REQUEST_AND_RESPONSE.RF_PARAM_SET[0])
        types = {
            protocol.DATA_REQUEST_AND_RESPONSE.RF_PARAM_SET: self.action_response,
        }
        method = types.get(code, self.default)
        return method()

    def tcp_link(self, client_socket, address):
        receive_data_all = bytes()
        # print('asdsa')
        while True:
            # while True:
            receive_data = client_socket.recv(self.BUFFSIZE)
            receive_data_all = receive_data_all+receive_data

            if receive_data.hex().endswith('aa'):
                print(receive_data_all.hex())
                self.listen_signal.emit(receive_data_all)
                receive_data_all = bytes()

        # socket.close()

    def accept_client(self):
        while True:
            self.client_socket, client_address = self.socket.accept()
            print('connect from:', client_address)
            # 传输数据都利用client_sock，和s无关
            t = threading.Thread(target=self.tcp_link, args=(self.client_socket, client_address))  # t为新创建的线程
            t.start()

    def just_receive_data(self, data):
        pass
