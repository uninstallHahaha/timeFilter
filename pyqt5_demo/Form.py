from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QDial, QLabel, QMessageBox, QHBoxLayout, \
    QVBoxLayout, QGridLayout, QFormLayout, QTextEdit, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt

class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()

    def Init_UI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('学点编程吧')

        formlayout = QFormLayout()
        nameLabel = QLabel("姓名")
        nameLineEdit = QLineEdit("")
        introductionLabel = QLabel("简介")
        introductionLineEdit = QTextEdit("")

        formlayout.addRow(nameLabel, nameLineEdit)
        formlayout.addRow(introductionLabel, introductionLineEdit)
        self.setLayout(formlayout)

        self.show()