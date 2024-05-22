import socket
import threading


class Ophir:
    def __init__(self, ip_host: str = None, port: int = None, packet_size: int = 64):
        self.ip = ip_host
        self.port = port
        self.packet_size = packet_size

        self.full_address = (self.ip, self.port)


    def connect(self, timeout: int = 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            try:
                timer = threading.Timer(timeout, soc.close)
                soc.connect(self.full_address)
                soc.send(b'connect')
                timer.cancel()
                return 'Connected to ophir'
            except Exception as e:
                print(f'Cannot connect to ophir: {e}')
                timer.cancel()
                return f'Cannot connect to ophir: {e}'

    def get_status(self, timeout: int = 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            try:
                timer = threading.Timer(timeout, soc.close)
                soc.connect(self.full_address)
                soc.send(b'status')
                answer = soc.recv(1024)
                timer.cancel()
                return f'Ophir status {answer}'
            except Exception as e:
                print(f'Cannot connect to ophir: {e}')
                timer.cancel()
                return f'Cannot connect to ophir: {e}'

    def arm_ophir(self, shot_num, timeout: int = 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            try:
                timer = threading.Timer(timeout, soc.close)
                soc.connect(self.full_address)
                soc.send(b'arm %d %05d' % (1, shot_num))
                timer.cancel()
                return 'Ophir armed'
            except Exception as e:
                print(f'Cannot arm ophir: {e}')
                timer.cancel()
                return f'Cannot connect to ophir: {e}'

    def disarm_ophir(self, timeout: int = 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            try:
                timer = threading.Timer(timeout, soc.close)
                soc.connect(self.full_address)
                soc.send(b'disarm')
                timer.cancel()
                return 'Ophir disarmed'
            except Exception as e:
                print(f'Cannot disarm ophir: {e}')
                timer.cancel()
                return f'Cannot connect to ophir: {e}'
