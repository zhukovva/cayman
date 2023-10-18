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
        config_data = ConfigData(self.config_file_path)
        if config_data.tree is None:
            self.error_window(config_data.error_message)


    def error_window(self, error_message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Внимание!")
        msg.setInformativeText(error_message)
        msg.setWindowTitle("Ошибка")
        msg.exec_()
