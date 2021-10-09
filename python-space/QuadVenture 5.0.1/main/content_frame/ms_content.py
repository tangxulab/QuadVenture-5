from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout, QMainWindow

import protocol.protocol_info as protocol


class MsContent(QMainWindow):
    def __init__(self, parent):
        super(MsContent, self).__init__(parent)
        self.frame = QtWidgets.QFrame()

        # self.frame.setFixedHeight(400)

        # thread = threading.Thread(target=self.server.accept_client)  # t为新创建的线程
        # thread.start()
        self.frame.setStyleSheet("QFrame{background:#FFFFFF}")
        frame_layout = QGridLayout()
        self.frame.setLayout(frame_layout)

        self.rf_setting_group = QtWidgets.QGroupBox(self.frame)
        self.rf_setting_group.setTitle("RF  参数设置")

        frame_layout.addWidget(self.rf_setting_group, 0, 0)

        rf_setting_group_layout = QGridLayout(self.rf_setting_group)
        self.rf_setting_group.setLayout(rf_setting_group_layout)
        self.rf_low_voltage_label = QtWidgets.QLabel(self.rf_setting_group)
        self.rf_low_voltage_label.setText("RF 低电压")
        self.rf_low_voltage_text = QtWidgets.QLineEdit(self.rf_setting_group)

        self.rf_high_voltage_label = QtWidgets.QLabel(self.rf_setting_group)
        self.rf_high_voltage_label.setText("RF 高电压")
        self.rf_high_voltage_text = QtWidgets.QLineEdit(self.rf_setting_group)
        self.rf_scan_time_label = QtWidgets.QLabel(self.rf_setting_group)
        self.rf_scan_time_label.setText("RF 扫描时间")
        self.rf_scan_time_text = QtWidgets.QLineEdit(self.rf_setting_group)
        self.rf_scan_frequency_label = QtWidgets.QLabel(self.rf_setting_group)
        self.rf_scan_frequency_label.setText("RF 扫描频率")
        self.rf_scan_frequency_text = QtWidgets.QLineEdit(self.rf_setting_group)
        self.btn_rf_setting = QtWidgets.QPushButton(self.rf_setting_group)
        self.btn_rf_setting.setText("下载")
        self.btn_rf_setting.clicked.connect(self.rf_setting_function)

        rf_setting_group_layout.addWidget(self.rf_low_voltage_label, 0, 0)
        rf_setting_group_layout.addWidget(self.rf_low_voltage_text, 0, 1)
        rf_setting_group_layout.addWidget(self.rf_high_voltage_label, 1, 0)
        rf_setting_group_layout.addWidget(self.rf_high_voltage_text, 1, 1)
        rf_setting_group_layout.addWidget(self.rf_scan_time_label, 2, 0)
        rf_setting_group_layout.addWidget(self.rf_scan_time_text, 2, 1)
        rf_setting_group_layout.addWidget(self.rf_scan_frequency_label, 3, 0)
        rf_setting_group_layout.addWidget(self.rf_scan_frequency_text, 3, 1)
        rf_setting_group_layout.addWidget(self.btn_rf_setting, 4, 0)

        self.dc_one_setting_group = QtWidgets.QGroupBox(self.frame)
        self.dc_one_setting_group.setTitle("DC1 设置 ")
        frame_layout.addWidget(self.dc_one_setting_group, 0, 1)

        dc_one_setting_group_layout = QGridLayout(self.dc_one_setting_group)
        self.dc_one_setting_group.setLayout(dc_one_setting_group_layout)
        self.dc_one_low_voltage_label = QtWidgets.QLabel(self.dc_one_setting_group)
        self.dc_one_low_voltage_label.setText("DC1 低电压")
        self.dc_one_low_voltage_text = QtWidgets.QLineEdit(self.dc_one_setting_group)

        self.dc_one_high_voltage_label = QtWidgets.QLabel(self.dc_one_setting_group)
        self.dc_one_high_voltage_label.setText("DC1 高电压")
        self.dc_one_high_voltage_text = QtWidgets.QLineEdit(self.dc_one_setting_group)
        self.dc_one_scan_time_label = QtWidgets.QLabel(self.dc_one_setting_group)
        self.dc_one_scan_time_label.setText("DC1 扫描时间")
        self.dc_one_scan_time_text = QtWidgets.QLineEdit(self.dc_one_setting_group)
        self.dc_one_scan_frequency_label = QtWidgets.QLabel(self.dc_one_setting_group)
        self.dc_one_scan_frequency_label.setText("DC1 扫描频率")
        self.dc_one_scan_frequency_text = QtWidgets.QLineEdit(self.dc_one_setting_group)
        self.btn_dc_one_setting = QtWidgets.QPushButton(self.dc_one_setting_group)
        self.btn_dc_one_setting.setText("下载")
        self.btn_dc_one_setting.clicked.connect(self.dc_one_setting_function)

        dc_one_setting_group_layout.addWidget(self.dc_one_low_voltage_label, 0, 0)
        dc_one_setting_group_layout.addWidget(self.dc_one_low_voltage_text, 0, 1)
        dc_one_setting_group_layout.addWidget(self.dc_one_high_voltage_label, 1, 0)
        dc_one_setting_group_layout.addWidget(self.dc_one_high_voltage_text, 1, 1)
        dc_one_setting_group_layout.addWidget(self.dc_one_scan_time_label, 2, 0)
        dc_one_setting_group_layout.addWidget(self.dc_one_scan_time_text, 2, 1)
        dc_one_setting_group_layout.addWidget(self.dc_one_scan_frequency_label, 3, 0)
        dc_one_setting_group_layout.addWidget(self.dc_one_scan_frequency_text, 3, 1)
        dc_one_setting_group_layout.addWidget(self.btn_dc_one_setting, 4, 0)

        self.dc_two_setting_group = QtWidgets.QGroupBox(self.frame)
        self.dc_two_setting_group.setTitle("DC2 设置 ")
        frame_layout.addWidget(self.dc_two_setting_group, 0, 2)

        dc_two_setting_group_layout = QGridLayout(self.dc_two_setting_group)
        self.dc_two_setting_group.setLayout(dc_two_setting_group_layout)
        self.dc_two_low_voltage_label = QtWidgets.QLabel(self.dc_two_setting_group)
        self.dc_two_low_voltage_label.setText("DC2 低电压")
        self.dc_two_low_voltage_text = QtWidgets.QLineEdit(self.dc_two_setting_group)

        self.dc_two_high_voltage_label = QtWidgets.QLabel(self.dc_two_setting_group)
        self.dc_two_high_voltage_label.setText("DC2 高电压")
        self.dc_two_high_voltage_text = QtWidgets.QLineEdit(self.dc_two_setting_group)
        self.dc_two_scan_time_label = QtWidgets.QLabel(self.dc_two_setting_group)
        self.dc_two_scan_time_label.setText("DC2 扫描时间")
        self.dc_two_scan_time_text = QtWidgets.QLineEdit(self.dc_two_setting_group)
        self.dc_two_scan_frequency_label = QtWidgets.QLabel(self.dc_two_setting_group)
        self.dc_two_scan_frequency_label.setText("DC2 扫描频率")
        self.dc_two_scan_frequency_text = QtWidgets.QLineEdit(self.dc_two_setting_group)
        self.btn_dc_two_setting = QtWidgets.QPushButton(self.dc_two_setting_group)
        self.btn_dc_two_setting.setText("下载")
        self.btn_dc_two_setting.clicked.connect(self.dc_two_setting_function)

        dc_two_setting_group_layout.addWidget(self.dc_two_low_voltage_label, 0, 0)
        dc_two_setting_group_layout.addWidget(self.dc_two_low_voltage_text, 0, 1)
        dc_two_setting_group_layout.addWidget(self.dc_two_high_voltage_label, 1, 0)
        dc_two_setting_group_layout.addWidget(self.dc_two_high_voltage_text, 1, 1)
        dc_two_setting_group_layout.addWidget(self.dc_two_scan_time_label, 2, 0)
        dc_two_setting_group_layout.addWidget(self.dc_two_scan_time_text, 2, 1)
        dc_two_setting_group_layout.addWidget(self.dc_two_scan_frequency_label, 3, 0)
        dc_two_setting_group_layout.addWidget(self.dc_two_scan_frequency_text, 3, 1)
        dc_two_setting_group_layout.addWidget(self.btn_dc_two_setting, 4, 0)

        self.voltage_setting_group = QtWidgets.QGroupBox(self.frame)
        self.voltage_setting_group.setTitle("电压设定")

        frame_layout.addWidget(self.voltage_setting_group, 1, 0)
        voltage_setting_group_layout = QGridLayout(self.voltage_setting_group)
        self.voltage_setting_group.setLayout(voltage_setting_group_layout)
        self.focus_lens_one_voltage_label = QtWidgets.QLabel(self.voltage_setting_group)
        self.focus_lens_one_voltage_label.setText("聚焦透镜1")
        self.focus_lens_one_voltage_text = QtWidgets.QLineEdit(self.voltage_setting_group)
        self.focus_lens_two_voltage_label = QtWidgets.QLabel(self.voltage_setting_group)
        self.focus_lens_two_voltage_label.setText("聚焦透镜2")
        self.focus_lens_two_voltage_text = QtWidgets.QLineEdit(self.voltage_setting_group)
        self.focus_lens_three_voltage_label = QtWidgets.QLabel(self.voltage_setting_group)
        self.focus_lens_three_voltage_label.setText("聚焦透镜3")
        self.focus_lens_three_voltage_text = QtWidgets.QLineEdit(self.voltage_setting_group)
        self.focus_lens_four_voltage_label = QtWidgets.QLabel(self.voltage_setting_group)
        self.focus_lens_four_voltage_label.setText("聚焦透镜4")
        self.focus_lens_four_voltage_text = QtWidgets.QLineEdit(self.voltage_setting_group)
        self.filament_voltage_label = QtWidgets.QLabel(self.voltage_setting_group)
        self.filament_voltage_label.setText("灯丝电压")
        self.filament_voltage_text = QtWidgets.QLineEdit(self.voltage_setting_group)

        self.filament_current_label = QtWidgets.QLabel(self.voltage_setting_group)
        self.filament_current_label.setText("灯丝电流")
        self.filament_current_text = QtWidgets.QLineEdit(self.voltage_setting_group)

        self.bias_voltage_label = QtWidgets.QLabel(self.voltage_setting_group)
        self.bias_voltage_label.setText("BIAS")
        self.bias_voltage_text = QtWidgets.QLineEdit(self.voltage_setting_group)

        self.dynamo_voltage_label = QtWidgets.QLabel(self.voltage_setting_group)
        self.dynamo_voltage_label.setText("打拿极电压")
        self.dynamo_voltage_text = QtWidgets.QLineEdit(self.voltage_setting_group)

        self.multiplier_voltage_label = QtWidgets.QLabel(self.voltage_setting_group)
        self.multiplier_voltage_label.setText("倍增器电压")
        self.multiplier_voltage_text = QtWidgets.QLineEdit(self.voltage_setting_group)

        self.deflection_voltage_label = QtWidgets.QLabel(self.voltage_setting_group)
        self.deflection_voltage_label.setText("偏转电压")
        self.deflection_voltage_text = QtWidgets.QLineEdit(self.voltage_setting_group)

        self.btn_voltage_setting = QtWidgets.QPushButton(self.voltage_setting_group)
        self.btn_voltage_setting.setText("下载")
        self.btn_voltage_setting.clicked.connect(self.voltage_setting_function)

        voltage_setting_group_layout.addWidget(self.focus_lens_one_voltage_label, 0, 0)
        voltage_setting_group_layout.addWidget(self.focus_lens_one_voltage_text, 0, 1)
        voltage_setting_group_layout.addWidget(self.focus_lens_two_voltage_label, 1, 0)
        voltage_setting_group_layout.addWidget(self.focus_lens_two_voltage_text, 1, 1)
        voltage_setting_group_layout.addWidget(self.focus_lens_three_voltage_label, 2, 0)
        voltage_setting_group_layout.addWidget(self.focus_lens_three_voltage_text, 2, 1)
        voltage_setting_group_layout.addWidget(self.focus_lens_four_voltage_label, 3, 0)
        voltage_setting_group_layout.addWidget(self.focus_lens_four_voltage_text, 3, 1)
        voltage_setting_group_layout.addWidget(self.filament_voltage_label, 4, 0)
        voltage_setting_group_layout.addWidget(self.filament_voltage_text, 4, 1)
        voltage_setting_group_layout.addWidget(self.bias_voltage_label, 5, 0)
        voltage_setting_group_layout.addWidget(self.bias_voltage_text, 5, 1)
        voltage_setting_group_layout.addWidget(self.dynamo_voltage_label, 6, 0)
        voltage_setting_group_layout.addWidget(self.dynamo_voltage_text, 6, 1)
        voltage_setting_group_layout.addWidget(self.multiplier_voltage_label, 7, 0)
        voltage_setting_group_layout.addWidget(self.multiplier_voltage_text, 7, 1)
        voltage_setting_group_layout.addWidget(self.deflection_voltage_label, 8, 0)
        voltage_setting_group_layout.addWidget(self.deflection_voltage_text, 8, 1)

        voltage_setting_group_layout.addWidget(self.filament_current_label, 9, 0)
        voltage_setting_group_layout.addWidget(self.filament_current_text, 9, 1)
        voltage_setting_group_layout.addWidget(self.btn_voltage_setting, 10, 0)

        self.temperature_setting_group = QtWidgets.QGroupBox(self.frame)
        self.temperature_setting_group.setTitle("温度设置")
        frame_layout.addWidget(self.temperature_setting_group, 1, 1)
        temperature_setting_group_layout = QGridLayout(self.temperature_setting_group)
        self.temperature_setting_group.setLayout(temperature_setting_group_layout)

        self.ion_source_temp_label = QtWidgets.QLabel(self.temperature_setting_group)
        self.ion_source_temp_label.setText("离子源温度")
        self.ion_source_temp_text = QtWidgets.QLineEdit(self.temperature_setting_group)
        self.quadrupole_temp_label = QtWidgets.QLabel(self.temperature_setting_group)
        self.quadrupole_temp_label.setText("四级杆温度")
        self.quadrupole_temp_text = QtWidgets.QLineEdit(self.temperature_setting_group)
        self.temperament_interface_temp_label = QtWidgets.QLabel(self.temperature_setting_group)
        self.temperament_interface_temp_label.setText("气质接口")
        self.temperament_interface_temp_text = QtWidgets.QLineEdit(self.temperature_setting_group)
        self.btn_temperature_setting = QtWidgets.QPushButton(self.temperature_setting_group)
        self.btn_temperature_setting.setText("下载")
        self.btn_temperature_setting.clicked.connect(self.temperature_setting_function)

        temperature_setting_group_layout.addWidget(self.ion_source_temp_label, 0, 0)
        temperature_setting_group_layout.addWidget(self.ion_source_temp_text, 0, 1)
        temperature_setting_group_layout.addWidget(self.quadrupole_temp_label, 1, 0)
        temperature_setting_group_layout.addWidget(self.quadrupole_temp_text, 1, 1)
        temperature_setting_group_layout.addWidget(self.temperament_interface_temp_label, 2, 0)
        temperature_setting_group_layout.addWidget(self.temperament_interface_temp_text, 2, 1)
        temperature_setting_group_layout.addWidget(self.btn_temperature_setting, 3, 0)

        self.switch_setting_group = QtWidgets.QGroupBox(self.frame)
        self.switch_setting_group.setTitle("开关设置")

        frame_layout.addWidget(self.switch_setting_group, 1, 2)
        switch_setting_group_layout = QGridLayout(self.switch_setting_group)
        self.switch_setting_group.setLayout(switch_setting_group_layout)
        self.rf_switch_label = QtWidgets.QLabel(self.switch_setting_group)
        self.rf_switch_label.setText("RF开关")
        self.btn_rf_open = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_rf_open.setText("开")
        self.btn_rf_open.clicked.connect(self.rf_open_function)

        self.btn_rf_close = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_rf_close.setText("关")
        self.btn_rf_close.clicked.connect(self.rf_close_function)
        switch_setting_group_layout.addWidget(self.rf_switch_label, 0, 0)
        switch_setting_group_layout.addWidget(self.btn_rf_open, 0, 1)
        switch_setting_group_layout.addWidget(self.btn_rf_close, 0, 2)

        self.filament_switch_label = QtWidgets.QLabel(self.switch_setting_group)
        self.filament_switch_label.setText("灯丝开关")
        self.btn_filament_open = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_filament_open.setText("开")
        self.btn_filament_open.clicked.connect(self.filament_open_function)
        self.btn_filament_close = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_filament_close.setText("关")
        self.btn_filament_close.clicked.connect(self.filament_close_function)
        switch_setting_group_layout.addWidget(self.filament_switch_label, 1, 0)
        switch_setting_group_layout.addWidget(self.btn_filament_open, 1, 1)
        switch_setting_group_layout.addWidget(self.btn_filament_close, 1, 2)
        self.hv_switch_label = QtWidgets.QLabel(self.switch_setting_group)
        self.hv_switch_label.setText("HV高压板上电开关")

        self.btn_hv_open = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_hv_open.setText("开")
        self.btn_hv_open.clicked.connect(self.hv_open_function)
        self.btn_hv_close = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_hv_close.setText("关")
        self.btn_hv_close.clicked.connect(self.hv_close_function)
        switch_setting_group_layout.addWidget(self.hv_switch_label, 2, 0)
        switch_setting_group_layout.addWidget(self.btn_hv_open, 2, 1)
        switch_setting_group_layout.addWidget(self.btn_hv_close, 2, 2)
        experiment_switch_label = QtWidgets.QLabel(self.switch_setting_group)
        experiment_switch_label.setText("实验开关")
        btn_experiment_open = QtWidgets.QPushButton(self.switch_setting_group)
        btn_experiment_open.setText("开")
        btn_experiment_open.clicked.connect(self.experiment_open_function)
        btn_experiment_close = QtWidgets.QPushButton(self.switch_setting_group)
        btn_experiment_close.setText("关")
        btn_experiment_close.clicked.connect(self.experiment_close_function)

        switch_setting_group_layout.addWidget(experiment_switch_label, 3, 0)
        switch_setting_group_layout.addWidget(btn_experiment_open, 3, 1)
        switch_setting_group_layout.addWidget(btn_experiment_close, 3, 2)
        self.standard_liquid_valve_switch_label = QtWidgets.QLabel(self.switch_setting_group)
        self.standard_liquid_valve_switch_label.setText("标液阀门控制")
        self.btn_standard_liquid_valve_open = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_standard_liquid_valve_open.setText("开")
        self.btn_standard_liquid_valve_open.clicked.connect(self.standard_liquid_valve_open_function)
        self.btn_standard_liquid_valve_close = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_standard_liquid_valve_close.setText("关")
        self.btn_standard_liquid_valve_close.clicked.connect(self.standard_liquid_valve_close_function)
        switch_setting_group_layout.addWidget(self.standard_liquid_valve_switch_label, 4, 0)
        switch_setting_group_layout.addWidget(self.btn_standard_liquid_valve_open, 4, 1)
        switch_setting_group_layout.addWidget(self.btn_standard_liquid_valve_close, 4, 2)
        self.vent_valve_switch_label = QtWidgets.QLabel(self.switch_setting_group)
        self.vent_valve_switch_label.setText("放空阀门控制")
        self.btn_vent_valve_open = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_vent_valve_open.setText("开")
        self.btn_vent_valve_open.clicked.connect(self.vent_valve_open_function)
        self.btn_vent_valve_close = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_vent_valve_close.setText("关")
        self.btn_vent_valve_close.clicked.connect(self.vent_valve_close_function)
        switch_setting_group_layout.addWidget(self.vent_valve_switch_label, 5, 0)
        switch_setting_group_layout.addWidget(self.btn_vent_valve_open, 5, 1)
        switch_setting_group_layout.addWidget(self.btn_vent_valve_close, 5, 2)

        self.molecular_pump_switch_label = QtWidgets.QLabel(self.switch_setting_group)
        self.molecular_pump_switch_label.setText("分子泵的开关")
        self.btn_molecular_pump_open = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_molecular_pump_open.setText("开")
        self.btn_molecular_pump_open.clicked.connect(self.molecular_pump_open)
        self.btn_molecular_pump_close = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_molecular_pump_close.setText("关")
        self.btn_molecular_pump_close.clicked.connect(self.molecular_pump_close)
        switch_setting_group_layout.addWidget(self.molecular_pump_switch_label, 6, 0)
        switch_setting_group_layout.addWidget(self.btn_molecular_pump_open, 6, 1)
        switch_setting_group_layout.addWidget(self.btn_molecular_pump_close, 6, 2)
        self.temperature_switch_label = QtWidgets.QLabel(self.switch_setting_group)
        self.temperature_switch_label.setText("温度开关")
        self.btn_temperature_open = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_temperature_open.setText("开")
        self.btn_temperature_open.clicked.connect(self.temperature_open_function)
        self.btn_temperature_close = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_temperature_close.setText("关")
        self.btn_temperature_close.clicked.connect(self.temperature_close_function)
        switch_setting_group_layout.addWidget(self.temperature_switch_label, 7, 0)
        switch_setting_group_layout.addWidget(self.btn_temperature_open, 7, 1)
        switch_setting_group_layout.addWidget(self.btn_temperature_close, 7, 2)
        self.filament_switch_label = QtWidgets.QLabel(self.switch_setting_group)
        self.filament_switch_label.setText("灯丝切换")
        self.btn_filament_open = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_filament_open.setText("1")
        self.btn_filament_open.clicked.connect(self.filament_one_switch_function)
        self.btn_filament_close = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_filament_close.setText("2")
        self.btn_filament_close.clicked.connect(self.filament_two_switch_function)
        switch_setting_group_layout.addWidget(self.filament_switch_label, 8, 0)
        switch_setting_group_layout.addWidget(self.btn_filament_open, 8, 1)
        switch_setting_group_layout.addWidget(self.btn_filament_close, 8, 2)
        self.HVDC_switch_label = QtWidgets.QLabel(self.switch_setting_group)
        self.HVDC_switch_label.setText("HVDC极性切换")
        self.btn_HVDC_open = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_HVDC_open.setText("开")
        self.btn_HVDC_open.clicked.connect(self.HVDC_open_function)
        self.btn_HVDC_close = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_HVDC_close.setText("关")
        self.btn_HVDC_close.clicked.connect(self.HVDC_close_function)
        switch_setting_group_layout.addWidget(self.HVDC_switch_label, 9, 0)
        switch_setting_group_layout.addWidget(self.btn_HVDC_open, 9, 1)
        switch_setting_group_layout.addWidget(self.btn_HVDC_close, 9, 2)
        self.fan_switch_label = QtWidgets.QLabel(self.switch_setting_group)
        self.fan_switch_label.setText("风扇")
        self.btn_fan_open = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_fan_open.setText("开")
        self.btn_fan_open.clicked.connect(self.fan_open_function)
        self.btn_fan_close = QtWidgets.QPushButton(self.switch_setting_group)
        self.btn_fan_close.setText("关")
        self.btn_fan_close.clicked.connect(self.fan_close_function)
        switch_setting_group_layout.addWidget(self.fan_switch_label, 10, 0)
        switch_setting_group_layout.addWidget(self.btn_fan_open, 10, 1)
        switch_setting_group_layout.addWidget(self.btn_fan_close, 10, 2)

    def molecular_pump_open(self):

        data = [protocol.SWITCH.ON[0]]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.MOLECULAR_PUMP_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def molecular_pump_close(self):
        data = [protocol.SWITCH.OFF]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.MOLECULAR_PUMP_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def rf_setting_function(self):
        # print('dfs')
        rf_low_voltage = int(self.rf_low_voltage_text.text())
        rf_low_voltage = int(rf_low_voltage / 1000 / 2 * 1000)
        rf_high_voltage = int(self.rf_high_voltage_text.text())
        rf_high_voltage = int(rf_high_voltage / 1000 / 2 * 1000)
        rf_scan_time = int(self.rf_scan_time_text.text())
        rf_scan_frequency = int(self.rf_scan_frequency_text.text())
        count = (rf_scan_time / 10000) / (1 / rf_scan_frequency)
        self.server.count = count
        data = [rf_low_voltage, rf_high_voltage, rf_scan_time, rf_scan_frequency]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.RF_PARAM_SET[0]
        length = 8
        self.sendMessage(command_code, length, data)

    def dc_one_setting_function(self):
        dc_one_low_voltage = int(self.dc_one_low_voltage_text.text())
        dc_one_low_voltage = int(dc_one_low_voltage / 200 / 2 * 1000)
        dc_one_high_voltage = int(self.dc_one_high_voltage_text.text())
        dc_one_high_voltage = int(dc_one_high_voltage / 200 / 2 * 1000)
        dc_one_scan_time = int(self.rf_scan_time_text.text())
        dc_one_scan_frequency = int(self.rf_scan_frequency_text.text())
        data = [dc_one_low_voltage, dc_one_high_voltage, dc_one_scan_time, dc_one_scan_frequency]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.DC_ONE_PARAM_SET[0]
        length = 8
        self.sendMessage(command_code, length, data)

    def dc_two_setting_function(self):
        dc_two_low_voltage = int(self.dc_two_low_voltage_text.text())
        dc_two_low_voltage = int(dc_two_low_voltage / 200 / 1 * 1000)
        dc_two_high_voltage = int(self.dc_two_high_voltage_text.text())
        dc_two_high_voltage = int(dc_two_high_voltage / 200 / 1 * 1000)
        dc_two_scan_time = int(self.dc_two_scan_time_text.text())
        dc_two_scan_frequency = int(self.dc_two_scan_frequency_text.text())
        data = [dc_two_low_voltage, dc_two_high_voltage, dc_two_scan_time, dc_two_scan_frequency]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.DC_TWO_PARAM_SET[0]
        length = 8
        self.sendMessage(command_code, length, data)

    def voltage_setting_function(self):

        focus_lens_one_voltage = int(self.focus_lens_one_voltage_text.text())
        focus_lens_one_voltage = int(10 * (50 - focus_lens_one_voltage))
        focus_lens_two_voltage = int(self.focus_lens_two_voltage_text.text())
        focus_lens_two_voltage = int(10 * (50 - focus_lens_two_voltage))
        focus_lens_three_voltage = int(self.focus_lens_three_voltage_text.text())
        focus_lens_three_voltage = int(10 * (50 - focus_lens_three_voltage))
        focus_lens_four_voltage = int(self.focus_lens_four_voltage_text.text())
        focus_lens_four_voltage = int(10 * (50 - focus_lens_four_voltage))
        filament_voltage = int(self.filament_voltage_text.text())
        filament_voltage = int(abs(filament_voltage) / 20 * 1000)
        filament_current = int(self.filament_current_text.text())
        filament_current = int(filament_current * 0.375 * 13.2 + 130)
        bias_voltage = int(self.bias_voltage_text.text())
        bias_voltage = int(10 * (50 - bias_voltage))
        dynamo_voltage = int(self.dynamo_voltage_text.text())
        dynamo_voltage = int(dynamo_voltage / 2000 / 3 * 1000)
        multiplier_voltage = int(self.multiplier_voltage_text.text())
        multiplier_voltage = int(multiplier_voltage / 400 / 3 * 1000)
        deflection_voltage = int(self.deflection_voltage_text.text())
        deflection_voltage = int(deflection_voltage / 400 / 3 * 1000)

        data = [focus_lens_four_voltage, focus_lens_one_voltage, focus_lens_two_voltage, focus_lens_three_voltage,
                filament_voltage, filament_current, bias_voltage, dynamo_voltage, multiplier_voltage,
                deflection_voltage]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.OTHER_PARAM_SET[0]
        length = 20
        self.sendMessage(command_code, length, data)

    def temperature_setting_function(self):
        ion_source_temp = int(self.ion_source_temp_text.text())
        quadrupole_temp = int(self.quadrupole_temp_text.text())
        temperament_interface_temp = int(self.temperament_interface_temp_text.text())
        data = [ion_source_temp, quadrupole_temp, temperament_interface_temp]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.TEMPERATURE_SET[0]
        length = 6
        self.sendMessage(command_code, length, data)

    def sendMessage(self, command_code, length, data_list):
        message = []
        data = bytes()
        head_code = 0x55
        tail_head = 0xAA
        data = data + (int.to_bytes(head_code, length=1, byteorder='big',signed=False))
        data = data + (int.to_bytes(command_code, length=1, byteorder='big',signed=False))
        message.append(command_code)
        message.append(length)
        for item in data_list:
            message.append(item)
        if length > 1:
            for i in range(1, len(message)):
                data = data + int.to_bytes(message[i], length=2, byteorder='big', signed=True)
        else:
            # data = data + int.to_bytes(message[0], length=1, byteorder='big', signed=False)
            data = data + int.to_bytes(message[1], length=2, byteorder='big', signed=True)
            data = data + int.to_bytes(message[2], length=length, byteorder='big', signed=True)
        sum_check = sum(data[1:])
        data = data + int.to_bytes(sum_check, length=2, byteorder='big', signed=True)
        data = data + int.to_bytes(tail_head, length=1, byteorder='big', signed=False)
        print("发送", data.hex())
        # print(data)

        self.server.client_socket.send(data)

    def rf_open_function(self):

        rf_scan_frequency = protocol.SWITCH.ON[0]
        data = [rf_scan_frequency]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.RF_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def rf_close_function(self):
        rf_scan_frequency = protocol.SWITCH.OFF
        data = [rf_scan_frequency]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.RF_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def filament_open_function(self):
        filament_switch = protocol.SWITCH.ON[0]
        data = [filament_switch]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.FILAMENT_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def filament_close_function(self):
        filament_switch = protocol.SWITCH.OFF
        data = [filament_switch]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.FILAMENT_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def hv_open_function(self):
        hv_switch = protocol.SWITCH.ON[0]
        data = [hv_switch]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.HV_HIGH_VOLTAGE_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def hv_close_function(self):
        hv_switch = protocol.SWITCH.OFF
        data = [hv_switch]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.HV_HIGH_VOLTAGE_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def experiment_open_function(self):
        experiment_switch = protocol.SWITCH.ON[0]
        data = [experiment_switch]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.EXPERIMENT_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def experiment_close_function(self):
        data = [protocol.SWITCH.OFF]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.EXPERIMENT_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def standard_liquid_valve_open_function(self):
        data = [protocol.SWITCH.ON[0]]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.STANDARD_LIQUID_VALVE_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def standard_liquid_valve_close_function(self):
        data = [protocol.SWITCH.OFF]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.STANDARD_LIQUID_VALVE_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def vent_valve_open_function(self):
        data = [protocol.SWITCH.ON[0]]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.VENT_VALVE_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def vent_valve_close_function(self):
        data = [protocol.SWITCH.OFF]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.VENT_VALVE_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def temperature_open_function(self):

        data = [protocol.SWITCH.ON[0]]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.TEMPERATURE_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def temperature_close_function(self):

        data = [protocol.SWITCH.OFF]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.TEMPERATURE_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def filament_one_switch_function(self):
        data = [protocol.SWITCH.ON[0]]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.FILAMENT_SELECT[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def filament_two_switch_function(self):
        data = [protocol.SWITCH.OFF]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.FILAMENT_SELECT[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def HVDC_open_function(self):
        data = [protocol.SWITCH.ON[0]]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.HVDC_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def HVDC_close_function(self):
        data = [protocol.SWITCH.OFF]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.HVDC_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def fan_open_function(self):
        data = [protocol.SWITCH.ON[0]]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.FAN_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def fan_close_function(self):
        data = [protocol.SWITCH.OFF]
        command_code = protocol.DATA_REQUEST_AND_RESPONSE.FAN_SWITCH[0]
        length = 1
        self.sendMessage(command_code, length, data)

    def set_server(self, server):
        self.server = server
