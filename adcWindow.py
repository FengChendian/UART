import sys

from PyQt5 import QtWidgets
from matplotlib import pyplot as plt
import port

# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy

from PyQt5.QtGui import QIcon


class adcWindow(QWidget):
    def __init__(self, port: port.Port):
        super().__init__()
        self.directory = 'C:/data'
        self.port = port
        self.setWindowTitle("ADC")
        self.initUI()
        self.initPort()

    def initUI(self):

        self.directoryLabel = QLabel()
        self.directoryLabel.setText(self.directory)

        self.selection = QPushButton()
        self.selection.setText("选择数据存储路径")
        self.selection.clicked.connect(self.select)

        self.collection = QPushButton()
        self.collection.setText('采集')
        self.collection.clicked.connect(self.collect)

        hBox = QHBoxLayout()
        hBox.addWidget(self.directoryLabel)
        hBox.addWidget(self.selection)

        vBox = QVBoxLayout()
        vBox.addLayout(hBox)
        vBox.addWidget(self.collection)
        self.setLayout(vBox)
        self.show()
    
    def initPort(self):
        
        if(self.port.ser is None):
            result = self.port.openPort()
            if result is False:
                QMessageBox.information(self, '提示', '自动连接串口失败\n请手动连接', QMessageBox.Ok)


    def select(self):
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(
            self, "选择存储路径", "./")
        self.directoryLabel.setText(self.directory)

    def collect(self):
        data = self.port.fetchDataElement_uint8()
        plt.figure(1)
        plt.plot(data[:200])
        plt.show()
        
