from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu, QMessageBox, QHBoxLayout, QPushButton, \
    QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon

from pyqt5_demo.components.content import Content


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        # main_layout = QHBoxLayout()
        main_layout = QHBoxLayout()
        left_part = QHBoxLayout()
        mid_button = QVBoxLayout()
        right_part = QHBoxLayout()

        # left
        bt1 = QPushButton('btn1', self)
        bt2 = QPushButton('btn2', self)
        bt3 = QPushButton('btn3', self)
        left_part.addWidget(bt1)
        left_part.addWidget(bt2)
        left_part.addWidget(bt3)

        # mid
        arrow = QLabel()
        arrow.setText(">")
        mid_button.addWidget(arrow)


        # right
        log_part = QVBoxLayout()
        log_error_part = QVBoxLayout()
        right_part.addLayout(log_part)
        right_part.addLayout(log_error_part)

        # main_layout.addStretch(1)
        main_layout.addLayout(left_part)
        main_layout.addLayout(mid_button)
        main_layout.addLayout(right_part)

        # main content
        main_content = QWidget()
        main_content.setLayout(main_layout)

        # set center
        self.setCentralWidget(main_content)

        self.statusBar().showMessage('准备就绪')

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('standar window')

        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)

        saveMenu = QMenu('保存方式(&S)', self)
        saveAct = QAction(QIcon('save.png'), '保存...', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('保存文件')

        saveasAct = QAction(QIcon('Save.png'), '另存为...(&O)', self)
        saveasAct.setStatusTip('文件另存为')
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)

        newAct = QAction(QIcon('File.png'), '新建(&N)', self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('新建文件')
        newAct.triggered.connect(self.newFile)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('工具栏')
        toolbar.addAction(newAct)
        toolbar.addAction(exitAct)

        self.appendLb(log_part)

        self.show()

    def newFile(self):
        QMessageBox.about(self, 'tip', 'new file...')

    def appendLb(self, content):
        
        content.addWidget()
