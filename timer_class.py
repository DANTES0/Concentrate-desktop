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
        self.CreateTimer()
        self.Frame_Timer()
        self.Task_list()
        self.InitWindow()

    def Task_list(self):

        lable = QLabel("Task list", self)
        lable.setGeometry(51, 575, 127, 50)
        lable.setAlignment(Qt.AlignCenter)
        lable.setStyleSheet("background-color:#8350AA;border-radius:25px;font:24px;font-family:Inter;"
                            "font-weight:bold;color:#ffffff;")

        list1 = QLineEdit(self)
        list1.setGeometry(51, 632, 598, 50)
        list1.setStyleSheet("background-color:#ffffff; border-radius:25px; font-family: Inter; font:18px;"
                            "padding: 0 40px; font-weight:bold;")
        list2 = QLineEdit(self)
        list2.setGeometry(51, 689, 598, 50)
        list2.setStyleSheet("background-color:#ffffff; border-radius:25px; font-family: Inter; font:18px;"
                            "padding: 0 40px; font-weight:bold;")
        lableCircle1 = QLabel(self)
        lableCircle1.setGeometry(69, 652, 9, 9)
        lableCircle1.setStyleSheet("background-color:#8350AA; border-radius:4px")

        lableCircle2 = QLabel(self)
        lableCircle2.setGeometry(69, 709, 9, 9)
        lableCircle2.setStyleSheet("background-color:#8350AA; border-radius:4px")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor(187, 137, 217), 20, Qt.SolidLine, Qt.FlatCap)
        painter.setPen(pen)
        painter.setBrush(QColor(229, 219, 233))
        painter.drawEllipse(146, 20, 407, 407)

    def Frame_Timer(self):
        pic_lable = QLabel(self)
        pixmap = QPixmap('source/Time_Cat.png')
        pic_lable.setPixmap(pixmap)
        pic_lable.setGeometry(246, 60, 197, 254)

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
        self.lable = QLabel("00:00", self)
        self.lable.setFont(QtGui.QFont('Inter', 20))
        self.lable.setAlignment(Qt.AlignCenter)
        self.lable.setStyleSheet("color:#8350AA; font-family: Inter; font-weight:bold;")
        self.lable.setGeometry(298, 358, 115, 36)

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

    def UpdateLabel(self, value):
        self.count = value
        m, s = divmod(self.count, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        self.lable.setText(str(min_sec_format))

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(650,50,700,762)
        self.setFixedSize(QSize(700,762))
