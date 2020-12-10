
# from mainWindow import MainAPP
from port import Port
from PyQt5.QtWidgets import QApplication, QComboBox, QHBoxLayout, QLabel, QWidget


class Settings(QWidget):
    def __init__(self, port: Port):
        super().__init__()
        self.setWindowTitle('设置')
        self.bandRateList = ['2962962', '115200']
        self.port = port
        self.initUI()

    def initUI(self):
        self.baundRateLabel = QLabel('波特率')
        self.baundRateButton = QComboBox()
        self.baundRateButton.addItems(self.bandRateList)
        self.baundRateButton.setEnabled(False)

        hbox = QHBoxLayout()
        hbox.addWidget(self.baundRateLabel)
        hbox.addWidget(self.baundRateButton)
        self.setLayout(hbox)
        self.show()

    def bandRateChange(self, i):
        self.port.bandradte = int(self.bandRateList[i])
        # QApplication.processEvents()
        # self.main.statusText()
        # MainAPP.refresh()
