from PyQt5 import QtWidgets


class UI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QPushButton"
                           "{"
                           "background-color: ;"
                           "}")
        self.x, self.y = 640, 360
        self.ax = self.screen().availableGeometry().width()
        self.ay = self.screen().availableGeometry().height()
        self.label = QtWidgets.QLabel(self)
        self.line = QtWidgets.QLineEdit(self)
        self.btn = QtWidgets.QPushButton(self)
        self.vLayout = QtWidgets.QVBoxLayout(self)

        self.initUI()

    def initUI(self):
        self.vLayout.addWidget(self.label)
        self.vLayout.addWidget(self.line)
        self.vLayout.addWidget(self.btn)

        self.setGeometry((self.ax - self.x) // 2, (self.ay - self.y) // 2, self.x, self.y)

        self.btn.setText("Send message")
