from PyQt5 import QtWidgets, QtGui, QtCore
import MainWindow
from ConfigDataXml import ConfigData


class MyWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, config_file_path, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.lineEdit_3.setInputMask("009.009.009.009;_")
        self.tabWidget.setCurrentIndex(0)
        self.config_file_path = config_file_path
        self.config_data = ConfigData(self.config_file_path)
        self.config_data_list = []
        if not self.config_data.error_check:
            self.error_window(self.config_data.error_message)
        if self.config_data.error_check:
            self.load_tableview()
            self.radio_button_list = []
            self.label_list = []
            self.h_layout_list = []
            self.v_layout = self.r_button_generator(self.new_model.rowCount())
            self.horizontalLayout_2.addLayout(self.v_layout)

    @staticmethod
    def error_window(error_message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Внимание!")
        msg.setInformativeText(error_message)
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    def load_tableview(self):
        for config in self.config_data.config_list:
            standard_item_list = []
            data = []
            for key in config.keys():
                item = QtGui.QStandardItem()
                item.setData(config[key], QtCore.Qt.DisplayRole)
                standard_item_list.append(item)
                data.append(config[key])
            self.new_model.appendRow(standard_item_list)
            self.config_data_list.append(data)
        print(self.config_data_list)
        # self.tableView.setModel(self.new_model)
        self.tableView_2.setModel(self.new_model)

    def r_button_generator(self, row_count):
        self.radio_button_list = []
        for row in range(0, row_count):
            rb_list = []
            for b_num in range(0, 4):
                r_b = QtWidgets.QRadioButton(self.tab_1)
                rb_list.append(r_b)
            self.radio_button_list.append(rb_list)

        self.h_layout_list = []
        i = 0
        for row in self.radio_button_list:
            h_layout = QtWidgets.QHBoxLayout(self.tab_1)
            label_name = QtWidgets.QLabel(self.config_data_list[i][0])
            label_ip = QtWidgets.QLabel(self.config_data_list[i][1])
            label_path = QtWidgets.QLabel(self.config_data_list[i][2])
            size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            label_name.setSizePolicy(size_policy)
            label_ip.setSizePolicy(size_policy)
            label_path.setSizePolicy(size_policy)
            label_name.setStyleSheet("font-size: 14px;")
            label_ip.setStyleSheet("font-size: 14px;")
            label_path.setStyleSheet("font-size: 14px;")
            i = i + 1
            self.label_list.append(label_name)
            h_layout.addWidget(label_name)
            h_layout.addWidget(label_ip)
            h_layout.addWidget(label_path)
            for button in row:
                h_layout.addWidget(button)
            self.h_layout_list.append(h_layout)

        v_layout = QtWidgets.QVBoxLayout(self.tab_1)
        for h_layout in self.h_layout_list:
            v_layout.addLayout(h_layout)
        return v_layout
