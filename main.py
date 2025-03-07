import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
import sys
import logging
from laser_utils import laser_gui, laser_functions

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
        self.arm_flag = False

        self.Console.setReadOnly(True)

    def arm_laser(self):
        try:
            laser_functions.arm(server_address=self.server_address)
            self.arm_flag = True
            time.sleep(2)
            laser_functions.start(server_address=self.server_address)

            self.timer_clock = 0
            self.timer.start(1000)

            self.Console.append('Laser armed')

            logger.info('Laser armed successfully')

        except TimeoutError as e:
            self.Console.append(f'Error during arm: {e}')
            logger.error(f'Error during arm: {e}')

    def disarm_laser(self):
        if self.arm_flag:
            try:
                self.timer.stop()
                self.Clock.display('0')

                laser_functions.stop(server_address=self.server_address)
                time.sleep(2)
                laser_functions.disarm(server_address=self.server_address)

                self.arm_flag = False
                self.Console.append('Laser disarmed')
                logger.info('Laser disarmed successfully')
            except TimeoutError as e:
                self.Console.append(f'Error during disarm: {e}')
                logger.error(f'Error during disarm: {e}')
        else:
            self.Console.append('Laser is not armed')
            logger.warning('Attempt to disarm unarmed laser')

    def fire_laser(self):
        laser_functions.fire(server_address=self.server_address)
        self.Console.append("Fire button pressed")

    def stop_fire_laser(self):
        laser_functions.fire_stop(server_address=self.server_address)
        self.Console.append("Stop fire button pressed")

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
