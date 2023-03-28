import sys, random, sqlite3

import yaml, datetime, os.path
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
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cleanTable()
        self.Graph()
        self.create_donutchart(0)
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
        self.backLabel.setGeometry(383,520,100,100)

        ConcentrationLabel = QLabel("Concentration time", self)
        ConcentrationLabel.setGeometry(83,13,227,29)
        ConcentrationLabel.setStyleSheet("background-color: transparent; font: bold 24px; font-family: Inter; color: #29002F")

    def updateGraph(self):
        sum_workM = 0
        sum_workTue = 0
        sum_workWed = 0
        sum_workThu = 0
        sum_workFri = 0
        sum_workSat = 0
        sum_workSun = 0
        sum_sportM = 0
        sum_sportTue = 0
        sum_sportWed = 0
        sum_sportThu = 0
        sum_sportFri = 0
        sum_sportSat = 0
        sum_sportSun = 0
        sum_otherM = 0
        sum_otherTue = 0
        sum_otherWed = 0
        sum_otherThu = 0
        sum_otherFri = 0
        sum_otherSat = 0
        sum_otherSun = 0
        sum_studyM = 0
        sum_studyTue = 0
        sum_studyWed = 0
        sum_studyThu = 0
        sum_studyFri = 0
        sum_studySat = 0
        sum_studySun = 0
        self.cur.execute("SELECT week, tag, time FROM stats")
        res = self.cur.fetchall()
        for row in res:
            if row[1] == 'work' and row[0] == 0:
                sum_workM = sum_workM + row[2]
            if row[1] == 'study' and row[0] == 0:
                sum_studyM = sum_studyM + row[2]
            if row[1] == 'other' and row[0] == 0:
                sum_otherM = sum_otherM + row[2]
            if row[1] == 'sport' and row[0] == 0:
                sum_sportM = sum_sportM + row[2]

            if row[1] == 'work' and row[0] == 1:
                sum_workTue = sum_workTue + row[2]
            if row[1] == 'study' and row[0] == 1:
                sum_studyTue = sum_studyTue + row[2]
            if row[1] == 'other' and row[0] == 1:
                sum_otherTue = sum_otherTue + row[2]
            if row[1] == 'sport' and row[0] == 1:
                sum_sportTue = sum_sportTue + row[2]

            if row[1] == 'work' and row[0] == 2:
                sum_workWed = sum_workWed + row[2]
            if row[1] == 'study' and row[0] == 2:
                sum_studyWed = sum_studyWed + row[2]
            if row[1] == 'other' and row[0] == 2:
                sum_otherWed = sum_otherWed + row[2]
            if row[1] == 'sport' and row[0] == 2:
                sum_sportWed = sum_sportWed + row[2]

            if row[1] == 'work' and row[0] == 3:
                sum_workThu = sum_workThu + row[2]
            if row[1] == 'study' and row[0] == 3:
                sum_studyThu = sum_studyThu + row[2]
            if row[1] == 'other' and row[0] == 3:
                sum_otherThu = sum_otherThu + row[2]
            if row[1] == 'sport' and row[0] == 3:
                sum_sportThu = sum_sportThu + row[2]

            if row[1] == 'work' and row[0] == 4:
                sum_workFri = sum_workFri + row[2]
            if row[1] == 'study' and row[0] == 4:
                sum_studyFri = sum_studyFri + row[2]
            if row[1] == 'other' and row[0] == 4:
                sum_otherFri = sum_otherFri + row[2]
            if row[1] == 'sport' and row[0] == 4:
                sum_sportFri = sum_sportFri + row[2]

            if row[1] == 'work' and row[0] == 5:
                sum_workSat = sum_workSat + row[2]
            if row[1] == 'study' and row[0] == 5:
                sum_studySat = sum_studySat + row[2]
            if row[1] == 'other' and row[0] == 5:
                sum_otherSat = sum_otherSat + row[2]
            if row[1] == 'sport' and row[0] == 5:
                sum_sportSat = sum_sportSat + row[2]

            if row[1] == 'work' and row[0] == 6:
                sum_workSun = sum_workSun + row[2]
            if row[1] == 'study' and row[0] == 6:
                sum_studySun = sum_studySun + row[2]
            if row[1] == 'other' and row[0] == 6:
                sum_otherSun = sum_otherSun + row[2]
            if row[1] == 'sport' and row[0] == 6:
                sum_sportSun = sum_sportSun + row[2]

            self.set1.append(
                [sum_sportM, sum_sportTue, sum_sportWed, sum_sportThu, sum_sportFri, sum_sportSat, sum_sportSun])
            self.set2.append([sum_workM, sum_workTue, sum_workWed, sum_workThu, sum_workFri, sum_workSat, sum_workSun])
            self.set3.append(
                [sum_studyM, sum_studyTue, sum_studyWed, sum_studyThu, sum_studyFri, sum_studySat, sum_studySun])
            self.set4.append(
                [sum_otherM, sum_otherTue, sum_otherWed, sum_otherThu, sum_otherFri, sum_otherSat, sum_otherSun])
            self.chartViewG.update()

    def Graph(self):
        sum_workM = 0
        sum_workTue = 0
        sum_workWed = 0
        sum_workThu = 0
        sum_workFri = 0
        sum_workSat = 0
        sum_workSun = 0
        sum_sportM = 0
        sum_sportTue = 0
        sum_sportWed = 0
        sum_sportThu = 0
        sum_sportFri = 0
        sum_sportSat = 0
        sum_sportSun = 0
        sum_otherM = 0
        sum_otherTue = 0
        sum_otherWed = 0
        sum_otherThu = 0
        sum_otherFri = 0
        sum_otherSat = 0
        sum_otherSun = 0
        sum_studyM = 0
        sum_studyTue = 0
        sum_studyWed = 0
        sum_studyThu = 0
        sum_studyFri = 0
        sum_studySat = 0
        sum_studySun = 0
        self.cur.execute("SELECT week, tag, time FROM stats")
        res = self.cur.fetchall()
        for row in res:
            if row[1] == 'work' and row[0] == 0:
                sum_workM = sum_workM + row[2]
            if row[1] == 'study' and row[0] == 0:
                sum_studyM = sum_studyM + row[2]
            if row[1] == 'other' and row[0] == 0:
                sum_otherM = sum_otherM + row[2]
            if row[1] == 'sport' and row[0] == 0:
                sum_sportM = sum_sportM + row[2]

            if row[1] == 'work' and row[0] == 1:
                sum_workTue = sum_workTue + row[2]
            if row[1] == 'study' and row[0] == 1:
                sum_studyTue = sum_studyTue + row[2]
            if row[1] == 'other' and row[0] == 1:
                sum_otherTue = sum_otherTue + row[2]
            if row[1] == 'sport' and row[0] == 1:
                sum_sportTue = sum_sportTue + row[2]

            if row[1] == 'work' and row[0] == 2:
                sum_workWed = sum_workWed + row[2]
            if row[1] == 'study' and row[0] == 2:
                sum_studyWed = sum_studyWed + row[2]
            if row[1] == 'other' and row[0] == 2:
                sum_otherWed = sum_otherWed + row[2]
            if row[1] == 'sport' and row[0] == 2:
                sum_sportWed = sum_sportWed + row[2]

            if row[1] == 'work' and row[0] == 3:
                sum_workThu = sum_workThu + row[2]
            if row[1] == 'study' and row[0] == 3:
                sum_studyThu = sum_studyThu + row[2]
            if row[1] == 'other' and row[0] == 3:
                sum_otherThu = sum_otherThu + row[2]
            if row[1] == 'sport' and row[0] == 3:
                sum_sportThu = sum_sportThu + row[2]

            if row[1] == 'work' and row[0] == 4:
                sum_workFri = sum_workFri + row[2]
            if row[1] == 'study' and row[0] == 4:
                sum_studyFri = sum_studyFri + row[2]
            if row[1] == 'other' and row[0] == 4:
                sum_otherFri = sum_otherFri + row[2]
            if row[1] == 'sport' and row[0] == 4:
                sum_sportFri = sum_sportFri + row[2]

            if row[1] == 'work' and row[0] == 5:
                sum_workSat = sum_workSat + row[2]
            if row[1] == 'study' and row[0] == 5:
                sum_studySat = sum_studySat + row[2]
            if row[1] == 'other' and row[0] == 5:
                sum_otherSat = sum_otherSat + row[2]
            if row[1] == 'sport' and row[0] == 5:
                sum_sportSat = sum_sportSat + row[2]

            if row[1] == 'work' and row[0] == 6:
                sum_workSun = sum_workSun + row[2]
            if row[1] == 'study' and row[0] == 6:
                sum_studySun = sum_studySun + row[2]
            if row[1] == 'other' and row[0] == 6:
                sum_otherSun = sum_otherSun + row[2]
            if row[1] == 'sport' and row[0] == 6:
                sum_sportSun = sum_sportSun + row[2]




        self.set1 = QBarSet('<b><font color="#FA7F9D">Sport</font></b>')
        self.set2 = QBarSet('<b><font color="#97ACF9">Work</font></b>')
        self.set3 = QBarSet('<b><font color="#FADA7F">Study</font></b>')
        self.set4 = QBarSet('<b><font color="#8CFA9C">Other</font></b>')

        # self.set1.append([random.randint(0, 10) for i in range(7)])
        self.set1.append([sum_sportM, sum_sportTue, sum_sportWed, sum_sportThu, sum_sportFri, sum_sportSat, sum_sportSun])
        self.set2.append([sum_workM, sum_workTue, sum_workWed, sum_workThu, sum_workFri, sum_workSat, sum_workSun])
        self.set3.append([sum_studyM, sum_studyTue, sum_studyWed, sum_studyThu, sum_studyFri, sum_studySat, sum_studySun])
        self.set4.append([sum_otherM, sum_otherTue, sum_otherWed, sum_otherThu, sum_otherFri, sum_otherSat, sum_otherSun])
        self.set1.setColor(QtGui.QColor("#FA7F9D"))
        self.set2.setColor(QtGui.QColor("#97ACF9"))
        self.set3.setColor(QtGui.QColor("#FADA7F"))
        self.set4.setColor(QtGui.QColor("#8CFA9C"))

        self.seriesG = QStackedBarSeries()
        self.seriesG.append(self.set1)
        self.seriesG.append(self.set2)
        self.seriesG.append(self.set3)
        self.seriesG.append(self.set4)

        self.chartG = QChart()
        self.chartG.setMaximumSize(700, 400)
        self.chartG.addSeries(self.seriesG)
        self.chartG.setTitle(f'<b><font face="Inter" size="5" color="#6E6E6E">Daily averageㅤㅤㅤㅤㅤㅤㅤ20% from last week</font></b>'
                       '<br align="left"><b><font face="Inter" size="5" color="#29002F">ㅤ3 h 10 min</font></b></br>')
        self.chartG.setAnimationOptions(QChart.AllAnimations)
        self.chartG.setBackgroundRoundness(30)
        self.chartG.setDropShadowEnabled(True)

        months = ('<b><font face="Inter" color="#6E6E6E" size="4">Mon</font></b>',
                  '<b><font face="Inter" color="#6E6E6E" size="4">Tue</font></b>',
                  '<b><font face="Inter" color="#6E6E6E" size="4">Wed</font></b>',
                  '<b><font face="Inter" color="#6E6E6E" size="4">Thu</font></b>',
                  '<b><font face="Inter" color="#6E6E6E" size="4">Fri</font></b>',
                  '<b><font face="Inter" color="#6E6E6E" size="4">Sat</font></b>',
                  '<b><font face="Inter" color="#6E6E6E" size="4">Sun</font></b>')

        axisX = QBarCategoryAxis()
        axisX.append(months)
        axisY = QValueAxis()
        minY = 0
        maxY = 12

        axisY.setRange(minY, maxY)
        axisY.setLabelFormat('<b><font face="Inter" color="#6E6E6E" size="4">%dh</font></b>')
        axisY.setTickCount(3)
        axisY.setMinorTickCount(1)

        self.chartG.addAxis(axisX, Qt.AlignBottom)
        self.chartG.addAxis(axisY, Qt.AlignRight)
        self.chartG.legend().setVisible(True)
        self.chartG.legend().setFont(QtGui.QFont('Arial', 12))
        self.chartG.legend().setAlignment(Qt.AlignBottom)
        self.chartG.legend().setMarkerShape(2)

        self.chartViewG = QChartView(self.chartG, self)
        self.chartViewG.setGeometry(0, 0, 580, 318)
        self.chartViewG.move(60, 32)
    def cleanTable(self):
        self.cur.execute("SELECT week, day, month, year, data FROM stats")
        res = self.cur.fetchall()
        for row in res:
            count_left_elem_week = datetime.date.today().weekday()
            left_border = datetime.date.today().day - count_left_elem_week
            if ((row[1] < left_border) or (row[2] < datetime.date.today().month) or (row[3] < datetime.date.today().year)):
                self.cur.execute(f"DELETE FROM stats WHERE data='{row[4]}'")
                self.data_base.commit()

    def create_donutchart(self, week):
        sum_work = 0
        sum_sport = 0
        sum_other = 0
        sum_study = 0
        self.cur.execute("SELECT week, tag, time FROM stats")
        res = self.cur.fetchall()
        for row in res:
            if row[0] == week:
                if row[1] == 'work':
                    sum_work = sum_work + row[2]
                if row[1] == 'study':
                    sum_study = sum_study + row[2]
                if row[1] == 'other':
                    sum_other = sum_other + row[2]
                if row[1] == 'sport':
                    sum_sport = sum_sport + row[2]

            print(row[0], row[1], row[2])
        minute_work, seconds_work = divmod(sum_work, 60)
        minute_study, seconds_study = divmod(sum_study, 60)
        minute_sport, seconds_sport = divmod(sum_sport, 60)
        minute_other, seconds_other = divmod(sum_other, 60)

        self.series = QPieSeries()
        self.series.clear()
        self.series.setHoleSize(0.4)

        self.series.append(f'<b><font color="#FA7F9D">Sport {minute_sport}m {seconds_sport}s</font></b>', sum_sport).setColor(QtGui.QColor("#FA7F9D"))
        self.series.append(f'<b><font color="#97ACF9">Work {minute_work}m {seconds_work}s</font></b>', sum_work).setColor(QtGui.QColor("#97ACF9"))
        self.series.append(f'<b><font color="#FADA7F">Study {minute_study}m {seconds_study}s</font></b>', sum_study).setColor(QtGui.QColor("#FADA7F"))
        self.series.append(f'<b><font color="#8CFA9C">Other {minute_other}m {seconds_other}s</font></b>', sum_other).setColor(QtGui.QColor("#8CFA9C"))
        self.chart = QChart()

        self.chart.legend().setAlignment(QtCore.Qt.AlignLeft)
        self.chart.addSeries(self.series)

        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setBackgroundRoundness(30)
        self.chart.setDropShadowEnabled(True)

        self.chart.legend().setFont(QtGui.QFont('Arial', 12))
        self.chart.legend().setMarkerShape(2)

        self.chartview = QChartView(self.chart, self)
        self.chartview.setGeometry(0,0, 580, 318)
        self.chartview.move(60, 410)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.chartview.update()

    def updateChart(self):
        sender = self.sender()
        sender.setStyleSheet(
            "background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F")
        self.prevSender.setStyleSheet(
            "QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
            "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
            "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
            )
        if self.prevSender == sender:
            sender.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                )
        self.prevSender = sender
        week = 0
        if sender == self.monBtn:
            week = 0
        if sender == self.tueBtn:
            week = 1
            self.backLabel.setGeometry(377,520,100,100)
        if sender == self.wedBtn:
            week = 2
        if sender == self.thuBtn:
            week = 3
        if sender == self.friBtn:
            week = 4
        if sender == self.satBtn:
            week = 5
        if sender == self.sunBtn:
            week = 6
        self.series.clear()
        sum_work = 0
        sum_sport = 0
        sum_other = 0
        sum_study = 0
        self.cur.execute("SELECT week, tag, time FROM stats")
        res = self.cur.fetchall()
        for row in res:
            if row[0] == week:
                if row[1] == 'work':
                    sum_work = sum_work + row[2]
                if row[1] == 'study':
                    sum_study = sum_study + row[2]
                if row[1] == 'other':
                    sum_other = sum_other + row[2]
                if row[1] == 'sport':
                    sum_sport = sum_sport + row[2]

            print(row[0], row[1], row[2])
        minute_work, seconds_work = divmod(sum_work, 60)
        minute_study, seconds_study = divmod(sum_study, 60)
        minute_sport, seconds_sport = divmod(sum_sport, 60)
        minute_other, seconds_other = divmod(sum_other, 60)

        self.series.append(f'<b><font color="#FA7F9D">Sport {minute_sport}m {seconds_sport}s</font></b>', sum_sport).setColor(QtGui.QColor("#FA7F9D"))
        self.series.append(f'<b><font color="#97ACF9">Work {minute_work}m {seconds_work}s</font></b>', sum_work).setColor(QtGui.QColor("#97ACF9"))
        self.series.append(f'<b><font color="#FADA7F">Study {minute_study}m {seconds_study}s</font></b>', sum_study).setColor(QtGui.QColor("#FADA7F"))
        self.series.append(f'<b><font color="#8CFA9C">Other {minute_other}m {seconds_other}s</font></b>', sum_other).setColor(QtGui.QColor("#8CFA9C"))
        self.series.setHoleSize(0.4)
        self.chartview.update()


    def FrameWeek(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setGeometry(66,370,568,36)
        frame.setStyleSheet("background-color:#A597AB; border-radius: 10px")

        self.monBtn = QPushButton('mon', self)
        self.monBtn.setGeometry(73,374,79,28)
        self.monBtn.setStyleSheet("QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        self.tueBtn = QPushButton('tue', self)
        self.tueBtn.setGeometry(152,374,79,28)
        self.tueBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        self.wedBtn = QPushButton('wed', self)
        self.wedBtn.setGeometry(231,374,79,28)
        self.wedBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        self.thuBtn = QPushButton('thu', self)
        self.thuBtn.setGeometry(310,374,79,28)
        self.thuBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        self.friBtn = QPushButton('fri', self)
        self.friBtn.setGeometry(389,374,79,28)
        self.friBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        self.satBtn = QPushButton('sat', self)
        self.satBtn.setGeometry(468,374,79,28)
        self.satBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                             "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        self.sunBtn = QPushButton('sun', self)
        self.sunBtn.setGeometry(547,374,79,28)
        self.sunBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                                  "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                                  "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
        self.prevSender = self.monBtn
        self.sunBtn.clicked.connect(self.updateChart)
        self.monBtn.clicked.connect(self.updateChart)
        self.tueBtn.clicked.connect(self.updateChart)
        self.wedBtn.clicked.connect(self.updateChart)
        self.thuBtn.clicked.connect(self.updateChart)
        self.satBtn.clicked.connect(self.updateChart)
        self.friBtn.clicked.connect(self.updateChart)
    # def Actions(self):
    #     sender = self.sender()
    #     sender.setStyleSheet("background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F")
    #     self.prevSender.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
    #                                   "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
    #                                   "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
    #                                   )
    #     if sender == self.monBtn:
    #         self.create_donutchart(0)
    #     if sender == self.tueBtn:
    #         self.create_donutchart(1)
    #     if sender == self.wedBtn:
    #         self.create_donutchart(2)
    #     if sender == self.thuBtn:
    #         self.create_donutchart(3)
    #     if sender == self.friBtn:
    #         self.create_donutchart(4)
    #     if sender == self.satBtn:
    #         self.create_donutchart(5)
    #     if sender == self.sunBtn:
    #         self.create_donutchart(6)
    #
    #     if self.prevSender == sender:
    #         sender.setStyleSheet(
    #             "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
    #             "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
    #             "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
    #             )
    #     self.prevSender = sender
