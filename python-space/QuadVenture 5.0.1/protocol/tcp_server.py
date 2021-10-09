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
        #receive_data_all = bytearray()
        # print('asdsa')
        while True:
            receive_data = client_socket.recv(self.BUFFSIZE)
            # print('接收', receive_data.hex())
            # receive_data_all = receive_data_all+receive_data
            # length = int.from_bytes(receive_data_all[2:4], byteorder='big')
            # while length >
            # # if not receive_data:
            # #     break
            # # receive_data_all = receive_data_all + receive_data
            #
            # # print(receive_data_all.hex())
            # # length = int.from_bytes(self.receive_data[2:4], byteorder='big')
            # # # print(length)
            # command_code = receive_data[1:2]
            # # # # # # # print(command_code.hex())
            # command_code = int.from_bytes(command_code, byteorder='big')
            # if command_code == protocol.DATA_REQUEST_AND_RESPONSE.MS_DATA_FIRST[0]:
            #     receive_data_all = receive_data_all + receive_data
            #     receive_data = client_socket.recv(self.BUFFSIZE)
            #     receive_data_all = receive_data_all + receive_data
            #     if len(receive_data) < int(self.count / 3) + 7:
            #         receive_data_all = receive_data_all + receive_data
            # #
            # # #     length = int.from_bytes(self.receive_data[2:4], byteorder='big')
            # # #     if length + 7 == len(self.receive_data):
            # # #         pass
            # # #     else:
            # # #         continue
            # # #
            # elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.MS_DATA_THIRD[0]:
            #     if len(receive_data) < self.count - int(self.count / 3) - int(self.count / 3) + 7:
            #         receive_data_all = receive_data_all + receive_data
            # # #     length = int.from_bytes(self.receive_data[2:4], byteorder='big')
            # # #     print(self.receive_data.hex())
            # # #     print("第三节", length, len(self.receive_data))
            # # #     if length + 7 == len(self.receive_data):
            # # #         print('>>>>>>>>>>>>')
            # # #
            # # #     else:
            # # #         continue
            # elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.MS_DATA_SECOND[0]:
            #     if len(receive_data) < int(self.count / 3) + 7:
            #         receive_data_all = receive_data_all + receive_data
            # #     length = int.from_bytes(self.receive_data[2:4], byteorder='big')
            # #     if length + 7 == len(self.receive_data):
            # #         pass
            # #     else:
            # #         continue
            # else:
            #     receive_data_all

            # receive_data.clear()
            # self.y.append(
            #     int.from_bytes(receive_data[4 + i:5 + i], byteorder='big') for i in range(len(receive_data) - 3))
            # self.figure = plt.figure()
            # self.canvas = FigureCanvas(self.figure)
            # ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8])
            # ax.clear()  # 每次绘制一个函数时清空绘图
            # self.x = np.linspace(0, 5 * np.pi, 400)
            # self.y = np.sin(self.x)
            # ax.plot(self.x, self.y)
            # self.canvas.draw()
            # print(receive_data.hex())

            # print(receive_data.hex())
            # print('-------------------------------------------------------------')
            print(receive_data.hex())
            # self.just_receive_data(receive_data)

            self.listen_signal.emit(receive_data)
            # receive_data_all.clear()

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
