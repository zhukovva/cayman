from PyQt5.QtWidgets import QGroupBox, QLabel


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
                combobox_child_label = self.findChild(QLabel, 'label_ip')
                parent_tab = self.parent()
                parent_tab_child_label = parent_tab.findChild(MyLabel)
                parent_tab_child_label.setText(f'Скачать с {combobox_child_label.text()}')
                parent_tab_child_label.download_list.append(combobox_child_label.text())

            else:
                self.setStyleSheet("background: rgb(82, 82, 82); border-radius: 3px;")
                self.check = False
                combobox_child_label = self.findChild(QLabel, 'label_ip')
                parent_tab = self.parent()
                parent_tab_child_label = parent_tab.findChild(MyLabel)
                parent_tab_child_label.download_list.remove(combobox_child_label.text())

class MyLabel(QLabel):

    def __init__(self, text):
        super().__init__(text)
        self.download_list = []
