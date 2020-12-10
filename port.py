from os import times
from PyQt5.QtWidgets import QMessageBox
import serial
import serial.tools.list_ports
import numpy as np
import matplotlib.pyplot as plt


class Port():
    def __init__(self):

        self.port_lists = serial.tools.list_ports.comports()

        # TTL转USB端口名
        self.ttl_to_usb = "CH340"

        self.sample = 12500 / 1.66
        self.data_size = 256
        self.bandradte = 2962962
        self.ser = None
        

    # 打开串口
    def openPort(self):
        uart_port = None
        for i in self.port_lists:
            # print(i.description)
            if(self.ttl_to_usb in i.description):
                uart_port = i.name
                break

        if uart_port is not None:
            self.ser = serial.Serial(uart_port, self.bandradte, timeout=0.8, stopbits=serial.STOPBITS_ONE,
                                 parity=serial.PARITY_EVEN, bytesize=serial.EIGHTBITS)
            return True
        else:
            return False

    # 用来对齐数据
    def align(self):
        while True:
            # print('A' in str(ser.readline()))
            if('Start' in str(self.ser.readline())):
                break

    def fetchDataElement(self):
        if(self.ser.isOpen() is False):
            self.openPort()

        data = np.array([])


        # times.sleep(0.01)
        self.align()
        for i in range(0, self.data_size):
            data = np.append(data, float(self.ser.readline()[0:-2]))
            # print(ser.readline())

        return data

    def fetchDataElement_uint8(self, dataSize=1000):
        if(self.ser.isOpen() is False):
            self.openPort()
        # self.ser.flush()
        # self.ser.reset_output_buffer()
        self.ser.reset_input_buffer()
        # self.align()
        data = []
        for i in range(0, dataSize):
            data.append(int.from_bytes(self.ser.read(size=1), byteorder='big', signed=False))
            # print(data[-1])
        return data
        

    def spectrum_one_figure(self):
        data = self.fetchDataElement()
        fren_x = np.linspace(0, self.sample / 2, self.data_size)
        plt.figure()
        plt.plot(fren_x[1:], data[1:], linewidth=0.3)
        plt.show()

    def colormap(self):
        data_map = np.array([self.fetchDataElement()]).T
        for i in range(20):
            data_map = np.append(data_map, np.array(
                [self.fetchDataElement()]).T, axis=1)
        plt.figure()
        # print(data_map.shape)
        plt.imshow(data_map[1:, :], aspect='auto', interpolation='none',
                   extent=[0, 1, 0, 1], origin='lower')
        plt.colorbar()
        plt.show()


    # port = serial.Serial("c")
if __name__ == '__main__':
    # Port().spectrum_one_figure()
    Port().colormap()
