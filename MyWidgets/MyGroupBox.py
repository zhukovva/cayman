from PyQt5.QtWidgets import QGroupBox


class MyGroupBox(QGroupBox):

    def __init__(self):
        super().__init__()
        self.check = False
        self.block = False

    def enterEvent(self, event):
        if not self.check:
            self.setStyleSheet("background: grey; border-radius: 3px;")

    def leaveEvent(self, event):
        if not self.check:
            self.setStyleSheet("background: rgb(82, 82, 82); border-radius: 3px;")

    def mouseDoubleClickEvent(self, event):
        if not self.block:
            if not self.check:
                self.setStyleSheet("background: rgb(0, 128, 0); border-radius: 3px;")
                self.check = True
            else:
                self.check = False
