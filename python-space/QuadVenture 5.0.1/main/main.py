import sys
import threading

import matplotlib
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QHBoxLayout, QTreeView, QGridLayout

import content_frame.ms_content as mc
import plugs.qt_ungrade.ControlFactory as ControlFactory
import protocol.protocol_info as protocol
from plugs.qt_ungrade.SizeDockWidget import SizeDockWidget
from protocol.tcp_server import tcp_server
from sub_widget.qualitative_settings import QualitativeSettingWindow
from sub_widget.quantitative_setting import QuantitativeSettingWindow
from utils.CommonHelper import CommonHelper

# import pyqtgraph as pg

matplotlib.use('Qt5Agg')

# import method.menu_method as method

params = [
    {'name': '离子聚焦透镜电压1', 'value': 0},
    {'name': '离子聚焦透镜电压2', 'value': 0},
    {'name': '离子聚焦透镜电压3', 'value': 0},
    {'name': '离子聚焦透镜电压4', 'value': 0},
    {'name': '灯丝电流', 'value': 0},
    {'name': 'BIAS电压', 'value': 0},
    {'name': '灯丝电压', 'value': 0},
    {'name': 'RF电流', 'value': 0},
    {'name': 'DC1电流', 'value': 0},
    {'name': 'DC2电流', 'value': 0},
    {'name': 'RF电压', 'value': 0},
    {'name': '电子倍增器EM', 'value': 0},
    {'name': '打拿极HED', 'value': 0},
    {'name': '偏转电压', 'value': 0},
    {'name': '真空度', 'value': 0},
    {'name': '离子源温度', 'value': 0},
    {'name': '四级杆温度', 'value': 0},
    {'name': '气质接口温度', 'value': 0},
    {'name': '分子泵转速', 'value': 0},
    {'name': '分子泵电流', 'value': 0},
    {'name': '分子泵电压', 'value': 0},
    {'name': '分子泵温度', 'value': 0},
    {'name': '分子泵通讯状态', 'value': 0},
    {'name': '当前使用灯丝号', 'value': 0},
    {'name': 'HVDC', 'value': 0},
    {'name': '协议版本号', 'value': 0},
]


def show_installation_param(layout):
    index = 0
    for param in params:
        layout.addWidget(QtWidgets.QLabel(str(param['name'])), index, 0)
        layout.addWidget(QtWidgets.QLabel(str(param['value'])), index, 1)
        index = index + 1


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # menu_method_class = method.MenuMethod()

        self.qualitative_setting_window = QualitativeSettingWindow()
        self.quantitative_setting_window = QuantitativeSettingWindow()
        # self.server = tcp_server()
        # t = threading.Thread(target=self.server.accept_client)
        # t.start()
        self.widget = QtWidgets.QWidget(self)
        # self.status_bar = QtWidgets.QStatusBar(self)
        self.statusBar().showMessage('准备就绪')
        self.statusBar().setStyleSheet("background:red")
        layout = QVBoxLayout()
        # self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        # self.tab_menu = QtWidgets.QTabWidget(self)

        self.server = tcp_server()
        t = threading.Thread(target=self.server.accept_client)
        t.start()
        layout.addWidget(self.setMenuUI())
        layout.addWidget(self.setContentUI())
        # layout.addWidget(self.status_bar)
        self.widget.setLayout(layout)

        self.ms_spectrogram_dock = None

        self.setCentralWidget(self.widget)
        self.setLayout(layout)
        self.setupUI()
        self.showMaximized()

        self.x = []
        self.y = []
#        self.pw = pg.PlotWidget()
 #       self.curve = self.pw.getPlotItem().plot(
#            pen=pg.mkPen('r', width=1)
 #       )


        # layout.addStretch(2)

    def setupUI(self):
        # self.status_bar.setObjectName("status_bar")
        # self.central_widget.setObjectName("central_widget")
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "QuadVenture 5"))

    def setMenuUI(self):
        """
            tab menu
        :rtype: object
        :return: menu
        """
        tab_menu = QtWidgets.QTabWidget(self)
        tab_menu.setFixedHeight(140)
        # tab_menu.move(10,10)
        tab_file = QtWidgets.QTabBar()  # 文件
        tab_2 = QtWidgets.QTabBar()  # second tab
        tab_installation = QtWidgets.QTabBar()  # 设备
        tab_acquisition = QtWidgets.QTabBar()  # 采集
        tab_5 = QtWidgets.QTabBar()  # fifth tab
        tab_method = QtWidgets.QTabBar()  # 方法
        # self_ta
        tab_menu.setObjectName("tab_menu")
        tab_file.setObjectName("tab_file")
        tab_menu.addTab(tab_file, "文件")

        tab_2.setObjectName("tab_2")
        tab_menu.addTab(tab_2, "视图")
        tab_installation.setObjectName("tab_installation")
        tab_menu.addTab(tab_installation, "设备")

        tab_method.setObjectName("tab_method")
        tab_menu.addTab(tab_method, "方法")
        tab_acquisition.setObjectName("tab_acquisition")
        tab_menu.addTab(tab_acquisition, "采集")
        tab_5.setObjectName("tab_5")
        tab_menu.addTab(tab_5, "帮助")

        control_factory = ControlFactory.ControlFactory()
        '''
        tabButton of tab_file
        '''
        tab_file_layout = QHBoxLayout()
        tab_file_layout.setAlignment(QtCore.Qt.AlignLeft)
        tab_file_layout.setContentsMargins(10, 0, 0, 5)

        tab_file_layout.addWidget(control_factory.create_function_area(
            {
                'title': '方法',
                'name': ['打开方法', '新建方法', '保存方法'],
                'icon': ['../resource/icon/file_open.png'],
                'function': [self.qualitative_setting, self.qualitative_setting, self.qualitative_setting]
            }

        ))
        tab_file.setLayout(tab_file_layout)

        '''
        toolButton of tab_acquisition
        '''
        tab_acquisition_layout = QHBoxLayout()
        tab_acquisition_layout.setAlignment(QtCore.Qt.AlignLeft)
        tab_acquisition_layout.setContentsMargins(10, 0, 0, 5)

        tab_acquisition_layout.addWidget(control_factory.create_function_area(
            {
                'title': '谱图',
                'name': ['质谱图', '色谱图', '放空阀'],
                'icon': ['../resource/icon/file_open.png'],
                'function': [self.ms_spectrogram_show, self.qualitative_setting, self.qualitative_setting]
            }

        ))
        tab_acquisition.setLayout(tab_acquisition_layout)
        """
        toolButtons of tab_installation_layout
        """

        tab_installation_layout = QHBoxLayout()
        tab_installation_layout.setAlignment(QtCore.Qt.AlignLeft)
        tab_installation_layout.setContentsMargins(10, 0, 0, 5)

        tab_installation_layout.addWidget(control_factory.create_function_area(
            {
                'title': '真空',
                'name': ['分子泵', '前期泵', '放空阀'],
                'icon': ['../resource/icon/file_open.png'],
                'function': [self.qualitative_setting, self.qualitative_setting, self.qualitative_setting]
            }

        ))
        tab_installation.setLayout(tab_installation_layout)
        '''
        toolButton of tab_method
        '''
        tab_method_layout = QHBoxLayout()
        tab_method_layout.setAlignment(QtCore.Qt.AlignLeft)
        tab_method_layout.setContentsMargins(10, 0, 0, 5)

        tab_method_layout.addWidget(control_factory.create_function_area(
            {
                'title': '参数',
                'name': ['仪器参数', '定性参数', '定量参数'],
                'icon': ['../resource/icon/instrument.png'],
                'function': [self.instrument_param_show, self.qualitative_setting, self.quantitative_setting]

            }

        ))
        tab_method.setLayout(tab_method_layout)

        return tab_menu

    def setContentUI(self) -> object:
        """

        :rtype: object
        """
        # self.server = server
        parent_frame_layout = QHBoxLayout()
        parent_frame_layout.setContentsMargins(0, 0, 0, 0)
        parent_frame_layout.setSpacing(0)
        self.parent_frame = QWidget(self)
        # parent_frame.setWindowFlags(QtCore.Qt.Widget)
        self.parent_frame.setLayout(parent_frame_layout)

        status_frame = QMainWindow(self.parent_frame)
        status_frame.setFixedWidth(15)
        status_frame.setWindowFlags(QtCore.Qt.Widget)
        status_frame.setObjectName("status_frame")
        self.content_frame = QMainWindow(self.parent_frame)
        self.content_frame.setWindowFlags(QtCore.Qt.Widget)

        self.left_dock = QtWidgets.QDockWidget(self.content_frame)
        left_dock_layout = QVBoxLayout()
        left_dock_layout.setSpacing(0)
        left_dock_layout.setContentsMargins(0, 0, 0, 0)
        tree_view = QTreeView(self.left_dock)
        left_dock_layout.addWidget(tree_view)
        al_widget = QWidget()
        al_widget.setLayout(left_dock_layout)
        self.left_dock.setWidget(al_widget)

        self.right_dock = QtWidgets.QDockWidget(self.content_frame)

        self.right_dock.setObjectName("right_dock_widget")
        right_dock_layout = QVBoxLayout()
        right_dock_layout.setSpacing(0)
        right_dock_layout.setAlignment(QtCore.Qt.AlignTop)
        right_dock_layout.setContentsMargins(0, 4, 1, 0)
        right_dock_content_widget = SizeDockWidget()
        right_dock_content_widget.setObjectName("right_dock_content_widget")
        right_dock_content_widget.setLayout(right_dock_layout)

        self.right_dock.setWidget(right_dock_content_widget)

        right_tab_widget_content = QtWidgets.QTabWidget(right_dock_content_widget)
        right_tab_widget_content.setObjectName("MS")
        # right_tab_widget_content.setFixedHeight(500)

        tab_gc = QtWidgets.QTabBar()  # first tab
        tab_gc.setStyleSheet("QTabBar{ background-color:#F0FFFF;}")

        tab_ms = QtWidgets.QTabBar()  # first tab
        tab_ms.setStyleSheet("QTabBar{ background-color:#F0FFFF;}")


        tab_ms_picture = QtWidgets.QTabBar()
        tab_ms_picture.setStyleSheet("QTabBar{ background-color:#F0FFFF;}")

        right_tab_widget_content.addTab(tab_gc, "GC")
        right_tab_widget_content.addTab(tab_ms, "MS")
        #right_tab_widget_content.addTab(tab_ms_picture, "质谱图")

        tab_layout = QVBoxLayout()
        ms_content = mc.MsContent(tab_ms)
        ms_content.set_server(self.server)

        self.server.listen_signal.connect(self.show_listen_data)
        tab_layout.addWidget(ms_content.frame)
        # tab_layout.setAlignment(QtCore.Qt.AlignTop)
        tab_ms.setLayout(tab_layout)

        right_dock_layout.addWidget(right_tab_widget_content)
        # button_param_setting = QtWidgets.QPushButton(right_dock_content_widget)
        # button_param_setting.setText("设置")

        # button_execute = QtWidgets.QPushButton(right_dock_content_widget)
        # button_execute.setText("执行")
        # button_layout = QHBoxLayout()
        # button_layout.addWidget(button_param_setting)
        # button_layout.addWidget(button_execute)

        # button_widget = QtWidgets.QWidget()
        # button_widget.setLayout(button_layout)
        # button_widget.setFixedHeight(100)
        # right_dock_layout.addWidget(button_param_setting)
        # right_dock_layout.addWidget(button_execute)

        # central_widget = QtWidgets.QWidget(content_frame)
        self.installation_param_dock = QtWidgets.QDockWidget(self.content_frame)
        self.installation_param_dock.setFixedWidth(200)
        self.param_content = QtWidgets.QWidget()
        self.installation_param_dock.setWidget(self.param_content)

        self.param_content_layout = QGridLayout()
        self.param_content.setLayout(self.param_content_layout)
        show_installation_param(self.param_content_layout)
        self.content_frame.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.left_dock)
        self.content_frame.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.right_dock)
        self.content_frame.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.installation_param_dock)
        self.content_frame.splitDockWidget(self.right_dock, self.installation_param_dock, QtCore.Qt.Horizontal)
        widget = QtWidgets.QWidget(self.content_frame)
        widget.setObjectName("content_mid_widget")
        widget.setFixedSize(0, 0)
        self.content_frame.setCentralWidget(widget)
        self.content_frame.setContentsMargins(0, 0, 0, 0)

        # parent_frame_layout.addWidget(status_frame)
        parent_frame_layout.addWidget(self.content_frame)
        return self.parent_frame

    def qualitative_setting(self):
        self.qualitative_setting_window.show()

    def quantitative_setting(self):
        self.quantitative_setting_window.show()

    def ms_spectrogram_show(self):
        self.right_dock.hide()
        # print(type(self.ms_spectrogram_dock))
        if self.ms_spectrogram_dock is None:
            self.ms_spectrogram_dock = QtWidgets.QDockWidget(self.content_frame)
            ms_spectrogram_dock_content_widget = SizeDockWidget()
            self.ms_spectrogram_dock.setWidget(ms_spectrogram_dock_content_widget)
            ms_spectrogram_widget_layout = QHBoxLayout()
            ms_spectrogram_widget_layout.setContentsMargins(0, 0, 0, 0)
            ms_spectrogram_dock_content_widget.setLayout(ms_spectrogram_widget_layout)
            self.content_frame.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.ms_spectrogram_dock)
            self.content_frame.splitDockWidget(self.ms_spectrogram_dock, self.installation_param_dock,
                                               QtCore.Qt.Horizontal)
            self.figure = plt.figure()
            plt.plot(self.y)
            plt.show()
           #  self.canvas = FigureCanvas(self.figure)
            # ms_spectrogram_widget_layout.addWidget(self.canvas)
            # self.plot_()
        else:
            self.ms_spectrogram_dock.show()
            self.content_frame.splitDockWidget(self.ms_spectrogram_dock, self.installation_param_dock,
                                               QtCore.Qt.Horizontal)

    def instrument_param_show(self):
        self.ms_spectrogram_dock.hide()
        self.content_frame.splitDockWidget(self.right_dock, self.installation_param_dock, QtCore.Qt.Horizontal)
        self.right_dock.show()

    def plot_(self):
        ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.clear()  # 每次绘制一个函数时清空绘图

        ax.plot(self.y)
        self.canvas.draw()

    def show_listen_data(self, data):
        # print(data.hex(),'asdassadsad')
        # print('接收',data)
        command_code = data[1:2]
        # print(command_code.hex())
        command_code = int.from_bytes(command_code, byteorder='big')
        # print(command_code)
        if command_code == protocol.DATA_REQUEST_AND_RESPONSE.RF_PARAM_SET[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)

        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.DC_ONE_PARAM_SET[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.DC_TWO_PARAM_SET[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.OTHER_PARAM_SET[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.TEMPERATURE_SET[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.EXPERIENCE_START_TIME_SET[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.RF_SWITCH[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.FILAMENT_SWITCH[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.HV_HIGH_VOLTAGE_SWITCH[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.EXPERIMENT_SWITCH[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.STANDARD_LIQUID_VALVE_SWITCH[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.VENT_VALVE_SWITCH[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.TEMPERATURE_SWITCH[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.FILAMENT_SELECT[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.HVDC_SWITCH[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.DATA_QUERY[0]:

            params[0]['value'] = 50-100*(int.from_bytes(data[8:10],byteorder='big') *2.5/65535)
            params[1]['value'] = 50-100*(int.from_bytes(data[10:12],byteorder='big') *2.5/65535)
            params[2]['value'] = 50-100*(int.from_bytes(data[4:6],byteorder='big') *2.5/65535)
            params[3]['value'] = 50-100*(int.from_bytes(data[6:8],byteorder='big') *2.5/65535)
            params[4]['value'] = 1000*(int.from_bytes(data[12:14],byteorder='big') *2.5/65535-130)/13.2/0.375
            params[5]['value'] =  50-100*(int.from_bytes(data[14:16],byteorder='big') *2.5/65535)
            params[6]['value'] =  100*(int.from_bytes(data[16:18],byteorder='big') *2.5/65535)
            params[7]['value'] =  (int.from_bytes(data[18:20],byteorder='big') *3.3/65535)/1.33
            params[8]['value'] =  -200*(int.from_bytes(data[20:22],byteorder='big') *3.3/65535)
            params[9]['value'] =  200*(int.from_bytes(data[22:24],byteorder='big') *3.3/65535)
            params[10]['value'] =  1000*(int.from_bytes(data[24:26],byteorder='big') *3.3/65535)
            params[11]['value'] =  -400*(int.from_bytes(data[26:28],byteorder='big') *3.3/4096)*2
            params[12]['value'] =  -2000*(int.from_bytes(data[28:30],byteorder='big') *3.3/4096)*2
            params[13]['value'] =  -400*(int.from_bytes(data[30:32],byteorder='big') *3.3/4096)*2
            params[14]['value'] =  ((int.from_bytes(data[32:34],byteorder='big') *3.3/4096)/2*11)
            params[15]['value'] =  (int.from_bytes(data[34:36],byteorder='big'))/10
            params[16]['value'] =  (int.from_bytes(data[36:38],byteorder='big'))/10
            params[17]['value'] =  (int.from_bytes(data[38:40],byteorder='big'))/10
            params[18]['value'] =  (int.from_bytes(data[40:43],byteorder='big'))
            params[19]['value'] =  (int.from_bytes(data[43:45],byteorder='big'))/100
            params[20]['value'] =  (int.from_bytes(data[45:47],byteorder='big'))/100
            params[21]['value'] =  (int.from_bytes(data[47:49],byteorder='big'))
            params[22]['value'] =  (int.from_bytes(data[49:50],byteorder='big'))
            params[23]['value'] =  (int.from_bytes(data[50:51],byteorder='big'))
            params[24]['value'] =  (int.from_bytes(data[51:52],byteorder='big'))
            params[25]['value'] =  (int.from_bytes(data[52:53],byteorder='big'))/10


            # data = data[4:]
            # for item in range(18):
            #     if item == 14:
            #         params[item]['value'] = int.from_bytes(data[2 * item:2 * item + 2],
            #                                                byteorder='big') / 4096 * 3.3 * 11 / 2
            #     else:
            #         params[item]['value'] = int.from_bytes(data[2 * item:2 * item + 2], byteorder='big')
            # params[18]['value'] = int.from_bytes(data[36:39], byteorder='big')
            # for item in range(0, 3):
            #     params[item]['value'] = int.from_bytes(data[39 + 2 * item:39 + 2 * item + 2], byteorder='big')
            # for item in range(0, 4):
            #     params[item]['value'] = int.from_bytes(data[45 + item:45 + item + 1], byteorder='big')
            # print(params)

            # self.param_content.setLayout(None)

            index = 0
            for param in params:
                # self.param_content_layout.get
                self.param_content_layout.removeWidget(self.param_content_layout.itemAtPosition(index, 1).widget())
                # self.param_content_layout.addWidget(QtWidgets.QLabel('' + str(param['name']) + ''), index, 0)
                self.param_content_layout.addWidget(QtWidgets.QLabel('' + str(param['value']) + ''), index, 1)
                index = index + 1
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.MOLECULAR_PUMP_SWITCH[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            message = int.from_bytes(data[4:4 + length], byteorder='big')
            if message == protocol.STATUS.SUCCESS:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置成功")
                # msg_box.
                print(msg_box)
            else:
                msg_box = QtWidgets.QMessageBox.about(self, "提示", "设置失败")
                # msg_box.exec_()
                print(msg_box)
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.MS_DATA_FIRST[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            # self.y.append(data[4 + i:5 + i] for i in range(len(data) - 3))
            #print("第一段",length)
            #for i in range(len(data)):
                # self.x.append(i)
                # self.y.append(data[i])
            # self.ms_spectrogram_show()
            # self.y.clear()
            # plt.plot(self.x,self.y)
            # plt.show()
            # self.x.clear()
            # self.y.clear()
            # self.canvas.draw()


        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.MS_DATA_SECOND[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            # self.y.append(data[4 + i:5 + i] for i in range(len(data) - 3))
            #print("第二段" , length)
            # self.y.append(int.from_bytes(data[4+i:5+i], byteorder='big') for i in range(len(data)-3))
        elif command_code == protocol.DATA_REQUEST_AND_RESPONSE.MS_DATA_THIRD[0]:
            length = int.from_bytes(data[2:4], byteorder='big')
            # self.y.append(data[4 + i:5 + i] for i in range(len(data) - 3))
            # t = threading.Thread(target=self.data_show, args=(data,))  # t为新创建的线程
            # t.start()
            # if len(data)>0:
            #     pg.plot(data)


            # 创建 PlotWidget 对象
            # self.pw = pg.PlotWidget()
            #
            # # 设置图表标题
            # self.pw.setTitle("质谱图",
            #                  color='008080',
            #                  size='12pt')
            #
            # self.i += 1
            # self.x.append(self.i)
            # # 创建随机温度值
            # # self.y.append(randint(10, 30))
            # self.y.append(data[4 + i:5 + i] for i in range(len(data) - 3))
            #
            # # plot data: x, y values
            # self.curve.setData(data)
            # self.x.clear()
            # self.y.clear()
            #print("第三段" , length)
            # print(len(data))
            # self.y.append(int.from_bytes(data[4 + i:5 + i], byteorder='big') for i in range(len(data) - 3))
            #self.y.append(int.from_bytes(data[4 + 2 * i:4 + 2 * i + 2], byteorder='big') for i in range((length-49) / 2))
            # self.ms_spectrogram_show()
            # print(len(self.y))
            #print(self.y)
            # self.y.clear()


    def data_show(self,data):

        pg.plot(data)









if __name__ == '__main__':
    app = QApplication(sys.argv)  # 初始化app

    mainWindow = MainWindow()  # 创建UI界面
    styleFile = '../qss/main.qss'
    qssStyle = CommonHelper.readQss(styleFile)
    mainWindow.setStyleSheet(qssStyle)
    mainWindow.show()
    sys.exit(app.exec_())  # 消息循环结束之后返回0，接着调用sys.exit(0)退出程序
