import sys, time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QDial, QLabel, QMessageBox, QHBoxLayout, \
    QVBoxLayout, QGridLayout, QFormLayout, QTextEdit, QLineEdit, QScrollArea
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt, QTimer


class MTimer:
    def __init__(self):
        self.initUI()

    def initUI(self):
        self.scr = QScrollArea()
        self.w = QWidget()
        self.lay = QVBoxLayout()

        # self.w.setMinimumSize(300, 1500)
        self.scr.resize(300, 150)
        # self.scr.setMaximumHeight(150)

        qbtn = QPushButton(self.w)
        qbtn.setText("start")
        qbtn.clicked.connect(self.start)
        qbtn.resize(70, 30)

        self.qtimer = QTimer()
        self.qtimer.timeout.connect(self.time)

        self.lay.addWidget(self.w)
        self.scr.setLayout(self.lay)
        self.scr.show()

    def time(self):
        self.ql = QLabel("alice", self.w)
        self.lay.addWidget(self.ql)

    def start(self):
        self.qtimer.start(500)
