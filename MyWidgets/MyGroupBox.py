from PyQt5.QtWidgets import QGroupBox


class MyGroupBox(QGroupBox):

    def __init__(self):
        super().__init__()

    def enterEvent(self, event):
        self.setStyleSheet("background: grey; border-radius: 3px;")

    def leaveEvent(self, event):
        self.setStyleSheet("background: rgb(82, 82, 82); border-radius: 3px;")
