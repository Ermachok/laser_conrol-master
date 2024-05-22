from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
import sys
from laser_utils import laser_gui, laser_functions
from ophir_utils.sensor import Sensor

class App(QtWidgets.QMainWindow, laser_gui.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.lcd_number)

        self.server_address = ('192.168.10.110', 4001)
        self.ArmButton.clicked.connect(self.arm_laser)
        self.DisarmButton.clicked.connect(self.disarm_laser)
        self.FireButton.clicked.connect(self.fire_laser)
        self.StopfireButton.clicked.connect(self.stop_fire_laser)

        self.timer_clock = 0

        self.ConnectOphir.clicked.connect(self.connect_ophir)
        self.StatusOphir.clicked.connect(self.status_ophir)
        self.ArmOphir.clicked.connect(self.arm_ophir)
        self.DisarmOphir.clicked.connect(self.disarm_ophir)

        self.Console.setReadOnly(True)

        self.arm_flag = 0

    def arm_laser(self):
        try:
            laser_functions.arm(self.server_address)
            self.timer_clock = 0
            self.timer.start(1000)
            self.arm_flag = True
            self.Console.append('Laser armed')
        except TimeoutError:
            self.Console.append(f'Error during arm(TimeOut)')


    def disarm_laser(self):
        if self.arm_flag:
            try:
                self.timer.stop()
                self.Clock.display('0')
                laser_functions.disarm(self.server_address)
                self.arm_flag = False
            except TimeoutError:
                self.Console.append('Some error in disarm laser(TimeOut)')
        else:
            self.Console.append('Laser are not aimed')

    def fire_laser(self):
        self.Console.append("This button doesn't work, ha-ha. Don't even try to shoot someone looser")


    def stop_fire_laser(self):
        self.Console.append("This button ALSO doesn't work, ha-ha ")
    def connect_ophir(self):
        try:
            pass
        except Exception:
            self.Console.append(f'Error ophir connection')

    def status_ophir(self):
        pass

    def arm_ophir(self):
        ...

    def disarm_ophir(self):
        ...

    def lcd_number(self):
        self.timer_clock += 1
        self.Clock.setDigitCount(2)
        self.Clock.display('%d' % self.timer_clock)




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()