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
        self.FrameBtn()
        self.Frame_Timer()
        self.CreateTimer()
        self.Task_list()
        self.InitWindow()

    def Task_list(self):

        lable = QLabel("Task list",self)
        lable.setGeometry(51,663,127,50)
        lable.setAlignment(Qt.AlignCenter)
        lable.setStyleSheet("background-color:#8350AA;border-radius:25px;font:24px;font-family:Inter;"
                            "font-weight:bold;color:#ffffff;")

        list1 = QLineEdit(self)
        list1.setGeometry(51,720,598,50)
        list1.setStyleSheet("background-color:#ffffff; border-radius:25px; font-family: Inter; font:18px;"
                            "padding: 0 40px; font-weight:bold;")
        list2 = QLineEdit(self)
        list2.setGeometry(51, 777, 598, 50)
        list2.setStyleSheet("background-color:#ffffff; border-radius:25px; font-family: Inter; font:18px;"
                            "padding: 0 40px; font-weight:bold;")
        lableCircle1 = QLabel(self)
        lableCircle1.setGeometry(69, 740, 9, 9)
        lableCircle1.setStyleSheet("background-color:#8350AA; border-radius:4px")

        lableCircle2 = QLabel(self)
        lableCircle2.setGeometry(69, 797, 9, 9)
        lableCircle2.setStyleSheet("background-color:#8350AA; border-radius:4px")
    def paintEvent(self,event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # Draw the background circle
        pen = QPen(QColor(187, 137, 217), 20, Qt.SolidLine, Qt.FlatCap)
        painter.setPen(pen)
        painter.setBrush(QColor(229, 219, 233))
        painter.drawEllipse(146, 106, 407, 407)
        # painter.fillRect(146,156,407,407,QColor(229, 219, 233))
    def Frame_Timer(self):
        # frame = QFrame(self)
        # frame.setGeometry(146,156,407, 407)
        # frame.setStyleSheet("border-radius: 200px; border: 1px solid black")
        pic_lable = QLabel(self)
        pixmap = QPixmap('source/Time_Cat.png')
        pic_lable.setPixmap(pixmap)
        pic_lable.setGeometry(246, 167, 197, 254)

        # pic_lable.setStyleSheet("background-color:transparent")
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
        self.sliderTimer.setGeometry(211,525,280,15)
        self.sliderTimer.setStyleSheet(""".QSlider {
                                            min-height: 68px;
                                            max-height: 68px;
                                            background: transparent;
                                            }
                                            
                                            .QSlider::groove:horizontal {
                                            border: 1px solid #262626;
                                            height: 5px;
                                            background: #393939;
                                            margin: 0 12px;
                                            }
                                            
                                            .QSlider::handle:horizontal {
                                            background: #BB89D9;
                                            border: 4px solid #BB89D9;
                                            border-radius: 8px;
                                            width: 32px;
                                            height: 100px;
                                            margin: -8px -12px;
                                        }""")
        self.lable = QLabel("00:00", self)
        self.lable.setFont(QtGui.QFont('Inter', 20))
        self.lable.setAlignment(Qt.AlignCenter)
        self.lable.setStyleSheet("color:white; font-family: Inter;")
        self.lable.setGeometry(298,432,115,36)

        self.start_btn = QPushButton("Start", self)
        self.start_btn.setGeometry(208,594,127,50)
        self.start_btn.clicked.connect(self.start_action)
        self.start_btn.setStyleSheet("border-radius: 25px; background-color:#9CC152; color:#ffffff; "
                                     "font-family:Inter; font:24px; font-weight:bold")

        self.stop_btn = QPushButton("Stop", self)
        self.stop_btn.move(70, 250)
        self.stop_btn.setGeometry(365, 594, 127, 50)
        self.stop_btn.clicked.connect(self.stop_action)
        self.stop_btn.setStyleSheet("border-radius: 25px; background-color:#FA7B7B; color:#ffffff; "
                                     "font-family:Inter; font:24px; font-weight:bold")

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
        self.start = True
        print(self.start)
        print(self.count)
        if self.count == 0:
            self.start = False
    def stop_action(self):
        self.start = False
        self.count = 0
        self.sliderTimer.setValue(0)
    def UpdateLabel(self,value):
        self.count = value
        m, s = divmod(self.count, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        self.lable.setText(str(min_sec_format))
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(650,50,700,850)
        self.setFixedSize(QSize(700,850))
        # self.show()
    def FrameBtn(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setGeometry(0,0,700,88)
        frame.setStyleSheet("background-color:#D8B5E9;")
        TimerBtn = QPushButton('Timer',self)
        TimerBtn.setGeometry(51,24,127,50)
        TimerBtn.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
        TaskButton = QPushButton('Task',self)
        TaskButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
        TaskButton.setGeometry(208,24,127,50)
        StatisticsButton = QPushButton('Statistics',self)
        StatisticsButton.clicked.connect(self.gotoStats)
        StatisticsButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
        StatisticsButton.setGeometry(365, 24, 127, 50)
        CatRoomButton = QPushButton('Cat room',self)
        CatRoomButton.clicked.connect(self.gotoCatRoom)
        CatRoomButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
        CatRoomButton.setGeometry(522,24,127,50)
    def gotoStats(self):
        print(widget.currentIndex)
        statistics = Statistics()
        widget.addWidget(statistics)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoCatRoom(self):
        print(widget.currentIndex)
        room = CatRoom()
        widget.addWidget(room)
        widget.setCurrentIndex(widget.currentIndex()+2)

class CatRoom(QMainWindow):
    def __init__(self):
        super.__init__()
        self.title = "Meow concentration"
        self.scene = QGraphicsScene()
        self.view= QGraphicsView(self.scene)
        self.setWindowIcon(QtGui.QIcon('source/cat.ico'))
        self.setStyleSheet("background-color: red")
        self.prevSender = None
        self.InitWindow()
    def BackLabel(self):
        self.backLabel = QLabel("White", self)
        pixmap = QPixmap('source/Cat_1.png')
        self.backLabel.setPixmap(pixmap)
        self.backLabel.setStyleSheet("background-color: transparent")
        # self.backLabel.setMinimumSize(120,120)
        self.backLabel.setGeometry(387,627,100,100)

    def InitWindow(self):
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle(self.title)
        self.setGeometry(650,50,700,850)
        self.setFixedSize(QSize(700,850))

class Statistics(QMainWindow):
    def __init__(self):

        super().__init__()
        self.title = "Meow concentration"
        self.scene = QGraphicsScene()
        self.view= QGraphicsView(self.scene)
        self.setWindowIcon(QtGui.QIcon('source/cat.ico'))
        self.setStyleSheet("background-color: #E5DBE9")
        self.prevSender = None
        # oImage = QImage("source")
        # sImage = oImage.scaled(QSize(750, 850))
        # palette = QPalette()
        # palette.setBrush(QPalette.Window, QBrush(sImage))
        # self.setPalette(palette)
        # self.lable.setText("Да ДА ДА")

        self.Graph()
        self.create_donutchart()
        self.BackLabel()
        self.FrameBtn()
        self.FrameWeek()
        # self.CreateTimer()
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
        self.lable.resize(220,100)
        self.lable.setAlignment(Qt.AlignCenter)
        self.lable.setStyleSheet("border: 3px solid black")
        # self.lable.setText(str(self.sliderTimer.value()))

        self.start_btn = QPushButton("Start", self)
        self.start_btn.move(70, 200)
        self.start_btn.clicked.connect(self.start_action)
        # self.start_btn.resize(150, 150)
        self.start_btn.setStyleSheet("border: 2px solid black;border-radius: 15%;")

        self.stop_btn = QPushButton("Stop", self)
        self.stop_btn.move(70, 200)
        self.stop_btn.clicked.connect(self.stop_action)
        self.stop_btn.setVisible(False)

        self.timer = QTimer(self)
        self.time = QTime(0,0,0)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        # self.lcdTime = QtWidgets.QLCDNumber(self)
        # self.lcdTime.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        # self.lcdTime.setDigitCount(8)
        # self.lcdTime.move(135, 300)
        # self.lcdTime.resize(320, 60)
        # self.time = QtCore.QTime(0, 0, 0)
        #
        # vbox = QtWidgets.QVBoxLayout(self)
        # vbox.addWidget(self.lcdTime)
        #
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.timerEvent)
        # self.timer.start(1000)
    def showTime(self):
        # self.minutes = self.count // 600
        # self.seconds = self.count - (self.minutes * 100)
        # checking if flag is true
        if self.start:
            # incrementing the counter
            # if self.seconds == 0:
            #     self.minutes -= 10
            #     self.seconds = 600
            self.count -= 1
            m, s = divmod(self.count, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m,s)
            # self.seconds = self.count - (self.minutes * 100)
            # print(self.seconds)
            # self.lable.setText(str(self.minutes) + ":" + str(self.seconds))
            self.lable.setText(str(min_sec_format))

            # timer is completed
            if self.count == 0:
                # making flag false
                self.lable.setText("00:00")
                self.start = False
    def start_action(self):
        # making flag true
        self.start_btn.setVisible(False)
        self.stop_btn.setVisible(True)
        self.start = True
        print(self.start)
        print(self.count)
        # self.lable.setText(str(self.count))
        # count = 0
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
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle(self.title)
        self.setGeometry(650,50,700,850)
        self.setFixedSize(QSize(700,850))
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
        CatRoomButton.clicked.connect(self.gotoCatRoom)
        CatRoomButton.setStyleSheet("background-color:#8350AA; border-radius: 25px; font: bold 24px; font-family: Inter; color: #ffffff")
        CatRoomButton.setGeometry(522,24,127,50)
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
        # self.WeekPushButton = QButtonGroup()
        # self.WeekPushButton.addButton(sunBtn)
        # self.WeekPushButton.addButton(monBtn)
        # self.WeekPushButton.addButton(thuBtn)
        # self.WeekPushButton.addButton(wedBtn)
        # self.WeekPushButton.addButton(friBtn)
        # self.WeekPushButton.buttonClicked.connect(self.Actions)
        # self.WeekPushButton.addButton()
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
        print(widget.currentIndex)
        timer = Timer()
        widget.addWidget(timer)
        widget.setCurrentIndex(widget.currentIndex()-1)
    def gotoCatRoom(self):
        print(widget.currentIndex)
        room = CatRoom()
        widget.addWidget(room)
        widget.setCurrentIndex(widget.currentIndex()+1)


app = QtWidgets.QApplication(sys.argv)
global widget
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle("Meow concentration")
widget.setWindowIcon(QtGui.QIcon('source/cat.ico'))
widget.setGeometry(650,50,700,850)
timer=Timer()
stats=Statistics()
widget.addWidget(timer)
widget.addWidget(stats)


widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")