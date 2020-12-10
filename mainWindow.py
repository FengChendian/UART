from PyQt5 import QtCore, QtWidgets
from adcWindow import adcWindow
import sys
from port import Port

# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QMessageBox, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy

from PyQt5.QtGui import QIcon

from settings import Settings


class MainAPP(QWidget):
    def __init__(self):
        super().__init__()
        self.port = Port()
        # draw UI
        self.initUI()

    def initUI(self):
        # size and location
        # self.setGeometry(500, 500, 500, 500)
        self.resize(500, 400)
        self.center()

        self.setWindowTitle("UART")

        self.setWindowIcon(QIcon("./icon/title.ico"))

        self.button()

        self.show()

    def center(self):
        window = self.frameGeometry()
        # 获取中心点
        centerPoint = QDesktopWidget().availableGeometry().center()
        window.moveCenter(centerPoint)
        # self.move(window.topLeft())

    def button(self):
        self.spectrum = QPushButton("Spectrum")
        self.spectrum.clicked.connect(self.spectrumAction)
        # self.spectrum.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.colorMap = QPushButton("ColorMap")
        self.colorMap.clicked.connect(self.colorMapAction)
        # self.colorMap.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.adc = QPushButton("ADC")
        self.adc.clicked.connect(self.adcAction)

        self.statusBox = QLabel()
        self.statusBox.setText(self.statusText())
        self.statusBox.setAlignment(QtCore.Qt.AlignCenter)

        self.connection = QPushButton('连接串口')
        self.connection.clicked.connect(self.connect)

        self.setting = QPushButton('串口设置')
        self.setting.clicked.connect(self.settingAction)

        vbox = QVBoxLayout()
        vbox.addWidget(self.adc)

        vbox.addWidget(self.spectrum)

        vbox.addWidget(self.colorMap)
        hbox = QHBoxLayout()
        # hbox.addStretch(1)
        hbox.addLayout(vbox)

        vbox2 = QVBoxLayout()
        vbox2.addStretch(1)
        vbox2.addWidget(self.statusBox)
        vbox2.addStretch(1)
        vbox2.addWidget(self.connection)
        vbox2.addWidget(self.setting)
        vbox2.addStretch(1)
        hbox.addLayout(vbox2)
        # hbox.addStretch(1)
        self.setLayout(hbox)

    def statusText(self):
        status = '当前配置\n波特率' + str(self.port.bandradte) + '\n停止位 1\nADC数据接收类型 uint8'
        return status

    def spectrumAction(self):
        if self.spectrum.isEnabled():
            # print("yes")
            self.port.spectrum_one_figure()
            # self.spectrum.setEnabled(False)

    def colorMapAction(self):    
        if self.spectrum.isEnabled():
            self.port.colormap()

    def adcAction(self):  
        self.ADC_Window = adcWindow(self.port)
        self.ADC_Window.show()
        # QtWidgets.QFileDialog.getExistingDirectory(self, "@2", "./")

    def connect(self):
        if(self.port.ser is None or self.port.ser.isOpen() is False):
            self.port.openPort()
        if(self.port.ser.isOpen()):
            QMessageBox.information(self, '提示', '连接成功', QMessageBox.Ok)
    
    def settingAction(self):
        # QMessageBox.information(self, '提示', '正在建设', QMessageBox.Ok)
        self.settings = Settings(self.port)
        self.settings.show()
    
    @staticmethod
    def refresh():
        QApplication.processEvents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MainAPP()
    sys.exit(app.exec_())
