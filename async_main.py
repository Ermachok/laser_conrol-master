import sys
import asyncio
import logging
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from qasync import QEventLoop, asyncSlot
from laser_utils import laser_gui, laser_functions_async


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

    @asyncSlot()
    async def arm_laser(self):
        try:
            await laser_functions_async.arm(self.server_address)
            self.timer_clock = 0
            self.timer.start(1000)
            self.arm_flag = True
            self.Console.append('Laser armed')
            logger.info('Laser armed successfully')
        except TimeoutError as e:
            self.Console.append(f'Error during arm: {e}')
            logger.error(f'Error during arm: {e}')
        except Exception as e:
            self.Console.append(f'Error during arm: {e}')

    @asyncSlot()
    async def disarm_laser(self):
        if self.arm_flag:
            try:
                self.timer.stop()
                self.Clock.display('0')
                await laser_functions_async.disarm(self.server_address)
                self.arm_flag = False
                self.Console.append('Laser disarmed')
                logger.info('Laser disarmed successfully')
            except TimeoutError as e:
                self.Console.append(f'Error during disarm: {e}')
                logger.error(f'Error during disarm: {e}')
        else:
            self.Console.append('Laser is not armed')
            logger.warning('Attempt to disarm unarmed laser')

    @asyncSlot()
    async def fire_laser(self):
        self.Console.append("This button doesn't work, ha-ha. Don't even try to shoot someone, loser")
        logger.warning("Fire button pressed, but it's not functional")

    @asyncSlot()
    async def stop_fire_laser(self):
        self.Console.append("This button ALSO doesn't work, ha-ha")
        logger.warning("Stop fire button pressed, but it's not functional")

    def lcd_number(self):
        self.timer_clock += 1
        self.Clock.setDigitCount(2)
        self.Clock.display('%d' % self.timer_clock)

def main():
    app = QtWidgets.QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = App()
    window.show()

    with loop:
        loop.run_forever()

if __name__ == '__main__':
    main()