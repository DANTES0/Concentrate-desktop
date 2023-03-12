import sys, random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *
from stats_class import Statistics
from timer_class import Timer

class widgets(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QtWidgets.QStackedWidget()
        timer = Timer()
        stats = Statistics()
        widget.addWidget(timer)
        widget.addWidget(stats)
        self.FrameBtn()

    def FrameBtn(self):
        frame = QFrame(self)
        # frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setGeometry(0,0,700,88)
        frame.setStyleSheet("background-color:#D8B5E9;")
        TimerBtn = QPushButton('Timer',self)
        TimerBtn.clicked.connect(self.gotoTimer)
        TimerBtn.setGeometry(51,24,127,50)
        TimerBtn.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
        TaskButton = QPushButton('Task',self)
        TaskButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
        TaskButton.setGeometry(208,24,127,50)
        StatisticsButton = QPushButton('Statistics',self)
        StatisticsButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
        StatisticsButton.setGeometry(365, 24, 127, 50)
        CatRoomButton = QPushButton('Cat room',self)
        CatRoomButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
        CatRoomButton.setGeometry(522,24,127,50)

app = QtWidgets.QApplication(sys.argv)
# global widget
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle("Meow concentration")
widget.setWindowIcon(QtGui.QIcon('source/cat.ico'))
widget.setGeometry(650,50,700,850)
timer = Timer()
stats = Statistics()
widget.addWidget(timer)
widget.addWidget(stats)
# widget.show()
def switch_page_stat():
    stats = Statistics()
    widget.addWidget(stats)
    widget.setCurrentIndex(widget.currentIndex()+1)

def switch_page_timer():
    timer = Timer()
    widget.addWidget(timer)
    widget.setCurrentIndex(widget.currentIndex()-1)

try:
    sys.exit(app.exec_())
except:
    print("Exiting")