from PyQt5 import QtWidgets
import sys, os
from MyWindow import MyWindow

if __name__ == "__main__":
    config_file_path = os.getcwd() + "\\config\\config.xml"
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow(config_file_path)
    window.show()
    sys.exit(app.exec_())
