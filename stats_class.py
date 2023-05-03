import sys, random, sqlite3
import  datetime, os.path
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *

class Statistics(QMainWindow):
    def __init__(self):

        super().__init__()
        self.scene = QGraphicsScene()
        self.view= QGraphicsView(self.scene)
        self.setStyleSheet("background-color: #E5DBE9")
        self.prevSender = None
        self.sqlRequest()
        self.Graph()
        self.create_donutchart(0)
        self.BackLabel()
        self.FrameWeek()
        self.InitWindow()

    def sqlRequest(self):
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS stats(
                tag TEXT,
                time INT,
                week INT,
                year INT,
                month INT,
                day INT,
                data TEXT);
        """)
        self.data_base.commit()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS average (
                lastmin INT,
                lastsec INT,
                thismin INT,
                thissec INT);
            """)
        self.data_base.commit()
        self.data_base.close()

    def InitWindow(self):
        self.setGeometry(650,50,700,762)
        self.setFixedSize(QSize(700,762))
    def BackLabel(self):
        self.backLabel = QLabel("White", self)
        pixmap = QPixmap('source/Cat_1.png')
        self.backLabel.setPixmap(pixmap)
        self.backLabel.setStyleSheet("background-color: transparent")
        self.backLabel.setGeometry(380,520,100,100)

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
        sum_Mon = 0
        sum_Tue = 0
        sum_Wed = 0
        sum_Thu = 0
        sum_Fri = 0
        sum_Sat = 0
        sum_Sun = 0
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
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

        self.data_base.close()
        sum_Mon = sum_sportM + sum_studyM + sum_otherM + sum_workM
        sum_Tue = sum_sportTue + sum_studyTue + sum_otherTue + sum_workTue
        sum_Wed = sum_sportWed + sum_studyWed + sum_otherWed + sum_workWed
        sum_Thu = sum_sportThu + sum_studyThu + sum_otherThu + sum_workThu
        sum_Fri = sum_sportFri + sum_studyFri + sum_otherFri + sum_workFri
        sum_Sat = sum_sportSat + sum_studySat + sum_otherSat + sum_workSat
        sum_Sun = sum_sportSun + sum_studySun + sum_otherSun + sum_workSun
        MaxSum = max(sum_Mon, sum_Tue, sum_Wed, sum_Thu, sum_Fri, sum_Sat, sum_Sun)
        list = [sum_Mon, sum_Tue, sum_Wed, sum_Thu, sum_Fri, sum_Sat, sum_Sun]

        self.chartG.removeSeries(self.seriesG)

        set1 = QBarSet('<b><font color="#FA7F9D">Sport</font></b>')
        set2 = QBarSet('<b><font color="#97ACF9">Work</font></b>')
        set3 = QBarSet('<b><font color="#FADA7F">Study</font></b>')
        set4 = QBarSet('<b><font color="#8CFA9C">Other</font></b>')

        self.seriesG.clear()
        set1.append([sum_sportM, sum_sportTue, sum_sportWed, sum_sportThu, sum_sportFri, sum_sportSat, sum_sportSun])
        set2.append([sum_workM, sum_workTue, sum_workWed, sum_workThu, sum_workFri, sum_workSat, sum_workSun])
        set3.append([sum_studyM, sum_studyTue, sum_studyWed, sum_studyThu, sum_studyFri, sum_studySat, sum_studySun])
        set4.append([sum_otherM, sum_otherTue, sum_otherWed, sum_otherThu, sum_otherFri, sum_otherSat, sum_otherSun])
        set1.setColor(QtGui.QColor("#FA7F9D"))
        set2.setColor(QtGui.QColor("#97ACF9"))
        set3.setColor(QtGui.QColor("#FADA7F"))
        set4.setColor(QtGui.QColor("#8CFA9C"))
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute("SELECT time FROM stats")
        averges = 0
        times = self.cur.fetchall()
        for time in times:
            averges += time[0]
        count = 1
        for i in list:
            print (i)
            if i != 0:
                count += 1
        if(count>1):
            count-=1

        averges = (sum_Mon + sum_Tue + sum_Wed + sum_Thu + sum_Fri + sum_Sat + sum_Sun)/count
        print(count)
        self.data_base.close()
        aver_min = 0
        aver_sec = 0
        if averges < 60:
            aver_sec = averges
            aver_min = 0
            print(aver_sec)
        else:
            aver_min, aver_sec = divmod(averges, 60)
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute("SELECT lastmin, lastsec FROM average")
        lasts = self.cur.fetchone()
        self.data_base.close()
        numbertwo = (aver_min * 60) + aver_sec
        numberone = (lasts[0] * 60) + lasts[1]
        try:
            procent = ((numberone * 100) / numbertwo) - 100
        except ZeroDivisionError:
            procent = 0
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute(f'UPDATE average SET thismin = {int(aver_min)}, thissec = {int(aver_sec)}')
        self.data_base.commit()
        self.data_base.close()
        procent = procent*-1
        print(aver_sec)
        if (procent < 0):
            self.chartG.setTitle(
                f'<b><font face="Inter" size="5" color="#6E6E6E">Daily averageㅤㅤㅤㅤㅤㅤ<img src="source/down_arrow.png"> {int(procent * -1)} % from last week</font></b>'
                f'<br align="left"><b><font face="Inter" size="5" color="#29002F">{int(aver_min)} min {int(aver_sec)} sec </font></b></br>')
        else:
            self.chartG.setTitle(
                f'<b><font face="Inter" size="5" color="#6E6E6E">Daily averageㅤㅤㅤㅤㅤㅤ<img src="source/up_arrow.png"> {int(procent)} % from last week</font></b>'
                f'<br align="left"><b><font face="Inter" size="5" color="#29002F">{int(aver_min)} min {int(aver_sec)} sec </font></b></br>')

        # seriesG = QStackedBarSeries()
        self.seriesG.append(set1)
        self.seriesG.append(set2)
        self.seriesG.append(set3)
        self.seriesG.append(set4)
        self.chartG.removeAxis(self.axisY)
        self.axisY = QValueAxis()
        minY = 0
        maxY = int(MaxSum / 60)

        self.axisY.setRange(minY, maxY)
        self.axisY.setLabelFormat(f'<b><font face="Inter" color="#6E6E6E" size="4">%d min</font></b>')
        self.axisY.setTickCount(3)
        self.axisY.setMinorTickCount(1)

        self.chartG.addAxis(self.axisY, Qt.AlignRight)
        self.chartG.addSeries(self.seriesG)
        self.chartG.update()
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
        sum_Mon = 0
        sum_Tue = 0
        sum_Wed = 0
        sum_Thu = 0
        sum_Fri = 0
        sum_Sat = 0
        sum_Sun = 0
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
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

            self.data_base.close()
        sum_Mon = sum_sportM + sum_studyM + sum_otherM + sum_workM
        sum_Tue = sum_sportTue + sum_studyTue + sum_otherTue + sum_workTue
        sum_Wed = sum_sportWed + sum_studyWed + sum_otherWed + sum_workTue
        sum_Thu = sum_sportThu + sum_studyThu + sum_otherThu + sum_workThu
        sum_Fri = sum_sportFri + sum_studyFri + sum_otherFri + sum_workFri
        sum_Sat = sum_sportSat + sum_studySat + sum_otherSat + sum_workSat
        sum_Sun = sum_sportSun + sum_studySun + sum_otherSun + sum_workSun
        MaxSum = max(sum_Mon, sum_Tue, sum_Wed, sum_Thu, sum_Fri, sum_Sat, sum_Sun)

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

        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute("SELECT time FROM stats")
        averges = 0
        times = self.cur.fetchall()
        for time in times:
            averges += time[0]
        # averges /= datetime.date.today().weekday()+1
        # averges = max(sum_Mon, sum_Tue, sum_Wed, sum_Thu, sum_Fri, sum_Sat, sum_Sun)
        averges = (sum_Mon + sum_Tue + sum_Wed + sum_Thu + sum_Fri + sum_Sat + sum_Sun)/7
        self.data_base.close()
        if averges < 60:
            aver_sec = averges
            aver_min = 0
        else:
            aver_min, aver_sec = divmod(averges, 60)

        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute("SELECT lastmin, lastsec FROM average")
        lasts = self.cur.fetchone()
        self.data_base.close()
        numbertwo = (aver_min * 60) + aver_sec
        numberone = (lasts[0] * 60) + lasts[1]
        try:
            procent = ((numberone * 100) / numbertwo) - 100
        except ZeroDivisionError:
            procent = 0
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute(f'UPDATE average SET thismin = {int(aver_min)}, thissec = {int(aver_sec)}')
        self.data_base.commit()
        self.data_base.close()

        self.chartG = QChart()
        self.chartG.setMaximumSize(700, 400)
        self.chartG.addSeries(self.seriesG)
        procent = procent*-1
        if (procent < 0):
            self.chartG.setTitle(
                f'<b><font face="Inter" size="5" color="#6E6E6E">Daily averageㅤㅤㅤㅤㅤㅤ<img src="source/down_arrow.png"> {int(procent * -1)} % from last week</font></b>'
                f'<br align="left"><b><font face="Inter" size="5" color="#29002F">{int(aver_min)} min {int(aver_sec)} sec </font></b></br>')
        else:
            self.chartG.setTitle(
                f'<b><font face="Inter" size="5" color="#6E6E6E">Daily averageㅤㅤㅤㅤㅤㅤ<img src="source/up_arrow.png"> {int(procent)} % from last week</font></b>'
                f'<br align="left"><b><font face="Inter" size="5" color="#29002F">{int(aver_min)} min {int(aver_sec)} sec </font></b></br>')
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
        self.axisY = QValueAxis()
        minY = 0
        maxY = int(MaxSum/60)

        self.axisY.setRange(minY, maxY)
        self.axisY.setLabelFormat(f'<b><font face="Inter" color="#6E6E6E" size="4">%d min</font></b>')
        self.axisY.setTickCount(3)
        self.axisY.setMinorTickCount(1)

        self.chartG.addAxis(axisX, Qt.AlignBottom)
        self.chartG.addAxis(self.axisY, Qt.AlignRight)
        self.chartG.legend().setVisible(True)
        self.chartG.legend().setFont(QtGui.QFont('Arial', 12))
        self.chartG.legend().setAlignment(Qt.AlignBottom)
        self.chartG.legend().setMarkerShape(2)

        self.chartViewG = QChartView(self.chartG, self)
        self.chartViewG.setGeometry(0, 0, 580, 318)
        self.chartViewG.move(60, 32)
        self.chartViewG.update()



    def create_donutchart(self, week):
        sum_work = 0
        sum_sport = 0
        sum_other = 0
        sum_study = 0
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
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
        self.data_base.close()
            # print(row[0], row[1], row[2])
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

    def UpdateFullStats(self):
        self.updateGraph()
        week = datetime.date.today().weekday()
        print(week)
        self.series.clear()
        sum_work = 0
        sum_sport = 0
        sum_other = 0
        sum_study = 0
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
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
        self.data_base.close()
        #     print(row[0], row[1], row[2])
        minute_work, seconds_work = divmod(sum_work, 60)
        minute_study, seconds_study = divmod(sum_study, 60)
        minute_sport, seconds_sport = divmod(sum_sport, 60)
        minute_other, seconds_other = divmod(sum_other, 60)

        self.series.append(f'<b><font color="#FA7F9D">Sport {minute_sport}m {seconds_sport}s</font></b>',
                           sum_sport).setColor(QtGui.QColor("#FA7F9D"))
        self.series.append(f'<b><font color="#97ACF9">Work {minute_work}m {seconds_work}s</font></b>',
                           sum_work).setColor(QtGui.QColor("#97ACF9"))
        self.series.append(f'<b><font color="#FADA7F">Study {minute_study}m {seconds_study}s</font></b>',
                           sum_study).setColor(QtGui.QColor("#FADA7F"))
        self.series.append(f'<b><font color="#8CFA9C">Other {minute_other}m {seconds_other}s</font></b>',
                           sum_other).setColor(QtGui.QColor("#8CFA9C"))
        self.series.setHoleSize(0.4)
        self.chartview.update()

        week = datetime.date.today().weekday()
        self.prevSender.setStyleSheet(
            "QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
            "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
            "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
        )
        if week == 0:
            self.monBtn.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
            self.prevSender = self.monBtn
        if week == 1:
            self.tueBtn.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
            self.prevSender = self.tueBtn
        if week == 2:
            self.wedBtn.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
            self.prevSender = self.wedBtn
        if week == 3:
            self.thuBtn.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
            self.prevSender = self.thuBtn
        if week == 4:
            self.friBtn.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
            self.prevSender = self.friBtn
        if week == 5:
            self.satBtn.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
            self.prevSender = self.satBtn
        if week == 6:
            self.sunBtn.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
            self.prevSender = self.sunBtn

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
            # self.backLabel.setGeometry(377,520,100,100)
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
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
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
        self.data_base.close()
       #     print(row[0], row[1], row[2])
        minute_work, seconds_work = divmod(sum_work, 60)
        minute_study, seconds_study = divmod(sum_study, 60)
        minute_sport, seconds_sport = divmod(sum_sport, 60)
        minute_other, seconds_other = divmod(sum_other, 60)

        self.series.append(f'<b><font color="#FA7F9D">Sport {minute_sport}m {seconds_sport}s</font></b>', sum_sport).setColor(QtGui.QColor("#FA7F9D"))
        self.series.append(f'<b><font color="#97ACF9">Work {minute_work}m {seconds_work}s</font></b>', sum_work).setColor(QtGui.QColor("#97ACF9"))
        self.series.append(f'<b><font color="#FADA7F">Study {minute_study}m {seconds_study}s</font></b>', sum_study).setColor(QtGui.QColor("#FADA7F"))
        self.series.append(f'<b><font color="#8CFA9C">Other {minute_other}m {seconds_other}s</font></b>', sum_other).setColor(QtGui.QColor("#8CFA9C"))
        self.series.setHoleSize(0.4)
        self.updateGraph()
        self.chartview.update()


    def FrameWeek(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setGeometry(66,370,568,36)
        frame.setStyleSheet("background-color:#A597AB; border-radius: 10px")

        week = datetime.date.today().weekday()


        self.monBtn = QPushButton('mon', self)
        self.monBtn.setGeometry(73,374,79,28)
        self.monBtn.setStyleSheet("QPushButton{background-color:transparent; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
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
        self.sunBtn.clicked.connect(self.updateChart)
        self.monBtn.clicked.connect(self.updateChart)
        self.tueBtn.clicked.connect(self.updateChart)
        self.wedBtn.clicked.connect(self.updateChart)
        self.thuBtn.clicked.connect(self.updateChart)
        self.satBtn.clicked.connect(self.updateChart)
        self.friBtn.clicked.connect(self.updateChart)
        if week == 0:
            self.monBtn.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
            self.prevSender = self.monBtn
        if week == 1:
            self.tueBtn.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
            self.prevSender = self.tueBtn
        if week == 2:
            self.wedBtn.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
            self.prevSender = self.wedBtn
        if week == 3:
            self.thuBtn.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
            self.prevSender = self.thuBtn
        if week == 4:
            self.friBtn.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
            self.prevSender = self.friBtn
        if week == 5:
            self.satBtn.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
            self.prevSender = self.satBtn
        if week == 6:
            self.sunBtn.setStyleSheet(
                "QPushButton{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:hover{background-color:#ffffff; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}"
                "QPushButton:pressed{background-color:#8a8189; border-radius: 4px; font: bold 24px; font-family: Inter; color:#29002F}")
            self.prevSender = self.sunBtn
