import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QDial, QLabel, QMessageBox, QHBoxLayout, \
    QVBoxLayout, QGridLayout, QFormLayout, QTextEdit, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt

from pyqt5_demo.Button import Button
from pyqt5_demo.Progress import Progress
from pyqt5_demo.ProgressInPage import ProgressInPage
from pyqt5_demo.StandarWindow import StandarWindow
from pyqt5_demo.Form import Form
from pyqt5_demo.StandardInputDialog import StandardID
from pyqt5_demo.TimerDemo import MTimer
from pyqt5_demo.UtilInputDialog import UtilInputDialog
from pyqt5_demo.components.main import Main


class ShowBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('title')
        btn = QPushButton('show', self)
        btn.clicked.connect(self.showBox)
        btn.resize(50, 25)
        btn.move(50, 50)
        self.show()

    def showBox(self):
        QMessageBox.about(self, 'message', 'this is your message')


class KeyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('学点编程吧')

        self.lab = QLabel('方向', self)
        self.lab.setGeometry(150, 100, 50, 50)

        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.lab.setText('↑')
        elif e.key() == Qt.Key_Down:
            self.lab.setText('↓')
        elif e.key() == Qt.Key_Left:
            self.lab.setText('←')
        else:
            self.lab.setText('→')


class MyLCD(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('学点编程吧')

        lcd.setGeometry(100, 50, 150, 60)
        dial.setGeometry(120, 120, 100, 100)

        dial.valueChanged.connect(lcd.display)

        self.show()


class QuitBtn(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('title')
        self.setWindowIcon(QIcon('icon.ico'))

        qbtn = QPushButton('退出', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(70, 30)
        qbtn.move(50, 50)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = MTimer()

    sys.exit(app.exec_())
