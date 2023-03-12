import sys, random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *

class Statistics(QMainWindow):
    def __init__(self):

        super().__init__()
        self.title = "Meow concentration"
        self.scene = QGraphicsScene()
        self.view= QGraphicsView(self.scene)
        self.setWindowIcon(QtGui.QIcon('source/cat.ico'))
        self.setStyleSheet("background-color: #E5DBE9")
        self.prevSender = None

        self.Graph()
        self.create_donutchart()
        self.BackLabel()
        self.FrameWeek()
        self.InitWindow()
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(650,50,700,762)
        self.setFixedSize(QSize(700,762))
    def BackLabel(self):
        self.backLabel = QLabel("White", self)
        pixmap = QPixmap('source/Cat_1.png')
        self.backLabel.setPixmap(pixmap)
        self.backLabel.setStyleSheet("background-color: transparent")
        self.backLabel.setGeometry(387,520,100,100)

        ConcentrationLabel = QLabel("Concentration time", self)
        ConcentrationLabel.setGeometry(83,13,227,29)
        ConcentrationLabel.setStyleSheet("background-color: transparent; font: bold 24px; font-family: Inter; color: #29002F")
    def Graph(self):
        self.set1 = QBarSet('<b><font color="#FA7F9D">Sport</font></b>')
        self.set2 = QBarSet('<b><font color="#97ACF9">Work</font></b>')
        self.set3 = QBarSet('<b><font color="#FADA7F">Study</font></b>')
        self.set4 = QBarSet('<b><font color="#8CFA9C">Meditation</font></b>')

        self.set1.append([random.randint(0, 10) for i in range(7)])
        self.set2.append([random.randint(0, 10) for i in range(7)])
        self.set3.append([random.randint(0, 10) for i in range(7)])
        self.set4.append([random.randint(0, 10) for i in range(7)])
        self.set1.setColor(QtGui.QColor("#FA7F9D"))
        self.set2.setColor(QtGui.QColor("#97ACF9"))
        self.set3.setColor(QtGui.QColor("#FADA7F"))
        self.set4.setColor(QtGui.QColor("#8CFA9C"))

        series = QStackedBarSeries()
        series.append(self.set1)
        series.append(self.set2)
        series.append(self.set3)
        series.append(self.set4)

        chart = QChart()
        chart.setMaximumSize(700, 400)
        chart.addSeries(series)
        chart.setTitle(f'<b><font face="Inter" size="5" color="#6E6E6E">Daily averageㅤㅤㅤㅤㅤㅤㅤ20% from last week</font></b>'
                       '<br align="left"><b><font face="Inter" size="5" color="#29002F">ㅤ3 h 10 min</font></b></br>')
        chart.setAnimationOptions(QChart.AllAnimations)
        chart.setBackgroundRoundness(30)
        chart.setDropShadowEnabled(True)

        months = ('<b><font face="Inter" color="#6E6E6E" size="4">Sun</font></b>',
                  '<b><font face="Inter" color="#6E6E6E" size="4">Mon</font></b>',
                  '<b><font face="Inter" color="#6E6E6E" size="4">Tue</font></b>',
                  '<b><font face="Inter" color="#6E6E6E" size="4">Wed</font></b>',
                  '<b><font face="Inter" color="#6E6E6E" size="4">Thu</font></b>',
                  '<b><font face="Inter" color="#6E6E6E" size="4">Fri</font></b>',
                  '<b><font face="Inter" color="#6E6E6E" size="4">Sat</font></b>')

        axisX = QBarCategoryAxis()
        axisX.append(months)
        axisY = QValueAxis()
        minY = 0
        maxY = 12

        axisY.setRange(minY, maxY)
        axisY.setLabelFormat('<b><font face="Inter" color="#6E6E6E" size="4">%dh</font></b>')
        axisY.setTickCount(3)
        axisY.setMinorTickCount(1)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignRight)
        chart.legend().setVisible(True)
        chart.legend().setFont(QtGui.QFont('Arial', 12))
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.legend().setMarkerShape(2)

        chartView = QChartView(chart, self)
        chartView.setGeometry(0, 0, 580, 318)
        chartView.move(60, 32)
    def create_donutchart(self):

        series = QPieSeries()
        series.setHoleSize(0.4)

        series.append(f'<b><font color="#FA7F9D">Sport {4}h {33}min</font></b>', 20).setColor(QtGui.QColor("#FA7F9D"))
        series.append('<b><font color="#97ACF9">Work 1h 45min</font></b>', 45).setColor(QtGui.QColor("#97ACF9"))
        series.append('<b><font color="#FADA7F">Study 1h</font></b>', 25).setColor(QtGui.QColor("#FADA7F"))
        series.append('<b><font color="#8CFA9C">Meditation 2h</font></b>', 10).setColor(QtGui.QColor("#8CFA9C"))
        chart = QChart()

        chart.legend().setAlignment(QtCore.Qt.AlignLeft)
        chart.addSeries(series)

        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setBackgroundRoundness(30)
        chart.setDropShadowEnabled(True)

        chart.legend().setFont(QtGui.QFont('Arial', 12))
        chart.legend().setMarkerShape(2)

        chartview = QChartView(chart, self)
        chartview.setGeometry(0,0, 580, 318)
        chartview.move(60, 410)
        chartview.setRenderHint(QPainter.Antialiasing)

    def FrameWeek(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setGeometry(66,370,568,36)
        frame.setStyleSheet("background-color:#A597AB; border-radius: 10px")

        sunBtn = QPushButton('sun', self)
        sunBtn.setGeometry(73,374,79,28)
        sunBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        monBtn = QPushButton('mon', self)
        monBtn.setGeometry(152,374,79,28)
        monBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        tueBtn = QPushButton('tue', self)
        tueBtn.setGeometry(231,374,79,28)
        tueBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        wedBtn = QPushButton('wed', self)
        wedBtn.setGeometry(310,374,79,28)
        wedBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        thuBtn = QPushButton('thu', self)
        thuBtn.setGeometry(389,374,79,28)
        thuBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        friBtn = QPushButton('fri', self)
        friBtn.setGeometry(468,374,79,28)
        friBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:pressed{background-color:#000000; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        satBtn = QPushButton('sat', self)
        satBtn.setGeometry(547,374,79,28)
        satBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                                  "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                                  "QPushButton:pressed{background-color:#000000; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        self.prevSender = monBtn
        sunBtn.clicked.connect(self.Actions)
        monBtn.clicked.connect(self.Actions)
        tueBtn.clicked.connect(self.Actions)
        wedBtn.clicked.connect(self.Actions)
        thuBtn.clicked.connect(self.Actions)
        satBtn.clicked.connect(self.Actions)
        friBtn.clicked.connect(self.Actions)
    def Actions(self):
        sender = self.sender()
        sender.setStyleSheet("background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F")
        self.prevSender.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                                      "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                                      "QPushButton:pressed{background-color:#000000; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                                      )
        if self.prevSender == sender:
            sender.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                )
        self.prevSender = sender
