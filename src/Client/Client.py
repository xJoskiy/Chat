import socket


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connectToServer()

    def connectToServer(self):
        self.client_sock.connect((self.ip, self.port))
