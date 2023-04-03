import sys, random, sqlite3
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
import  datetime, os.path
from PyQt5.QtCore import *
from stats_class import Statistics
from timer_class import Timer
from catRoom_class import CatRoom
from Task_class import Task

import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class SlidingStackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        super(SlidingStackedWidget, self).__init__(parent)

        self.m_direction = Qt.Horizontal
        self.m_speed = 500
        self.m_animationtype = QEasingCurve.OutCubic
        self.m_now = 0
        self.m_next = 0
        self.m_wrap = False
        self.m_pnow = QPoint(0, 0)
        self.m_active = False

    def setDirection(self, direction):
        self.m_direction = direction

    def setSpeed(self, speed):
        self.m_speed = speed

    def setAnimation(self, animationtype):
        self.m_animationtype = animationtype

    def setWrap(self, wrap):
        self.m_wrap = wrap

    def slideIn1(self):
        self.slideInIdx(0)

    def slideIn2(self):
        self.slideInIdx(1)

    def slideIn3(self):
        self.slideInIdx(2)

    def slideIn4(self):
        self.slideInIdx(3)
    def slideInIdx(self, idx):
        if idx > (self.count() - 1):
            idx = idx % self.count()
        elif idx < 0:
            idx = (idx + self.count()) % self.count()
        self.slideInWgt(self.widget(idx))

    def slideInWgt(self, newwidget):
        if self.m_active:
            return

        self.m_active = True

        _now = self.currentIndex()
        _next = self.indexOf(newwidget)

        if _now == _next:
            self.m_active = False
            return

        offsetx, offsety = self.frameRect().width(), self.frameRect().height()
        self.widget(_next).setGeometry(self.frameRect())

        if not self.m_direction == Qt.Horizontal:
            if _now < _next:
                offsetx, offsety = 0, -offsety
            else:
                offsetx = 0
        else:
            if _now < _next:
                offsetx, offsety = -offsetx, 0
            else:
                offsety = 0

        pnext = self.widget(_next).pos()
        pnow = self.widget(_now).pos()
        self.m_pnow = pnow

        offset = QPoint(offsetx, offsety)
        self.widget(_next).move(pnext - offset)
        self.widget(_next).show()
        self.widget(_next).raise_()

        anim_group = QParallelAnimationGroup(
            self, finished=self.animationDoneSlot
        )

        for index, start, end in zip(
            (_now, _next), (pnow, pnext - offset), (pnow + offset, pnext)
        ):
            animation = QPropertyAnimation(
                self.widget(index),
                b"pos",
                duration=self.m_speed,
                easingCurve=self.m_animationtype,
                startValue=start,
                endValue=end,
            )
            anim_group.addAnimation(animation)

        self.m_next = _next
        self.m_now = _now
        self.m_active = True
        anim_group.start(QAbstractAnimation.DeleteWhenStopped)

    def animationDoneSlot(self):
        self.setCurrentIndex(self.m_next)
        self.widget(self.m_now).hide()
        self.widget(self.m_now).move(self.m_pnow)
        self.m_active = False

class MyItem(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.xcor = 0
        self.ycor = 0
        self.xsize = 0
        self.ysize = 0
        self.based_text = ""
        self.changed_text = ""
        self.changed_style = False
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Animation
        self.zoom_factor = 1.1

        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setEasingCurve(QEasingCurve.InOutSine)
        self.anim.setDuration(150)
    def enterEvent(self, event: QEvent) -> None:
        self.resize_obj()
        initial_rect = self.geometry()
        final_rect = QRect(
            0,
            0,
            int(initial_rect.width() * self.zoom_factor),
            int(initial_rect.height() * self.zoom_factor),
        )
        final_rect.moveCenter(initial_rect.center())
        self.anim.setStartValue(initial_rect)
        self.anim.setEndValue(final_rect)
        # self.setText(self.changed_text)
        if self.changed_style == True:
            self.setObjectName("buy_cat_button_hover")
            self.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        self.anim.setDirection(QAbstractAnimation.Forward)
        self.anim.start()
    def leaveEvent(self, event: QEvent) -> None:
        self.resize_obj()
        # self.setText(self.based_text)
        if self.changed_style == True:
            self.setObjectName("buy_cat_button")
            self.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        self.anim.setDirection(QAbstractAnimation.Backward)
        self.anim.start()
    def resize_obj(self):
        self.setGeometry(self.xcor, self.ycor, self.xsize, self.ysize)
    @pyqtProperty(int)
    def xcor_value(self):
        return self.xcor
    @xcor_value.setter
    def xcor_value(self, value):
        self.xcor = value
    @xcor_value.setter
    def ycor_value(self, value):
        self.ycor = value
    @pyqtProperty(int)
    def xsize_value(self):
        return self.xsize
    @xcor_value.setter
    def xsize_value(self, value):
        self.xsize = value
    @pyqtProperty(int)
    def ysize_value(self):
        return self.ysize
    @xcor_value.setter
    def ysize_value(self, value):
        self.ysize = value
    @pyqtProperty(int)
    def based_text_value(self):
        return self.based_text
    @xcor_value.setter
    def based_text_value(self, value):
        self.based_text = value
    @pyqtProperty(int)
    def changed_text_value(self):
        return self.changed_text
    @xcor_value.setter
    def changed_text_value(self, value):
        self.changed_text = value
    @pyqtProperty(bool)
    def change_style_button(self):
        return self.changed_style
    @xcor_value.setter
    def change_style_button(self, value):
        self.changed_style = value
class widgets(QMainWindow):
    def __init__(self, parent=None):
        super(widgets, self).__init__(parent)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.flag = True
        self.cleanTable()

        self.slidingStacked = SlidingStackedWidget(self)
        self.slidingStacked.setGeometry(0, 88, 700, 762)

        self.timer = Timer()
        self.Task = Task()
        self.stats = Statistics()
        self.catRoom = CatRoom()

        self.slidingStacked.addWidget(self.timer)
        self.slidingStacked.addWidget(self.Task)
        self.slidingStacked.addWidget(self.stats)
        self.slidingStacked.addWidget(self.catRoom)

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setGeometry(0, 0, 700, 88)
        frame.setStyleSheet("background-color:#D8B5E9;")

        TimerBtn = MyItem('Timer',self, pressed=self.slidingStacked.slideIn1)
        TimerBtn.xcor = 51
        TimerBtn.ycor = 24
        TimerBtn.xsize = 127
        TimerBtn.ysize = 50
        TimerBtn.setStyleSheet('background-color:#8350AA; border-radius: 25px;font: bold 24px; font-family: Inter; color: #ffffff')
        TimerBtn.resize_obj()

        TaskBtn = MyItem('Task', self, pressed=self.slidingStacked.slideIn2)
        TaskBtn.xcor = 208
        TaskBtn.ycor = 24
        TaskBtn.xsize = 127
        TaskBtn.ysize = 50
        TaskBtn.setStyleSheet(
            'background-color:#8350AA; border-radius: 25px;font: bold 24px; font-family: Inter; color: #ffffff')
        TaskBtn.resize_obj()

        StatisticsButton = MyItem('Statistics', self, pressed=self.slidingStacked.slideIn3)
        StatisticsButton.xcor = 365
        StatisticsButton.ycor = 24
        StatisticsButton.xsize = 127
        StatisticsButton.ysize = 50
        StatisticsButton.setStyleSheet(
            'background-color:#8350AA; border-radius: 25px;font: bold 24px; font-family: Inter; color: #ffffff')
        StatisticsButton.resize_obj()

        CatRoomButton = MyItem('CatRoom', self, pressed=self.slidingStacked.slideIn4)
        CatRoomButton.xcor = 522
        CatRoomButton.ycor = 24
        CatRoomButton.xsize = 127
        CatRoomButton.ysize = 50
        CatRoomButton.setStyleSheet(
            'background-color:#8350AA; border-radius: 25px;font: bold 24px; font-family: Inter; color: #ffffff')
        CatRoomButton.resize_obj()

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle("Meow concentration")
        self.setWindowIcon(QtGui.QIcon("source/icon.ico"))

        self.setGeometry(650, 50, 700, 850)
        self.setFixedSize(QSize(700, 850))

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.show()
    def cleanTable(self):
        print("зашли в тейбл")
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute("SELECT week, day, month, year, data FROM stats")
        res = self.cur.fetchall()
        self.data_base.close()
        if(res == []):
            print("зашли в обновление average")
            self.data_base = sqlite3.connect('details.db')
            self.cur = self.data_base.cursor()
            self.cur.execute("SELECT thismin, thissec FROM average")
            aver = self.cur.fetchone()
            print("aver")
            print(aver)
            self.data_base.close()
            self.data_base = sqlite3.connect('details.db')
            self.cur = self.data_base.cursor()
            self.cur.execute(f'UPDATE average SET lastmin ={aver[0]} , lastsec = {aver[1]}')
            self.data_base.commit()
            self.data_base.close()
        for row in res:
            count_left_elem_week = datetime.date.today().weekday()
            left_border = datetime.date.today().day - count_left_elem_week
            if ((row[1] < left_border) or (row[2] < datetime.date.today().month) or (row[3] < datetime.date.today().year)):
                self.data_base = sqlite3.connect('details.db')
                self.cur = self.data_base.cursor()
                self.cur.execute(f"DELETE FROM stats WHERE data='{row[4]}'")
                self.data_base.commit()

app = QtWidgets.QApplication(sys.argv)
window = widgets()
sys.exit(app.exec_())
