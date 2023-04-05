import sys, random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *
import datetime, sqlite3
from MyItem import MyItem
from Money import Money_lable
class Timer(QMainWindow):
    def __init__(self):

        super().__init__()
        self.scene = QGraphicsScene()
        self.view= QGraphicsView(self.scene)
        self.setStyleSheet("background-color: #E5DBE9")

        self.prevSenderTag = None
        print (datetime.date.today().weekday())

        self.Frame_Timer()
        self.CreateTimer()
        self.choose_tag()
        self.sqlRequest()
        self.money_tag()
        self.Timer()
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
        self.data_base.close()
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS money(
                money INT);
        """)
        self.data_base.commit()
        self.data_base.close()

    def money_tag(self):
        self.data_base = sqlite3.connect("details.db")
        self.cur = self.data_base.cursor()
        self.cur.execute("SELECT money FROM money")
        money = self.cur.fetchone()
        self.data_base.close()
        self.money = Money_lable()
        self.money.setParent(self)
        self.money.setGeometry(600, 7, 98, 41)
        self.money.setStyleSheet("background:transparent")
        if money[0] >= 100 and money[0] <= 999:
            self.money.setGeometry(600,7,93,41)
        if money[0] < 100:
            self.money.setGeometry(626,7,67,41)
        if money[0] > 999:
            self.money.setGeometry(596,7,97,41)
        if money[0] > 9999:
            self.money.setGeometry(582,7,111,41)

    def Timer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.updateMoney)
        timer.start(1000)

    def updateMoney(self):
        self.money.updateM()
        # self.money.setIcon(QIcon("source/Coin.png"))
        # self.money.setLayoutDirection(Qt.RightToLeft)
        # self.money.setText(str(money[0]))
        # self.moneyLable.setStyleSheet("background: #8350AA; border-radius: 20px; font-family: Inter; font:bold 24px; color: #FFFFFF; padding: 0 0px 0 0px;line-height: 15px;")
        # self.moneyLable.setText(f'<p align="center" style="text-align: middle;"><h2><font size="3">{str(money[0])}</font></h2></p> <img src = "source/Coin.png" width="22" height="22" align="middle" hspace="100">')
        # self.moneyLable.setText(f'{money[0]} <img src = "source/Coin.png" align="middle">')
        # self.money.setStyleSheet("background: #8350AA;border-radius: 20px;font-family: 'Inter'; font-style: normal; color:#ffffff; font-weight: 700; font-size: 22px; line-height: 15px; text-align: center;padding: 0px 10px 0px 5px;")
        # self.money.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # if money[0]<100:
        #     self.money.setGeometry(626, 7, 67, 41)
        # if money[0]>999:
        #     self.money.setGeometry(596, 7, 97, 41)
        # if money[0]>9999:
        #     self.money.setGeometry(582,7,111,41)
    def choose_tag(self):
        self.labelTag = QLabel(self)
        self.labelTag.setGeometry(183,590,333,92)
        self.labelTag.setStyleSheet("background: #ffffff; border-radius: 40px;")
        self.label_1 = QLabel('Choose \n   a tag',self)
        self.label_1.setGeometry(62,613,95,58)
        self.label_1.setStyleSheet("font-family: Inter; font:bold 24px")
        pixmap = QPixmap('source/Arrow.png')
        self.pic_label = QLabel(self)
        self.pic_label.setPixmap(pixmap)
        self.pic_label.setGeometry(100,570,85,40)

        self.label_work = QPushButton('work', self)
        self.label_work.setGeometry(267,610, 60, 24)
        self.label_work.setStyleSheet("background:transparent; font: bold 20px; font-family:Inter;")
        self.label_study = QPushButton('study', self)
        self.label_study.setGeometry(267,647,60,24)
        self.label_study.setStyleSheet("background:transparent; font: bold 20px; font-family:Inter")
        self.label_sport = QPushButton('sport', self)
        self.label_sport.setGeometry(407,610,60,24)
        self.label_sport.setStyleSheet("background:transparent; font: bold 20px; font-family:Inter")
        self.label_other = QPushButton('other', self)
        self.label_other.setGeometry(407,647,60,24)
        self.label_other.setStyleSheet("background:transparent; font: bold 20px; font-family:Inter")

        self.btnGroup = QButtonGroup(self)
        self.btnGroup.addButton(self.label_work)
        self.btnGroup.addButton(self.label_study)
        self.btnGroup.addButton(self.label_other)
        self.btnGroup.addButton(self.label_sport)

        self.label_work_circle = QLabel(self)
        self.label_work_circle.setGeometry(239,619,10,10)
        self.label_work_circle.setStyleSheet("background:#8350AA; border-radius:5px")
        self.label_study_circle = QLabel(self)
        self.label_study_circle.setGeometry(239,655,10,10)
        self.label_study_circle.setStyleSheet("background:#979797; border-radius:5px")
        self.label_sport_circle = QLabel(self)
        self.label_sport_circle.setGeometry(379,619,10,10)
        self.label_sport_circle.setStyleSheet("background:#979797; border-radius:5px")
        self.label_other_circle = QLabel(self)
        self.label_other_circle.setGeometry(379,655,10,10)
        self.label_other_circle.setStyleSheet("background:#979797; border-radius:5px")
        self.prevSenderTag = self.label_work

        self.label_work.clicked.connect(self.Action_Tag)
        self.label_study.clicked.connect(self.Action_Tag)
        self.label_sport.clicked.connect(self.Action_Tag)
        self.label_other.clicked.connect(self.Action_Tag)


    def Action_Tag(self):
        sender = self.sender()
        self.prevSenderTag = sender
        if sender == self.label_sport:
            self.label_sport_circle.setStyleSheet("background:#8350AA; border-radius:5px")
            self.label_other_circle.setStyleSheet("background:#979797; border-radius:5px")
            self.label_study_circle.setStyleSheet("background:#979797; border-radius:5px")
            self.label_work_circle.setStyleSheet("background:#979797; border-radius:5px")
        if sender == self.label_study:
            self.label_study_circle.setStyleSheet("background:#8350AA; border-radius:5px")
            self.label_other_circle.setStyleSheet("background:#979797; border-radius:5px")
            self.label_sport_circle.setStyleSheet("background:#979797; border-radius:5px")
            self.label_work_circle.setStyleSheet("background:#979797; border-radius:5px")
        if sender == self.label_work:
            self.label_work_circle.setStyleSheet("background:#8350AA; border-radius:5px")
            self.label_other_circle.setStyleSheet("background:#979797; border-radius:5px")
            self.label_study_circle.setStyleSheet("background:#979797; border-radius:5px")
            self.label_sport_circle.setStyleSheet("background:#979797; border-radius:5px")
        if sender == self.label_other:
            self.label_other_circle.setStyleSheet("background:#8350AA; border-radius:5px")
            self.label_sport_circle.setStyleSheet("background:#979797; border-radius:5px")
            self.label_study_circle.setStyleSheet("background:#979797; border-radius:5px")
            self.label_work_circle.setStyleSheet("background:#979797; border-radius:5px")


    def Frame_Timer(self):
        self.bigEllipse = QLabel(self)
        self.bigEllipse.setGeometry(138, 14, 428, 428)
        self.bigEllipse.setStyleSheet("background:#BB89D9; border-radius:214px;")
        self.smallEllipse = QLabel(self)
        self.smallEllipse.setGeometry(160,36,384,384)
        self.smallEllipse.setStyleSheet("background:#E5DBE9; border-radius:190px;")

        self.pic_label_timer = QLabel(self)
        pixmap = QPixmap('source/cat_with_big_balls.png')
        self.pic_label_timer.setStyleSheet("background:transparent")
        self.pic_label_timer.setPixmap(pixmap)
        self.pic_label_timer.setGeometry(209, 90, 285, 254)

    def CreateTimer(self):
        self.start = False
        self.count = 0
        self.sliderTimer = QSlider(Qt.Horizontal, self)
        self.sliderTimer.move(70, 150)
        self.sliderTimer.setRange(0, 7200)
        self.sliderTimer.valueChanged.connect(self.UpdateLabel)
        self.sliderTimer.setSingleStep(60)
        self.sliderTimer.setTickInterval(60)
        self.sliderTimer.setPageStep(60)
        self.sliderTimer.setGeometry(211, 430, 280, 15)
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
        self.lableTimer = QLabel("00:00", self)
        self.lableTimer.setFont(QtGui.QFont('Inter', 20))
        self.lableTimer.setAlignment(Qt.AlignCenter)
        self.lableTimer.setStyleSheet("color:#8350AA; font-family: Inter; font-weight:bold;")
        self.lableTimer.setGeometry(298, 358, 115, 36)

        self.start_sound = QSound('source/1.wav', self)
        self.start_btn = QPushButton("Start", self)
        self.start_btn.setGeometry(208, 500, 127, 50)
        self.start_btn.clicked.connect(self.start_action)
        self.start_btn.clicked.connect(self.start_sound.play)
        self.start_btn.setStyleSheet("border-radius: 25px; background-color:#9CC152; color:#ffffff; "
                                     "font-family:Inter; font:24px; font-weight:bold;")

        self.stop_btn = QPushButton("Stop", self)
        self.stop_btn.move(70, 250)
        self.stop_btn.setGeometry(365, 500, 127, 50)
        self.stop_btn.clicked.connect(self.stop_action)
        self.stop_btn.setStyleSheet("border-radius: 25px; background-color:#FA7B7B; color:#ffffff; "
                                    "font-family:Inter; font:24px; font-weight:bold")
        self.stop_btn.setDisabled(True)

        self.timer = QTimer(self)
        self.time = QTime(0, 0, 0)
        self.timer.timeout.connect(self.showTime)

    def showTime(self):
        if self.start:
            self.count -= 1
            m, s = divmod(self.count, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.lableTimer.setText(str(min_sec_format))
            if self.count == 0:
                self.lableTimer.setText("00:00")
                self.start = False
                if self.prevSenderTag == self.label_work:
                    name_tag = 'work'
                if self.prevSenderTag == self.label_sport:
                    name_tag = 'sport'
                if self.prevSenderTag == self.label_other:
                    name_tag = 'other'
                if self.prevSenderTag == self.label_study:
                    name_tag = 'study'
                details = (name_tag, self.all_count_timer - self.count, datetime.date.today().weekday(),datetime.date.today().year, datetime.date.today().month, datetime.date.today().day,datetime.date.today())
                self.data_base = sqlite3.connect('details.db')
                self.cur = self.data_base.cursor()
                self.cur.execute("INSERT INTO stats VALUES(?, ?, ?, ?, ?, ?, ?);", details)
                self.data_base.commit()
                self.data_base.close()

                self.data_base = sqlite3.connect("details.db")
                self.cur = self.data_base.cursor()
                self.cur.execute('SELECT money FROM money')
                temp = self.cur.fetchone()
                self.data_base.close()
                time = self.all_count_timer - self.count
                money = temp[0]
                # обработка начисления монет
                if(time<=3600):
                    money = money + 0.05*time
                elif(time>3600):
                    money = money + 180 + (time - 3600)*0.1
                self.data_base = sqlite3.connect("details.db")
                self.cur = self.data_base.cursor()
                self.cur.execute(f'UPDATE money SET money={int(money)}')
                self.data_base.commit()
                self.data_base.close()

                self.sliderTimer.setEnabled(True)
                self.start_btn.setEnabled(True)
                self.animationTimer = QPropertyAnimation(self.lableTimer, b"geometry")
                self.animationTimer.setDuration(1000)
                self.animationTimer.setStartValue(QRect(298, 408, 115, 36))
                self.animationTimer.setEndValue(QRect(298, 358, 115, 36))
                self.animationTimer.start()

                self.anmationStartBtn = QPropertyAnimation(self.start_btn, b"geometry")
                self.anmationStartBtn.setDuration(1000)
                self.anmationStartBtn.setStartValue(QRect(208, 550, 127, 50))
                self.anmationStartBtn.setEndValue(QRect(208, 500, 127, 50))
                self.anmationStartBtn.start()

                self.animationStopBtn = QPropertyAnimation(self.stop_btn, b"geometry")
                self.animationStopBtn.setDuration(1000)
                self.animationStopBtn.setStartValue(QRect(365, 550, 127, 50))
                self.animationStopBtn.setEndValue(QRect(365, 500, 127, 50))
                self.animationStopBtn.start()

                self.animationSliderTimer = QPropertyAnimation(self.sliderTimer, b"geometry")
                self.animationSliderTimer.setDuration(1000)
                self.animationSliderTimer.setStartValue(QRect(211, 480, 280, 15))
                self.animationSliderTimer.setEndValue(QRect(211, 430, 280, 15))
                self.animationSliderTimer.start()

                self.animationSmallLabelTimer = QPropertyAnimation(self.smallEllipse, b"geometry")
                self.animationSmallLabelTimer.setDuration(1000)
                self.animationSmallLabelTimer.setStartValue(QRect(160, 86, 384, 384))
                self.animationSmallLabelTimer.setEndValue(QRect(160, 36, 384, 384))
                self.animationSmallLabelTimer.start()

                self.animationBigLabelTimer = QPropertyAnimation(self.bigEllipse, b"geometry")
                self.animationBigLabelTimer.setDuration(1000)
                self.animationBigLabelTimer.setStartValue(QRect(138, 64, 428, 428))
                self.animationBigLabelTimer.setEndValue(QRect(138, 14, 428, 428))
                self.animationBigLabelTimer.start()

                self.movie.stop()
                self.pic_label_timer.setPixmap(QPixmap('source/cat_with_big_balls.png'))

                self.animationPicLabelTimer = QPropertyAnimation(self.pic_label_timer, b"geometry")
                self.animationPicLabelTimer.setDuration(1000)
                self.animationPicLabelTimer.setStartValue(QRect(209, 140, 285, 254))
                self.animationPicLabelTimer.setEndValue(QRect(209, 90, 285, 254))
                self.animationPicLabelTimer.start()

                self.labelTag.show()
                self.label_work.show()
                self.label_sport.show()
                self.label_other.show()
                self.label_study.show()
                self.label_other_circle.show()
                self.label_work_circle.show()
                self.label_study_circle.show()
                self.label_sport_circle.show()
                self.label_1.show()
                self.pic_label.show()
                # self.money.setText(str(int(money)))
                self.stop_btn.setDisabled(True)

    def start_action(self):
        if self.count != 0:
            # 0 - Monday(Понедельник);
            # 1 - Tuesday(Вторник);
            # 2 - Wednesday(Среда);
            # 3 - Thursday(Четверг);
            # 4 - Friday(Пятница);
            # 5 - Saturday(Суббота);
            # 6 - Sunday(Воскресенье).
            print(datetime.date.today().weekday())
            self.all_count_timer = self.count
            self.timer.start(1000)
            self.sliderTimer.setEnabled(False)
            self.start_btn.setEnabled(False)
            self.stop_btn.setDisabled(False)
            #дичь лютая
            self.lableTimer.setGeometry(298,358,115,36)
            self.animationTimer = QPropertyAnimation(self.lableTimer, b"geometry")
            self.animationTimer.setDuration(1000)
            self.animationTimer.setStartValue(QRect(298, 358, 115, 36))
            self.animationTimer.setEndValue(QRect(298, 408, 115, 36))
            self.animationTimer.start()

            self.anmationStartBtn = QPropertyAnimation(self.start_btn, b"geometry")
            self.anmationStartBtn.setDuration(1000)
            self.anmationStartBtn.setStartValue(QRect(208, 500, 127, 50))
            self.anmationStartBtn.setEndValue(QRect(208, 550, 127, 50))
            self.anmationStartBtn.start()

            self.animationStopBtn = QPropertyAnimation(self.stop_btn, b"geometry")
            self.animationStopBtn.setDuration(1000)
            self.animationStopBtn.setStartValue(QRect(365,500,127,50))
            self.animationStopBtn.setEndValue(QRect(365, 550, 127, 50))
            self.animationStopBtn.start()

            self.animationSliderTimer = QPropertyAnimation(self.sliderTimer, b"geometry")
            self.animationSliderTimer.setDuration(1000)
            self.animationSliderTimer.setStartValue(QRect(211, 430, 280, 15))
            self.animationSliderTimer.setEndValue(QRect(211, 480, 280, 15))
            self.animationSliderTimer.start()

            self.animationSmallLabelTimer = QPropertyAnimation(self.smallEllipse, b"geometry")
            self.animationSmallLabelTimer.setDuration(1000)
            self.animationSmallLabelTimer.setStartValue(QRect(160,36,384,384))
            self.animationSmallLabelTimer.setEndValue(QRect(160,86,384,384))
            self.animationSmallLabelTimer.start()

            self.animationBigLabelTimer = QPropertyAnimation(self.bigEllipse, b"geometry")
            self.animationBigLabelTimer.setDuration(1000)
            self.animationBigLabelTimer.setStartValue(QRect(138, 14, 428, 428))
            self.animationBigLabelTimer.setEndValue(QRect(138, 64, 428, 428))
            self.animationBigLabelTimer.start()

            self.movie = QMovie('source/2.gif')
            self.pic_label_timer.setMovie(self.movie)
            self.movie.start()

            self.animationPicLabelTimer = QPropertyAnimation(self.pic_label_timer, b"geometry")
            self.animationPicLabelTimer.setDuration(1000)
            self.animationPicLabelTimer.setStartValue(QRect(209, 90, 285, 254))
            self.animationPicLabelTimer.setEndValue(QRect(209, 140, 285, 254))
            self.animationPicLabelTimer.start()
            #***********************************
            self.start = True
            print(self.start)
            print(self.count)
            self.labelTag.hide()
            self.label_work.hide()
            self.label_sport.hide()
            self.label_other.hide()
            self.label_study.hide()
            self.label_other_circle.hide()
            self.label_work_circle.hide()
            self.label_study_circle.hide()
            self.label_sport_circle.hide()
            self.label_1.hide()
            self.pic_label.hide()
            if self.count == 0:
                self.start = False

    def stop_action(self):
        self.start = False
        if self.prevSenderTag == self.label_work:
            name_tag = 'work'
        if self.prevSenderTag == self.label_sport:
            name_tag = 'sport'
        if self.prevSenderTag == self.label_other:
            name_tag = 'other'
        if self.prevSenderTag == self.label_study:
            name_tag = 'study'
        details = (name_tag,self.all_count_timer - self.count, datetime.date.today().weekday(), datetime.date.today().year, datetime.date.today().month, datetime.date.today().day,datetime.date.today())
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute("INSERT INTO stats VALUES(?, ?, ?, ?, ?, ?, ?);", details)
        self.data_base.commit()
        self.data_base.close()

        self.data_base = sqlite3.connect("details.db")
        self.cur = self.data_base.cursor()
        self.cur.execute('SELECT money FROM money')
        temp = self.cur.fetchone()
        self.data_base.close()
        time = self.all_count_timer - self.count
        money = temp[0]
        print(f'time = {time}')
        # обработка начисления монет
        if (time <= 3600):
            print("зашел в первый if")
            money = money+ 0.05 * time
        elif (time > 3600):
            money = money + 180 + (time - 3600) * 0.1

        self.data_base = sqlite3.connect("details.db")
        self.cur = self.data_base.cursor()
        self.cur.execute(f'UPDATE money SET money={int(money)}')
        self.data_base.commit()
        self.data_base.close()


        self.sliderTimer.setEnabled(True)
        self.start_btn.setEnabled(True)
        self.sliderTimer.setValue(0)
        self.timer.stop()
        #***************************
        self.animationTimer = QPropertyAnimation(self.lableTimer, b"geometry")
        self.animationTimer.setDuration(1000)
        self.animationTimer.setStartValue(QRect(298, 408, 115, 36))
        self.animationTimer.setEndValue(QRect(298, 358, 115, 36))
        self.animationTimer.start()

        self.anmationStartBtn = QPropertyAnimation(self.start_btn, b"geometry")
        self.anmationStartBtn.setDuration(1000)
        self.anmationStartBtn.setStartValue(QRect(208, 550, 127, 50))
        self.anmationStartBtn.setEndValue(QRect(208, 500, 127, 50))
        self.anmationStartBtn.start()

        self.animationStopBtn = QPropertyAnimation(self.stop_btn, b"geometry")
        self.animationStopBtn.setDuration(1000)
        self.animationStopBtn.setStartValue(QRect(365, 550, 127, 50))
        self.animationStopBtn.setEndValue(QRect(365, 500, 127, 50))
        self.animationStopBtn.start()

        self.animationSliderTimer = QPropertyAnimation(self.sliderTimer, b"geometry")
        self.animationSliderTimer.setDuration(1000)
        self.animationSliderTimer.setStartValue(QRect(211, 480, 280, 15))
        self.animationSliderTimer.setEndValue(QRect(211, 430, 280, 15))
        self.animationSliderTimer.start()

        self.animationSmallLabelTimer = QPropertyAnimation(self.smallEllipse, b"geometry")
        self.animationSmallLabelTimer.setDuration(1000)
        self.animationSmallLabelTimer.setStartValue(QRect(160, 86, 384, 384))
        self.animationSmallLabelTimer.setEndValue(QRect(160, 36, 384, 384))
        self.animationSmallLabelTimer.start()

        self.animationBigLabelTimer = QPropertyAnimation(self.bigEllipse, b"geometry")
        self.animationBigLabelTimer.setDuration(1000)
        self.animationBigLabelTimer.setStartValue(QRect(138, 64, 428, 428))
        self.animationBigLabelTimer.setEndValue(QRect(138, 14, 428, 428))
        self.animationBigLabelTimer.start()

        self.movie.stop()
        self.pic_label_timer.setPixmap(QPixmap('source/cat_with_big_balls.png'))
        self.animationPicLabelTimer = QPropertyAnimation(self.pic_label_timer, b"geometry")
        self.animationPicLabelTimer.setDuration(1000)
        self.animationPicLabelTimer.setStartValue(QRect(209, 140, 285, 254))
        self.animationPicLabelTimer.setEndValue(QRect(209, 90, 285, 254))
        self.animationPicLabelTimer.start()
        #***************************
        self.labelTag.show()
        self.label_work.show()
        self.label_sport.show()
        self.label_other.show()
        self.label_study.show()
        self.label_other_circle.show()
        self.label_work_circle.show()
        self.label_study_circle.show()
        self.label_sport_circle.show()
        self.label_1.show()
        self.pic_label.show()
        self.count = 0
        # self.money.setText(str(int(money)))
        self.stop_btn.setDisabled(True)
        # self.money_tag()
        # self.update()
        # self.moneyLable.update()
        # self.thread = MyThread()
        # self.thread.mySignal.connect(self.money_tag)
        # self.thread.start()

    def UpdateLabel(self, value):
        self.count = value
        m, s = divmod(self.count, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        self.lableTimer.setText(str(min_sec_format))
        print(self.count)

    def InitWindow(self):
        self.setGeometry(650, 50, 700, 762)
        self.setFixedSize(QSize(700, 762))

# class MyThread(QtCore.QThread):
#     mySignal = QtCore.pyqtSignal(int)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__()
#         self.val = 0
#
#     def run(self):
#         while True:
#             self.val += 1  # Получаем определённые данные
#             self.mySignal.emit(self.val)  # Передаем данные для отображения
#             QtCore.QThread.msleep(1)