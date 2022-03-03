from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QMenu, QLabel, QLineEdit, QMessageBox, QProgressDialog)
from PyQt5.QtCore import Qt, QTimer


class Button(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('title')
        self.setGeometry(300, 300, 300, 200)

        bt1 = QPushButton("这是什么", self)
        self.bt2 = QPushButton('发送验证码', self)
        bt1.resize(70, 30)
        bt1.move(50, 50)
        self.bt2.resize(70, 30)
        self.bt2.move(50, 100)

        menu = QMenu(self)
        menu.addAction('我是')
        menu.addSeparator()
        menu.addAction('世界上')
        menu.addSeparator()
        menu.addAction('最帅的')
        bt1.setMenu(menu)

        self.count = 10

        self.bt2.clicked.connect(self.Action)

        self.time = QTimer(self)
        self.time.setInterval(1000)
        self.time.timeout.connect(self.Refresh)

        self.show()

    def Action(self):
        if self.bt2.isEnabled():
            self.time.start()
            self.bt2.setEnabled(False)

    def Refresh(self):
        if self.count > 0:
            self.bt2.setText(str(self.count) + '秒后重发')
            self.count -= 1
        else:
            self.time.stop()
            self.bt2.setEnabled(True)
            self.bt2.setText('发送验证码')
            self.count = 10
