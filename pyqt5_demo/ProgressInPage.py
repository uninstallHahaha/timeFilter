from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QBasicTimer
import sys


class ProgressInPage(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(600, 480)
        self.setWindowTitle('title')

        self.pb1 = QProgressBar(self)
        self.pb2 = QProgressBar(self)

        self.pb1.setFormat("%v")
        self.pb2.setInvertedAppearance(True)

        self.b1 = QPushButton('内圈跑进度', self)

        self.pb1.move(50, 50)
        self.pb2.move(50, 100)
        self.b1.move(50, 150)

        self.show()

        self.timer = QBasicTimer()
        self.step = 0

        self.b1.clicked.connect(self.doaction)

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            QMessageBox.information(self, '提示', '内圈收工了!')
            self.b1.setText('再来一次')
            self.step = 0
            return

        self.step = self.step + 1
        self.pb1.setValue(self.step)
        self.pb2.setValue(self.step)

    def doaction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.b1.setText('继续')
        else:
            self.timer.start(100, self)
            self.b1.setText('停止')
