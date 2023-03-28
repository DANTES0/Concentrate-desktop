import sys, random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Store(QWidget):
    def __init__(self):

        super().__init__()
        self.scene = QGraphicsScene()
        self.view= QGraphicsView(self.scene)

        self.mywidget = QFrame()
        self.testbutton = QPushButton(self)

        self.InitWindow()

    def InitWindow(self):
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setGeometry(0, 142, 700, 762)
        self.setFixedSize(QSize(700, 477))

        self.testbutton.setGeometry(31, 31, 146, 180)