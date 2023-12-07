from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, \
    QTabWidget, QMessageBox, QRadioButton, QLabel, QSizePolicy, QPushButton, \
    QProgressBar, QDateEdit
from PyQt5.QtCore import Qt, QDateTime, QDate, QTime
from datetime import datetime
from ConfigDataXml import ConfigData
from MyWidgets.MyGroupBox import MyGroupBox, MyLabel


class MyWindow(QMainWindow):
    def __init__(self, config_file_path, parent=None):
        QMainWindow.__init__(self, parent)
        self.config_file_path = config_file_path
        self.config_data = ConfigData(self.config_file_path)
        self.config_data_list = []
        self.radio_button_list = []
        self.label_list = []
        self.group_box_list = []

        self.setObjectName("main_window")
        self.resize(700, 400)
        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.setCentralWidget(self.central_widget)
        self.vertical_layout_1 = QVBoxLayout(self.central_widget)
        self.vertical_layout_1.setObjectName("vertical_layout_1")
        self.tab_widget = QTabWidget(self.central_widget)
        self.tab_widget.setObjectName("tabWidget")
        """Tab_1"""
        self.tab_1 = QWidget()
        self.tab_1.setObjectName("tab_1")
        self.vertical_layout_2 = QVBoxLayout(self.tab_1)
        self.vertical_layout_2.setObjectName("vertical_layout_2")
        """Tab_1 Header"""
        self.horizontal_layout_1 = QHBoxLayout(self.tab_1)
        self.label_size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label_header_name = QLabel("Название")
        self.label_header_name.setAlignment(Qt.AlignCenter)
        self.label_header_ip = QLabel("IP адрес")
        self.label_header_ip.setObjectName("label_header_ip")
        self.label_header_ip.setAlignment(Qt.AlignCenter)
        self.label_header_path = QLabel("Путь сохранения")
        self.label_header_path.setAlignment(Qt.AlignCenter)
        self.label_header_channel = QLabel("Каналы")
        self.label_header_channel.setAlignment(Qt.AlignCenter)
        self.horizontal_layout_1.addWidget(self.label_header_name)
        self.horizontal_layout_1.addWidget(self.label_header_ip)
        self.horizontal_layout_1.addWidget(self.label_header_path)
        self.horizontal_layout_1.addWidget(self.label_header_channel)
        self.vertical_layout_2.addLayout(self.horizontal_layout_1)
        """"Tab_1 Data table"""
        if not self.config_data.error_check:
            self.error_window(self.config_data.error_message)
        if self.config_data.error_check:
            self.load_tableview()
            self.vertical_layout_3 = self.r_button_generator(len(self.config_data_list))
            self.vertical_layout_2.addLayout(self.vertical_layout_3)
        """Tab_1 Buttons"""
        self.horizontal_layout_2 = QHBoxLayout(self.tab_1)
        self.label_status = MyLabel("file_name + status")
        self.button_download = QPushButton("Загрузить")
        self.button_download.clicked.connect(self.download_button_click)
        self.dateEdit = QDateEdit(self.tab_1)
        self.dateEdit.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(datetime.now())  # установка даты на сегодня
        self.dateEdit.setMaximumDate(datetime.now())  # установка максимальной даты
        self.horizontal_layout_2.addWidget(self.label_status)
        self.horizontal_layout_2.addWidget(self.dateEdit)
        self.horizontal_layout_2.addWidget(self.button_download)
        self.vertical_layout_2.addLayout(self.horizontal_layout_2)

        self.tab_widget.addTab(self.tab_1, "")
        """Tab_2"""
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")

        self.tab_widget.addTab(self.tab_2, "")
        self.vertical_layout_1.addWidget(self.tab_widget)
        """Tab widget"""
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_1), "Скачать с Cayman")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), "Автоматическое скачивание")
        self.setCentralWidget(self.central_widget)
        self.style()  # applying style

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
                r_b.setObjectName(str(b_num))
                r_b.setAutoExclusive(False)
                rb_list.append(r_b)
            self.radio_button_list.append(rb_list)

        i = 0
        for row in self.radio_button_list:
            group_box = MyGroupBox()
            group_box.setStyleSheet("background: rgb(82, 82, 82); border-radius: 3px;")
            h_layout = QHBoxLayout(self.tab_1)
            label_name = QLabel(self.config_data_list[i][0])
            label_name.setObjectName("label_name")
            label_ip = QLabel(self.config_data_list[i][1])
            label_ip.setObjectName("label_ip")
            label_path = QLabel(self.config_data_list[i][2])
            label_path.setObjectName("label_path")
            label_name.setSizePolicy(self.label_size_policy)
            label_ip.setSizePolicy(self.label_size_policy)
            label_path.setSizePolicy(self.label_size_policy)
            label_name.setStyleSheet("font-size: 12px; color: white;")
            label_ip.setStyleSheet("font-size: 12px; color: white;")
            label_path.setStyleSheet("font-size: 12px; color: white;")
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

    def download_button_click(self):
        for group_box in self.group_box_list:
            label_ip = group_box.findChild(QLabel, 'label_ip')
            if label_ip.text() in self.label_status.download_list:
                download_config_list = []
                label_name = group_box.findChild(QLabel, 'label_name')
                download_config_list.append(label_name.text())
                download_config_list.append(label_ip.text())
                label_path = group_box.findChild(QLabel, 'label_path')
                download_config_list.append(label_path.text())
                radio_b1 = group_box.findChild(QRadioButton, '0')
                download_config_list.append(str(radio_b1.isChecked()))
                radio_b2 = group_box.findChild(QRadioButton, '1')
                download_config_list.append(str(radio_b2.isChecked()))
                radio_b3 = group_box.findChild(QRadioButton, '2')
                download_config_list.append(str(radio_b3.isChecked()))
                radio_b4 = group_box.findChild(QRadioButton, '3')
                download_config_list.append(str(radio_b4.isChecked()))
                print(download_config_list)

    def style(self):
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
                           "QTabWidget {\n"
                           "    color:rgb(0,0,0);\n"
                           "    background-color:rgb(247,246,246);\n"
                           "}\n"
                           "QTabWidget::pane {\n"
                           "        border-color: rgb(77,77,77);\n"
                           "        background-color:rgb(101,101,101);\n"
                           "        border-style: solid;\n"
                           "        border-width: 1px;\n"
                           "        border-radius: 6px;\n"
                           "}\n"
                           "QTabBar::tab {\n"
                           "    padding:2px;\n"
                           "    color:rgb(250,250,250);\n"
                           "      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
                           "    border-style: solid;\n"
                           "    border-width: 2px;\n"
                           "      border-top-right-radius:4px;\n"
                           "   border-top-left-radius:4px;\n"
                           "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
                           "    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
                           "    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
                           "    border-bottom-color: rgb(101,101,101);\n"
                           "}\n"
                           "QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
                           "      background-color:rgb(101,101,101);\n"
                           "      margin-left: 0px;\n"
                           "      margin-right: 1px;\n"
                           "}\n"
                           "QTabBar::tab:!selected {\n"
                           "        margin-top: 1px;\n"
                           "        margin-right: 1px;\n"
                           "}\n"
                           "QLabel {\n"
                           "    color:rgb(255,255,255);    \n"
                           "}\n"
                           "QProgressBar {\n"
                           "    text-align: center;\n"
                           "    color: rgb(240, 240, 240);\n"
                           "    border-width: 1px; \n"
                           "    border-radius: 10px;\n"
                           "    border-color: rgb(58, 58, 58);\n"
                           "    border-style: inset;\n"
                           "    background-color:rgb(77,77,77);\n"
                           "}\n"
                           "QProgressBar::chunk {\n"
                           "    background-color: qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
                           "    border-radius: 5px;\n"
                           "}\n"
                           "QPushButton{\n"
                           "    border-style: outset;\n"
                           "    border-width: 2px;\n"
                           "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
                           "    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
                           "    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
                           "    border-bottom-color: rgb(58, 58, 58);\n"
                           "    border-bottom-width: 1px;\n"
                           "    border-style: solid;\n"
                           "    color: rgb(255, 255, 255);\n"
                           "    padding: 2px;\n"
                           "    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
                           "}\n"
                           "QPushButton:hover{\n"
                           "    border-style: outset;\n"
                           "    border-width: 2px;\n"
                           "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
                           "    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
                           "    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
                           "    border-bottom-color: rgb(115, 115, 115);\n"
                           "    border-bottom-width: 1px;\n"
                           "    border-style: solid;\n"
                           "    color: rgb(255, 255, 255);\n"
                           "    padding: 2px;\n"
                           "    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
                           "}\n"
                           "QPushButton:pressed{\n"
                           "    border-style: outset;\n"
                           "    border-width: 2px;\n"
                           "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(22, 22, 22, 255));\n"
                           "    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
                           "    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
                           "    border-bottom-color: rgb(58, 58, 58);\n"
                           "    border-bottom-width: 1px;\n"
                           "    border-style: solid;\n"
                           "    color: rgb(255, 255, 255);\n"
                           "    padding: 2px;\n"
                           "    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
                           "}\n"
                           "QPushButton:disabled{\n"
                           "    border-style: outset;\n"
                           "    border-width: 2px;\n"
                           "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
                           "    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
                           "    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
                           "    border-bottom-color: rgb(58, 58, 58);\n"
                           "    border-bottom-width: 1px;\n"
                           "    border-style: solid;\n"
                           "    color: rgb(0, 0, 0);\n"
                           "    padding: 2px;\n"
                           "    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
                           "}\n"
                           )
