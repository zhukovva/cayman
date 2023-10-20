from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,\
    QTabWidget, QGroupBox, QMessageBox, QRadioButton, QLabel, QSizePolicy
from ConfigDataXml import ConfigData
from MyWidgets.MyGroupBox import MyGroupBox


class MyWindow(QMainWindow):
    def __init__(self, config_file_path, parent=None):
        QMainWindow.__init__(self, parent)
        self.config_file_path = config_file_path
        self.config_data = ConfigData(self.config_file_path)
        self.config_data_list = []
        self.radio_button_list = []
        self.label_list = []
        self.group_box_list = []

        self.setObjectName("MainWindow")
        self.resize(700, 400)
        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.setCentralWidget(self.central_widget)
        self.vertical_layout_1 = QVBoxLayout(self.central_widget)
        self.vertical_layout_1.setObjectName("vertical_layout_1")
        self.tab_widget = QTabWidget(self.central_widget)
        self.tab_widget.setObjectName("tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName("tab_1")
        self.vertical_layout_2 = QVBoxLayout(self.tab_1)
        self.vertical_layout_2.setObjectName("vertical_layout_2")

        if not self.config_data.error_check:
            self.error_window(self.config_data.error_message)
        if self.config_data.error_check:
            self.load_tableview()
            self.vertical_layout_3 = self.r_button_generator(len(self.config_data_list))
            self.vertical_layout_2.addLayout(self.vertical_layout_3)
        self.tab_widget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")

        self.tab_widget.addTab(self.tab_2, "")
        self.vertical_layout_1.addWidget(self.tab_widget)
        self.setCentralWidget(self.central_widget)
        self.setStyleSheet("QMainWindow {\n"
                           "    background-color:rgb(82, 82, 82);\n"
                           "}\n"
                           "QTabWidget::pane {\n"
                           "        border-color: rgb(77,77,77);\n"
                           "        background-color:rgb(101,101,101);\n"
                           "        border-style: solid;\n"
                           "        border-width: 1px;\n"
                           "        border-radius: 6px;\n"
                           "}\n"
                           )

    @staticmethod
    def error_window(error_message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Внимание!")
        msg.setInformativeText(error_message)
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    def load_tableview(self):
        for config in self.config_data.config_list:
            data = []
            for key in config.keys():
                data.append(config[key])
            self.config_data_list.append(data)

    def r_button_generator(self, row_count):
        self.radio_button_list = []
        for row in range(0, row_count):
            rb_list = []
            for b_num in range(0, 4):
                r_b = QRadioButton(self.tab_1)
                rb_list.append(r_b)
            self.radio_button_list.append(rb_list)

        i = 0
        for row in self.radio_button_list:
            group_box = MyGroupBox()
            group_box.setStyleSheet("background: rgb(82, 82, 82); border-radius: 3px;")
            h_layout = QHBoxLayout(self.tab_1)
            label_name = QLabel(self.config_data_list[i][0])
            label_ip = QLabel(self.config_data_list[i][1])
            label_path = QLabel(self.config_data_list[i][2])
            size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            label_name.setSizePolicy(size_policy)
            label_ip.setSizePolicy(size_policy)
            label_path.setSizePolicy(size_policy)
            label_name.setStyleSheet("font-size: 14px; color: white;")
            label_ip.setStyleSheet("font-size: 14px; color: white;")
            label_path.setStyleSheet("font-size: 14px; color: white;")
            i = i + 1
            self.label_list.append(label_name)
            h_layout.addWidget(label_name)
            h_layout.addWidget(label_ip)
            h_layout.addWidget(label_path)
            for button in row:
                h_layout.addWidget(button)
            group_box.setLayout(h_layout)
            self.group_box_list.append(group_box)

        v_layout = QVBoxLayout(self.tab_1)
        for group_box in self.group_box_list:
            v_layout.addWidget(group_box)
        return v_layout
