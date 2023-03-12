import sys, random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *
class Timer(QMainWindow):
    def __init__(self):

        super().__init__()
        self.title = "Meow concentration"
        self.scene = QGraphicsScene()
        self.view= QGraphicsView(self.scene)
        self.setWindowIcon(QtGui.QIcon('source/cat.ico'))
        self.setStyleSheet("background-color: #E5DBE9")
        # self.FrameBtn()
        self.CreateTimer()
        self.InitWindow()
    def CreateTimer(self):
        self.start = False
        self.count = 0

        self.sliderTimer = QSlider(Qt.Horizontal, self)
        self.sliderTimer.move(70, 150)
        self.sliderTimer.setRange(0,7200)
        self.sliderTimer.valueChanged.connect(self.UpdateLabel)
        self.sliderTimer.setSingleStep(60)
        self.sliderTimer.setTickInterval(60)
        self.sliderTimer.setPageStep(60)

        self.lable = QLabel("00:00", self)
        self.lable.setFont(QtGui.QFont('Arial', 30))
        # self.lable.resize(220,220)
        self.lable.setAlignment(Qt.AlignCenter)
        self.lable.setStyleSheet("border: 3px solid black; border-radius:200px;")
        # self.lable.move(250, 300)
        self.lable.setGeometry(146,156,407,407)
        self.lable.setAlignment(Qt.AlignBottom)
        self.lable.setAlignment(Qt.AlignHCenter)
        # self.lable.setText(str(self.sliderTimer.value()))

        self.start_btn = QPushButton("Start", self)
        self.start_btn.move(70, 250)
        self.start_btn.clicked.connect(self.start_action)
        # self.start_btn.resize(150, 150)
        self.start_btn.setStyleSheet("border: 2px solid black;border-radius: 15%;")

        self.stop_btn = QPushButton("Stop", self)
        self.stop_btn.move(70, 250)
        self.stop_btn.clicked.connect(self.stop_action)
        self.stop_btn.setVisible(False)

        self.timer = QTimer(self)
        self.time = QTime(0,0,0)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
    def showTime(self):
        if self.start:
            self.count -= 1
            m, s = divmod(self.count, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m,s)
            self.lable.setText(str(min_sec_format))
            if self.count == 0:
                self.lable.setText("00:00")
                self.start = False
    def start_action(self):
        self.start_btn.setVisible(False)
        self.stop_btn.setVisible(True)
        self.start = True
        print(self.start)
        print(self.count)
        if self.count == 0:
            self.start = False
    def stop_action(self):
        self.start = False
        self.count = 0
        self.stop_btn.setVisible(False)
        self.start_btn.setVisible(True)
        self.sliderTimer.setValue(0)
        # self.label.setText("00:00")
    def UpdateLabel(self,value):
        self.count = value
        m, s = divmod(self.count, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        self.lable.setText(str(min_sec_format))
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(650,50,700,762)
        self.setFixedSize(QSize(700,762))
        # self.show()
    # def FrameBtn(self):
    #     frame = QFrame(self)
    #     frame.setFrameShape(QFrame.NoFrame)
    #     frame.setGeometry(0,0,700,88)
    #     frame.setStyleSheet("background-color:#D8B5E9;")
    #     TimerBtn = QPushButton('Timer',self)
    #     TimerBtn.setGeometry(51,24,127,50)
    #     TimerBtn.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
    #     TaskButton = QPushButton('Task',self)
    #     TaskButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
    #     TaskButton.setGeometry(208,24,127,50)
    #     StatisticsButton = QPushButton('Statistics',self)
    #     StatisticsButton.clicked.connect(self.gotoStats)
    #     StatisticsButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
    #     StatisticsButton.setGeometry(365, 24, 127, 50)
    #     CatRoomButton = QPushButton('Cat room',self)
    #     CatRoomButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
    #     CatRoomButton.setGeometry(522,24,127,50)
    def gotoStats(self):
        print("123")
        # statistics = stats_class.Statistics()
        # main.widget.addWidget(statistics)
        # widget.setCurrentIndex(widget.currentIndex()+1)