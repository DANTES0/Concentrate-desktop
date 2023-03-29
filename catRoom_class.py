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
        self.setStyleSheet("background-image: url(source/CatRoomBg.png);")
        self.prevSender = None
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
        #  закрытие всех виджетов магазина
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
        self.mywidget.shadow_1.close()
        self.mywidget.shadow_2.close()
        self.mywidget.shadow_3.close()
        self.mywidget.shadow_4.close()
        self.mywidget.shadow_5.close()
        self.mywidget.shadow_6.close()
        self.mywidget.shadow_7.close()
        self.mywidget.shadow_8.close()
        self.storeButton_load.show()
        self.mywidget.storeButton_exit.hide()
    def init_Ui(self):
        #  ининициализация кнопки для входа в магазин
        self.storeButton_load = QPushButton(self)
        self.storeButton_load.setGeometry(559, 8, 41, 41)
        self.storeButton_load.setStyleSheet("background:#8350AA; border-radius: 10px;")
        self.storeButton_load.setIcon(QIcon('source/store_icon.svg'))

        self.storeButton_load.clicked.connect(self.storeButton_load_store)
    def load_store(self):
        #  фрейм серого фона для магазина
        self.mywidget = QFrame()

        #  тёмный прозрачный фон магазина
        self.bg = QFrame()
        self.bg.setGeometry(0, 0, 700, 762)
        self.bg.setFixedSize(QSize(700, 762))
        self.bg.setStyleSheet("background:#000000; background: rgba(0, 0, 0, 0.6);")
        self.bg.setParent(self)
        self.bg.show()

        #  кнопка магазина
        self.mywidget.storeButton_exit = QPushButton(self)
        self.mywidget.storeButton_exit.setGeometry(559, 8, 41, 41)
        self.mywidget.storeButton_exit.setStyleSheet("background:#8350AA; border-radius: 10px;")
        self.mywidget.storeButton_exit.setIcon(QIcon('source/store_icon.svg'))

        self.mywidget.storeButton_exit.clicked.connect(self.storeButton_exit_store)
        self.mywidget.storeButton_exit.show()

        #  серый фон магазина
        self.mywidget.setGeometry(83, 60, 700, 762)
        self.mywidget.setFixedSize(QSize(534, 667))
        self.mywidget.setParent(self)
        self.mywidget.setStyleSheet("background:#D9D9D9; border-radius: 60px;")
        self.mywidget.show()

        #  тень кнопки 1
        self.mywidget.shadow_1 = QLabel()
        self.mywidget.shadow_1.setGeometry(116, 105, 152, 180)
        self.mywidget.shadow_1.setParent(self)
        self.mywidget.shadow_1.setStyleSheet("background:#455D81; border-radius: 30px;")
        self.mywidget.shadow_1.show()

        #  кнопка 1
        self.mywidget.button_1 = QPushButton(self)
        self.mywidget.button_1.setGeometry(113, 96, 146, 180)
        self.mywidget.button_1.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_1.show()

        #  тень кнопки 2
        self.mywidget.shadow_2 = QLabel()
        self.mywidget.shadow_2.setGeometry(280, 105, 152, 180)
        self.mywidget.shadow_2.setParent(self)
        self.mywidget.shadow_2.setStyleSheet("background:#455D81; border-radius: 30px;")
        self.mywidget.shadow_2.show()

        #  кнопка 2
        self.mywidget.button_2 = QPushButton(self)
        self.mywidget.button_2.setGeometry(277, 96, 146, 180)
        self.mywidget.button_2.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_2.show()

        #  тень кнопки 3
        self.mywidget.shadow_3 = QLabel()
        self.mywidget.shadow_3.setGeometry(444, 105, 152, 180)
        self.mywidget.shadow_3.setParent(self)
        self.mywidget.shadow_3.setStyleSheet("background:#455D81; border-radius: 30px;")
        self.mywidget.shadow_3.show()

        #  кнопка 3
        self.mywidget.button_3 = QPushButton(self)
        self.mywidget.button_3.setGeometry(441, 96, 146, 180)
        self.mywidget.button_3.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_3.show()

        #  тень кнопки 4
        self.mywidget.shadow_4 = QLabel()
        self.mywidget.shadow_4.setGeometry(116, 311, 152, 180)
        self.mywidget.shadow_4.setParent(self)
        self.mywidget.shadow_4.setStyleSheet("background:#455D81; border-radius: 30px;")
        self.mywidget.shadow_4.show()

        #  кнопка 4
        self.mywidget.button_4 = QPushButton(self)
        self.mywidget.button_4.setGeometry(113, 304, 146, 180)
        self.mywidget.button_4.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_4.show()

        #  тень кнопки 5
        self.mywidget.shadow_5 = QLabel()
        self.mywidget.shadow_5.setGeometry(280, 311, 152, 180)
        self.mywidget.shadow_5.setParent(self)
        self.mywidget.shadow_5.setStyleSheet("background:#814545; border-radius: 30px;")
        self.mywidget.shadow_5.show()

        # кнопка 5
        self.mywidget.button_5 = QPushButton(self)
        self.mywidget.button_5.setGeometry(277, 304, 146, 180)
        self.mywidget.button_5.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_5.show()

        #  тень кнопки 6
        self.mywidget.shadow_6 = QLabel()
        self.mywidget.shadow_6.setGeometry(444, 311, 152, 180)
        self.mywidget.shadow_6.setParent(self)
        self.mywidget.shadow_6.setStyleSheet("background:#814545; border-radius: 30px;")
        self.mywidget.shadow_6.show()

        #  кнопка 6
        self.mywidget.button_6 = QPushButton(self)
        self.mywidget.button_6.setGeometry(441, 304, 146, 180)
        self.mywidget.button_6.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_6.show()

        #  тень кнопки 7
        self.mywidget.shadow_7 = QLabel()
        self.mywidget.shadow_7.setGeometry(193, 521, 152, 180)
        self.mywidget.shadow_7.setParent(self)
        self.mywidget.shadow_7.setStyleSheet("background:#814545; border-radius: 30px;")
        self.mywidget.shadow_7.show()

        #  кнопка 7
        self.mywidget.button_7 = QPushButton(self)
        self.mywidget.button_7.setGeometry(190, 512, 146, 180)
        self.mywidget.button_7.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_7.show()

        #  тень кнопки 8
        self.mywidget.shadow_8 = QLabel()
        self.mywidget.shadow_8.setGeometry(357, 521, 152, 180)
        self.mywidget.shadow_8.setParent(self)
        self.mywidget.shadow_8.setStyleSheet("background:#814545; border-radius: 30px;")
        self.mywidget.shadow_8.show()

        #  кнопка 8
        self.mywidget.button_8 = QPushButton(self)
        self.mywidget.button_8.setGeometry(354, 512, 146, 180)
        self.mywidget.button_8.setStyleSheet("background:#FFFFFF; border-radius: 30px")
        self.mywidget.button_8.show()
