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
        self.prevSender = None
        # self.setCentralWidget(self.storeButton)
        self.init_Ui()
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(650, 50, 700, 762)
        self.setFixedSize(QSize(700, 762))

    def store_button_was_clicked(self):
        print("Store button clicked!")

    def store_button_was_toggled(self, checked):
        print(checked)

    def init_Ui(self):
        self.storeButton = QPushButton(self)
        self.storeButton.setGeometry(559, 8, 41, 41)
        self.storeButton.setStyleSheet("background:#8350AA; border-radius: 10px;")
        self.storeButton.setIcon(QIcon('source/store_icon.svg'))

        self.storeButton.setCheckable(True)
        self.storeButton.clicked.connect(self.store_button_was_clicked)
        self.storeButton.clicked.connect(
            self.store_button_was_toggled)  # if Store is opened, set TRUE value; if Store is closed, set FALSE value