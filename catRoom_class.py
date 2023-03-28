import sys, random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CatRoom(QMainWindow):
    def __init__(self):
        super().__init__()  # super() lets you avoid referring to the base class explicitly
        self.title = "Meow concentration"
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.setWindowIcon(QtGui.QIcon('source/cat.ico'))
        self.setStyleSheet("background-image: url(source/CatRoomBg.png);")  # background-color: #FFFFF;
        #self.setAttribute(Qt.WA_TranslucentBackground)
        #self.setWindowOpacity(0.6)
        self.prevSender = None
        # self.setCentralWidget(self.storeButton)
        self.init_Ui()
        self.InitWindow()
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(650, 50, 700, 762)
        self.setFixedSize(QSize(700, 762))

    def storeButton_load_store(self):
        print("'Enter Store' button clicked!")
        self.storeButton_load.hide()
        self.load_store()

    def storeButton_exit_store(self):
        print("'Exit Store' button clicked!")
        self.mywidget.close()
        self.bg.close()
        self.mywidget.button_1.close()
        self.mywidget.button_2.close()
        self.mywidget.button_3.close()
        self.mywidget.button_4.close()
        self.mywidget.button_5.close()
        self.mywidget.button_6.close()
        self.mywidget.button_7.close()
        self.mywidget.button_8.close()
        self.storeButton_load.show()
        self.mywidget.storeButton_exit.hide()
    def init_Ui(self):
        self.storeButton_load = QPushButton(self)
        self.storeButton_load.setGeometry(559, 8, 41, 41)
        self.storeButton_load.setStyleSheet("background:#8350AA; border-radius: 10px;")
        self.storeButton_load.setIcon(QIcon('source/Vector.svg'))

        self.storeButton_load.clicked.connect(self.storeButton_load_store)
    def load_store(self):
        self.mywidget = QFrame()

        #  фон магазина
        self.bg = QFrame()
        self.bg.setGeometry(0, 0, 700, 762)
        self.bg.setFixedSize(QSize(700, 762))
        self.bg.setStyleSheet("background:#000000; background: rgba(0, 0, 0, 0.6);")
        self.bg.setParent(self)
        self.bg.show()

        self.mywidget.storeButton_exit = QPushButton(self)
        self.mywidget.storeButton_exit.setGeometry(559, 8, 41, 41)
        self.mywidget.storeButton_exit.setStyleSheet("background:#8350AA; border-radius: 10px;")
        self.mywidget.storeButton_exit.setIcon(QIcon('source/Vector.svg'))

        self.mywidget.storeButton_exit.clicked.connect(self.storeButton_exit_store)
        self.mywidget.storeButton_exit.show()

        self.mywidget.setGeometry(0, 142, 700, 762)
        self.mywidget.setFixedSize(QSize(700, 477))
        self.mywidget.setParent(self)
        self.mywidget.setStyleSheet("background:#D9D9D9; border-radius: 60px;")
        self.mywidget.show()

        #кнопка 1
        self.mywidget.button_1 = QPushButton(self)
        self.mywidget.button_1.setGeometry(31, 173, 146, 180)
        self.mywidget.button_1.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_1.show()

        #кнопка 2
        self.mywidget.button_2 = QPushButton(self)
        self.mywidget.button_2.setGeometry(195, 173, 146, 180)
        self.mywidget.button_2.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_2.show()

        #кнопка 3
        self.mywidget.button_3 = QPushButton(self)
        self.mywidget.button_3.setGeometry(359, 173, 146, 180)
        self.mywidget.button_3.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_3.show()

        # кнопка 4
        self.mywidget.button_4 = QPushButton(self)
        self.mywidget.button_4.setGeometry(359, 173, 146, 180)
        self.mywidget.button_4.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_4.show()

        # кнопка 5
        self.mywidget.button_5 = QPushButton(self)
        self.mywidget.button_5.setGeometry(359, 173, 146, 180)
        self.mywidget.button_5.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_5.show()

        # кнопка 6
        self.mywidget.button_6 = QPushButton(self)
        self.mywidget.button_6.setGeometry(359, 173, 146, 180)
        self.mywidget.button_6.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_6.show()

        # кнопка 7
        self.mywidget.button_7 = QPushButton(self)
        self.mywidget.button_7.setGeometry(359, 173, 146, 180)
        self.mywidget.button_7.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_7.show()

        # кнопка 6
        self.mywidget.button_8 = QPushButton(self)
        self.mywidget.button_8.setGeometry(359, 173, 146, 180)
        self.mywidget.button_8.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_8.show()