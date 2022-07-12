import sys

from PyQt5.QtWidgets import QApplication
import threading
from Client import *
from UI import *


class App(QApplication):
    def __init__(self):
        super(QApplication, self).__init__(sys.argv)
        self.client = Client('192.168.0.14', 2000)
        self.ui = UI()
        self.ui.show()
        self.ui.btn.clicked.connect(self.sendMsg)
        threading.Thread(target=self.recvMsg).start()

    def sendMsg(self):
        self.client.client_sock.send((msg := self.ui.line.text()).encode('utf-8'))
        self.ui.label.setText(f"{self.ui.label.text()}\n{msg}")
        self.ui.line.setText('')
        self.ui.line.setFocus()

    def recvMsg(self):
        while True:
            msg = self.client.client_sock.recv(1024).decode('utf-8')
            self.ui.label.setText(f"{self.ui.label.text()}\n{msg}")


