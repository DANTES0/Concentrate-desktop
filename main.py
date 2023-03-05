import sys, random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QBrush, QPen, QImage, QPalette
from PyQt5.QtChart import *
from PyQt5.QtCore import *


class Window(QMainWindow):
    def __init__(self):

        super().__init__()
        self.title = "123"
        # oImage = QImage("source\IMG_2309.jpg")
        # sImage = oImage.scaled(QSize(750, 850))
        # palette = QPalette()
        # palette.setBrush(QPalette.Window, QBrush(sImage))
        # self.setPalette(palette)
        # self.lable.setText("Да ДА ДА")
        self.Graph()
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
        self.setGeometry(650,50,750,850)
        self.setFixedSize(QSize(750,850))
        self.show()


    def Graph(self):
        self.set0 = QBarSet('X0')
        self.set1 = QBarSet('X1')
        self.set2 = QBarSet('X2')
        self.set3 = QBarSet('X3')
        self.set4 = QBarSet('X4')

        self.set0.append([random.randint(0, 10) for i in range(6)])
        self.set1.append([random.randint(0, 10) for i in range(6)])
        self.set2.append([random.randint(0, 10) for i in range(6)])
        self.set3.append([random.randint(0, 10) for i in range(6)])
        self.set4.append([random.randint(0, 10) for i in range(6)])

        series = QStackedBarSeries()
        series.append(self.set0)
        series.append(self.set1)
        series.append(self.set2)
        series.append(self.set3)
        series.append(self.set4)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Bar Chart Demo')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun')

        axisX = QBarCategoryAxis()
        axisX.append(months)

        axisY = QValueAxis()
        axisY.setRange(0, 15)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)
        self.setCentralWidget(chartView)

    # def timerEvent(self):
    #     #        global time
    #     self.time = self.time.addSecs(1)
    #     #        print(self.time.toString("hh:mm"))
    #     self.lcdTime.display(self.time.toString("mm:ss "))


    # def paintEvent(self,event):
    #     painter = QPainter(self)
    #     painter.setPen(QPen(Qt.red, 8, Qt.SolidLine))
    #     painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
    #     painter.drawEllipse(130,150,350,350)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    App.setStyleSheet("""
    QWidget.QLCDNumber {
        background-color: "transparent";
        color: "white";
        font: bold italic large "Times New Roman"
    }
    """)

    sys.exit(App.exec_())
