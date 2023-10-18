from PyQt5 import QtWidgets, QtGui, QtCore
import MainWindow
from ConfigDataXml import ConfigData
from PyQt5.QtCore import QObject, pyqtSignal


class MyWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, config_file_path, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.lineEdit_3.setInputMask("009.009.009.009;_")
        self.tabWidget.setCurrentIndex(0)
        self.config_file_path = config_file_path
        self.config_data = ConfigData(self.config_file_path)
        if not self.config_data.error_check:
            self.error_window(self.config_data.error_message)
        if self.config_data.error_check:
            self.load_tableview()

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
            for key in config.keys():
                item = QtGui.QStandardItem()
                item.setData(config[key], QtCore.Qt.DisplayRole)
                standard_item_list.append(item)
            self.new_model.appendRow(standard_item_list)
        self.tableView.setModel(self.new_model)
        self.tableView_2.setModel(self.new_model)
        self.tableView.resizeColumnToContents(0)
        self.tableView.resizeColumnToContents(1)
        self.tableView.resizeColumnToContents(2)
        self.tableView.resizeColumnToContents(3)
        self.tableView_2.resizeColumnsToContents()
