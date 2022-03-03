import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QDial, QLabel, QMessageBox, QHBoxLayout, \
    QVBoxLayout, QGridLayout, QFormLayout, QTextEdit, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt


class Content:
    def __init__(self):
        self.initUI()

    def initUI(self):
        hlay = QHBoxLayout()

        bt2 = QPushButton('btn2', hlay)
        bt1 = QPushButton('btn1', hlay)
        bt3 = QPushButton('btn3', hlay)

        # hlay.addStretch(1)
        hlay.addWidget(bt1)
        hlay.addWidget(bt2)
        hlay.addWidget(bt3)

        vlay = QVBoxLayout()
        vlay.addLayout(hlay)
        # add a element is auto stretch to full remain space
        vlay.addStretch(1)

        self.element = vlay
