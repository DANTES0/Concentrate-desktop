import sys, random, sqlite3
import  datetime, os.path
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *

class Task(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Meow concentration"
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.setWindowIcon(QtGui.QIcon('source/cat.ico'))
        self.setStyleSheet("background-color: #E5DBE9")
        self.add_task()
        self.cat()
        self.InitWindow()
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(650,50,700,762)
        self.setFixedSize(QSize(700,762))
    def add_task(self):
        self.labelTask = QLineEdit(self)
        self.labelTask.setGeometry(51, 209, 598, 50)
        self.labelTask.setStyleSheet("background: #ffffff; border-radius: 25px;")

        self.labelPlus = QPushButton(self)
        self.labelPlus.setGeometry(61, 218, 29, 29)
        self.labelPlus.setStyleSheet("background: #F6F0B7; border-radius: 14px;")
        pixmap = QPixmap('source/plus.png')
        Icon = QIcon(pixmap)
        self.labelPlus.setIcon(Icon)

    def cat(self):
        self.labelCat = QLabel(self)
        pixmap = QPixmap('source/TaskCat.png')
        self.labelCat.setPixmap(pixmap)
        self.labelCat.setGeometry(213, 0, 254, 208)
