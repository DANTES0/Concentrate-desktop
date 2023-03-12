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
        # self.FrameBtn()
        self.FrameWeek()
        # self.CreateTimer()
        self.InitWindow()
    def InitWindow(self):
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle(self.title)
        self.setGeometry(650,50,700,762)
        self.setFixedSize(QSize(700,762))
        # self.show()
    def BackLabel(self):
        self.backLabel = QLabel("White", self)
        pixmap = QPixmap('source/Cat_1.png')
        self.backLabel.setPixmap(pixmap)
        self.backLabel.setStyleSheet("background-color: transparent")
        # self.backLabel.setMinimumSize(120,120)
        self.backLabel.setGeometry(387,627,100,100)

        ConcentrationLabel = QLabel("Concentration time", self)
        ConcentrationLabel.setGeometry(83,101,227,29)
        ConcentrationLabel.setStyleSheet("background-color: transparent; font: bold 24px; font-family: Inter; color: #29002F")
    def Graph(self):
        # self.set0 = QBarSet('X0')
        self.set1 = QBarSet('<b><font color="#FA7F9D">Sport</font></b>')
        self.set2 = QBarSet('<b><font color="#97ACF9">Work</font></b>')
        self.set3 = QBarSet('<b><font color="#FADA7F">Study</font></b>')
        self.set4 = QBarSet('<b><font color="#8CFA9C">Meditation</font></b>')

        # self.set0.append([random.randint(0, 10) for i in range(7)])
        self.set1.append([random.randint(0, 10) for i in range(7)])
        self.set2.append([random.randint(0, 10) for i in range(7)])
        self.set3.append([random.randint(0, 10) for i in range(7)])
        self.set4.append([random.randint(0, 10) for i in range(7)])
        self.set1.setColor(QtGui.QColor("#FA7F9D"))
        self.set2.setColor(QtGui.QColor("#97ACF9"))
        self.set3.setColor(QtGui.QColor("#FADA7F"))
        self.set4.setColor(QtGui.QColor("#8CFA9C"))
        series = QStackedBarSeries()
        # series.append(self.set0)
        series.append(self.set1)
        series.append(self.set2)
        series.append(self.set3)
        series.append(self.set4)
        chart = QChart()
        # chart.setPos(700, 600)
        chart.setMaximumSize(700, 400)
        # chart.set
        chart.addSeries(series)
        # chart.setTheme('ChartThemeBlueCerulean')
        chart.setTitle(f'<b><font face="Inter" size="5" color="#6E6E6E">Daily averageㅤㅤㅤㅤㅤㅤㅤ20% from last week</font></b>'
                       '<br align="left"><b><font face="Inter" size="5" color="#29002F">ㅤ3 h 10 min</font></b></br>')
        # chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setAnimationOptions(QChart.AllAnimations)
        # chart.setTheme(4)
        chart.setBackgroundRoundness(30)
        chart.setDropShadowEnabled(True)
        # chart.isZoomed()
        # chart.setBackgroundVisible(False)

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
        # axisY.setLabelFormat('<font face="Bryndan Write" size="5">%dh</font>')
        axisY.setLabelFormat('<b><font face="Inter" color="#6E6E6E" size="4">%dh</font></b>')
        axisY.setTickCount(3)
        axisY.setMinorTickCount(1)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignRight)
        chart.legend().setVisible(True)
        chart.legend().setFont(QtGui.QFont('Arial', 12))
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.legend().setMarkerShape(2)
        #Стало
        chartView = QChartView(chart, self)
        # self.scene.addItem(self.chart)
        chartView.setGeometry(0, 0, 580, 318)
        chartView.move(60, 120)
        # self.chartView.show()
        # self.setCentralWidget(chartView)

        # self.view.show()
        # chartView.setAlignment(Qt.AlignBottom)
    def create_donutchart(self):

        series = QPieSeries()
        series.setHoleSize(0.4)
        # series.setPieSize(0.8)
        series.append(f'<b><font color="#FA7F9D">Sport {4}h {33}min</font></b>', 20).setColor(QtGui.QColor("#FA7F9D"))
        series.append('<b><font color="#97ACF9">Work 1h 45min</font></b>', 45).setColor(QtGui.QColor("#97ACF9"))
        series.append('<b><font color="#FADA7F">Study 1h</font></b>', 25).setColor(QtGui.QColor("#FADA7F"))
        series.append('<b><font color="#8CFA9C">Meditation 2h</font></b>', 10).setColor(QtGui.QColor("#8CFA9C"))
        chart = QChart()
        # chart.legend().hide()
        # chart.legend().moveBy(5,700)
        chart.legend().setAlignment(QtCore.Qt.AlignLeft)
        chart.addSeries(series)
        # chart.setMaximumSize(450, 450)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        # chart.setTitle("")
        # chart.setTheme(QChart.ChartThemeQt)
        chart.setBackgroundRoundness(30)
        chart.setDropShadowEnabled(True)
        # chart.setBackgroundVisible(False)
        chart.legend().setFont(QtGui.QFont('Arial', 12))
        chart.legend().setMarkerShape(2)

        chartview = QChartView(chart, self)
        chartview.setGeometry(0,0, 580, 318)
        chartview.move(60, 520)
        chartview.setRenderHint(QPainter.Antialiasing)

        # self.setCentralWidget(chartview)
    # def FrameBtn(self):
    #     frame = QFrame(self)
    #     # frame.setFrameShape(QFrame.StyledPanel)
    #     frame.setFrameShape(QFrame.NoFrame)
    #     frame.setGeometry(0,0,700,88)
    #     frame.setStyleSheet("background-color:#D8B5E9;")
    #     TimerBtn = QPushButton('Timer',self)
    #     TimerBtn.clicked.connect(self.gotoTimer)
    #     TimerBtn.setGeometry(51,24,127,50)
    #     TimerBtn.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
    #     TaskButton = QPushButton('Task',self)
    #     TaskButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
    #     TaskButton.setGeometry(208,24,127,50)
    #     StatisticsButton = QPushButton('Statistics',self)
    #     StatisticsButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
    #     StatisticsButton.setGeometry(365, 24, 127, 50)
    #     CatRoomButton = QPushButton('Cat room',self)
    #     CatRoomButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
    #     CatRoomButton.setGeometry(522,24,127,50)
    def FrameWeek(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setGeometry(66,474,568,36)
        frame.setStyleSheet("background-color:#A597AB; border-radius: 10px")
        sunBtn = QPushButton('sun', self)
        sunBtn.setGeometry(73,478,79,28)
        sunBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        monBtn = QPushButton('mon', self)
        monBtn.setGeometry(152,478,79,28)
        monBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        tueBtn = QPushButton('tue', self)
        tueBtn.setGeometry(231,478,79,28)
        tueBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        wedBtn = QPushButton('wed', self)
        wedBtn.setGeometry(310,478,79,28)
        wedBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        thuBtn = QPushButton('thu', self)
        thuBtn.setGeometry(389,478,79,28)
        thuBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        friBtn = QPushButton('fri', self)
        friBtn.setGeometry(468,478,79,28)
        friBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:pressed{background-color:#000000; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        satBtn = QPushButton('sat', self)
        satBtn.setGeometry(547,478,79,28)
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
    def gotoTimer(self):
        print("123")
        # global widget
        # timer = timer_class.Timer()
        # main.widget.addWidget(timer)
        # widget.setCurrentIndex(widget.currentIndex()-1)