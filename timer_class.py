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

        self.prevSenderTag = None
        self.CreateTimer()
        self.Frame_Timer()
        # self.Task_list()
        self.choose_tag()
        self.InitWindow()

    # def Task_list(self):
    #
    #     lable = QLabel("Task list", self)
    #     lable.setGeometry(51, 575, 127, 50)
    #     lable.setAlignment(Qt.AlignCenter)
    #     lable.setStyleSheet("background-color:#8350AA;border-radius:25px;font:24px;font-family:Inter;"
    #                         "font-weight:bold;color:#ffffff;")
    #
    #     list1 = QLineEdit(self)
    #     list1.setGeometry(51, 632, 598, 50)
    #     list1.setStyleSheet("background-color:#ffffff; border-radius:25px; font-family: Inter; font:18px;"
    #                         "padding: 0 40px; font-weight:bold;")
    #     list2 = QLineEdit(self)
    #     list2.setGeometry(51, 689, 598, 50)
    #     list2.setStyleSheet("background-color:#ffffff; border-radius:25px; font-family: Inter; font:18px;"
    #                         "padding: 0 40px; font-weight:bold;")
    #     lableCircle1 = QLabel(self)
    #     lableCircle1.setGeometry(69, 652, 9, 9)
    #     lableCircle1.setStyleSheet("background-color:#8350AA; border-radius:4px")
    #
    #     lableCircle2 = QLabel(self)
    #     lableCircle2.setGeometry(69, 709, 9, 9)
    #     lableCircle2.setStyleSheet("background-color:#8350AA; border-radius:4px")

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
    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     painter.setRenderHint(QPainter.Antialiasing)
    #     pen = QPen(QColor(187, 137, 217), 20, Qt.SolidLine, Qt.FlatCap)
    #     painter.setPen(pen)
    #     painter.setBrush(QColor(229, 219, 233))
    #     painter.drawEllipse(146, 20, 407, 407)
    #     if self.sender == self.start_btn:
    #         self.animationPainter = QPropertyAnimation(painter, b"geometry")
    #         self.animationPainter.setDuration(1000)
    #         self.animationPainter.setStartValue(QRect(146, 20, 407, 407))
    #         self.animationPainter.setEndValue(QRect(146, 70, 407, 407))
    #         self.animationPainter.start()


    def Frame_Timer(self):
        pic_lable = QLabel(self)
        pixmap = QPixmap('source/Time_Cat.png')
        pic_lable.setPixmap(pixmap)
        pic_lable.setGeometry(246, 60, 197, 254)

        self.ellipse = QtWidgets.QGraphicsEllipseItem()
        self.ellipse.setRect(146,20,407,407)
        pen = QPen(QColor(187, 137, 217), 20, Qt.SolidLine, Qt.FlatCap)
        self.ellipse.setPen(pen)
        self.ellipse.setBrush(QColor(229, 219, 233))

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

        self.start_btn = QPushButton("Start", self)
        self.start_btn.setGeometry(208, 500, 127, 50)
        self.start_btn.clicked.connect(self.start_action)
        self.start_btn.setStyleSheet("border-radius: 25px; background-color:#9CC152; color:#ffffff; "
                                     "font-family:Inter; font:24px; font-weight:bold")

        self.stop_btn = QPushButton("Stop", self)
        self.stop_btn.move(70, 250)
        self.stop_btn.setGeometry(365, 500, 127, 50)
        self.stop_btn.clicked.connect(self.stop_action)
        self.stop_btn.setStyleSheet("border-radius: 25px; background-color:#FA7B7B; color:#ffffff; "
                                    "font-family:Inter; font:24px; font-weight:bold")

        self.timer = QTimer(self)
        self.time = QTime(0, 0, 0)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

    def showTime(self):
        if self.start:
            self.count -= 1
            m, s = divmod(self.count, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.lableTimer.setText(str(min_sec_format))
            if self.count == 0:
                self.lableTimer.setText("00:00")
                self.start = False
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

    def start_action(self):
        self.sender = self.sender()
        #дичь лютая
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
        # self.lableTimer.move(298,400)
        # i = 358
        # while i != 500:
        #     self.lableTimer.move(298,i)
        if self.count == 0:
            self.start = False

    def stop_action(self):
        self.start = False
        self.count = 0
        self.sliderTimer.setValue(0)
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

    def UpdateLabel(self, value):
        self.count = value
        m, s = divmod(self.count, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        self.lableTimer.setText(str(min_sec_format))
        print(self.count)

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(650,50,700,762)
        self.setFixedSize(QSize(700,762))
