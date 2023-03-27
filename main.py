import sys, random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *
from stats_class import Statistics
from timer_class import Timer
from catRoom_class import CatRoom

class widgets(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.FrameBtn()
        self.widget = QtWidgets.QStackedWidget(self)
        self.widget.setGeometry(0, 88, 700, 762)
        self.timer = Timer()
        self.stats = Statistics()
        self.catRoom = CatRoom()
        self.widget.addWidget(self.timer)
        self.widget.addWidget(self.stats)
        self.widget.addWidget(self.catRoom)
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle("Meow concentration")
        self.setWindowIcon(QtGui.QIcon("source/cat.ico"))
        self.setGeometry(650, 50, 700, 850)
        self.setFixedSize(QSize(700, 850))
        self.show()
    def FrameBtn(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setGeometry(0,0,700,88)
        frame.setStyleSheet("background-color:#D8B5E9;")
        TimerBtn = QPushButton('Timer',self)
        TimerBtn.setGeometry(51,24,127,50)
        TimerBtn.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
        TimerBtn.clicked.connect(self.gotoTimer)
        TaskButton = QPushButton('Task',self)
        TaskButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
        TaskButton.setGeometry(208,24,127,50)
        StatisticsButton = QPushButton('Statistics',self)
        StatisticsButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
        StatisticsButton.setGeometry(365, 24, 127, 50)
        StatisticsButton.clicked.connect(self.gotoStats)
        CatRoomButton = QPushButton('Cat room',self)
        CatRoomButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
        CatRoomButton.setGeometry(522,24,127,50)
        CatRoomButton.clicked.connect(self.gotoCatRoom)

    def gotoTimer(self):
        self.timer = Timer()
        self.widget.addWidget(self.timer)
        self.widget.setCurrentIndex(0)
    def gotoStats(self):
        print(self.widget.currentIndex())
        self.stats = Statistics()
        self.widget.addWidget(self.stats)
        self.widget.setCurrentIndex(1)
    def gotoCatRoom(self):
        print(self.widget.currentIndex())
        self.catRoom = CatRoom()
        self.widget.addWidget(self.catRoom)
        self.widget.setCurrentIndex(2)

app = QtWidgets.QApplication(sys.argv)
window = widgets()
sys.exit(app.exec_())
