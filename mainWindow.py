import sys
 
#这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy

from PyQt5.QtGui import QIcon

class MainAPP(QWidget):
    def __init__(self):
        super().__init__()
        # draw UI
        self.initUI()

    def initUI(self):
        # size and location
        # self.setGeometry(500, 500, 500, 500)
        self.resize(500, 400)
        self.center()

        self.setWindowTitle("UART")

        self.setWindowIcon(QIcon("icon.png"))

        self.button()

        self.show()

    def center(self):
        window = self.frameGeometry()
        # 获取中心点
        centerPoint =  QDesktopWidget().availableGeometry().center()
        window.moveCenter(centerPoint)
        # self.move(window.topLeft())
    
    def button(self):
        self.spectrum = QPushButton("Spectrum")
        self.spectrum.clicked.connect(self.spectrumAction)
        # self.spectrum.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        
        self.colorMap = QPushButton("ColorMap")
        self.colorMap.clicked.connect(self.colorMapAction)
        # self.colorMap.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        vbox = QVBoxLayout()

        vbox.addWidget(self.spectrum)

        vbox.addWidget(self.colorMap)


        hbox = QHBoxLayout()
        # hbox.addStretch(1)
        hbox.addLayout(vbox)
        # hbox.addStretch(1)
        self.setLayout(hbox)

    def spectrumAction(self):
        if self.spectrum.isEnabled():
            print("yes")
            # self.spectrum.setEnabled(False)

    def colorMapAction(self):
        if self.spectrum.isEnabled():
            print("colorMap")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    a = MainAPP()
    sys.exit(app.exec_())