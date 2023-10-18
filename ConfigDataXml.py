import xml.etree.ElementTree as XML_module
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QMessageBox


class ConfigData:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.tree = None
        self.root = None
        self.error_message = None
        self.get_root()

    def get_root(self):
        try:
            tree = XML_module.parse(self.config_file_path)
            root = tree.getroot()
            self.tree = tree
            self.root = root
        except XML_module.ParseError as err:
            err.msg = "Ошибка разметки файла"
            self.error_message = err.msg
        except FileNotFoundError as err:
            err.msg = '{}'.format(err)
            self.error_message = err.msg
