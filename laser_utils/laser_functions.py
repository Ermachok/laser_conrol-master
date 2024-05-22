import socket
import threading
#server_address = ('192.168.10.110', 4001)


def arm(server_address, timeout:int = 3):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    timer = threading.Timer(timeout, sock.close)
    try:
        timer.start()
        sock.connect(server_address)
        sock.send(b'\x23\x03\x53\x00\x79')  # idling on
        print('sent idling on')
        answer_serv = sock.recv(1024)
        print(answer_serv)

        sock.send(b'\x23\x03\x43\x00\x69')  # start
        print('sent start')
        answer_serv = sock.recv(1024)
        print(answer_serv)
        sock.close()
        timer.cancel()
        return True
    except Exception:
        print('Cannot connect to laser')
        timer.cancel()
        raise TimeoutError

def disarm(server_address, timeout:int = 3):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    timer = threading.Timer(timeout, sock.close)
    try:
        sock.connect(server_address)

        sock.send(b'\x23\x03\x44\x00\x70')  # stop
        print('sent stop')
        answer_serv = sock.recv(1024)
        print(answer_serv)

        sock.send(b'\x23\x03\x73\x00\x99')  # idling off
        print('sent idling off')
        answer_serv = sock.recv(1024)
        print(answer_serv)
        sock.close()
        timer.cancel()
        return True
    except Exception:
        print('Cannot disarm laser!!! WHAT DO YOU DO NOW?')
        raise TimeoutError

def fire(server_address):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)

    sock.send(b'\x23\x03\x42\x00\x68')  # laser generator on
    print('fire')
    answer_serv = sock.recv(1024)
    print(answer_serv)

    sock.close()


def fire_stop(server_address):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)

    sock.send(b'\x23\x03\x62\x00\x88')  # laser generator off
    print('stop fire')
    answer_serv = sock.recv(1024)
    print(answer_serv)
    sock.close()

