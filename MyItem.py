import sys, random, sqlite3
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
import  datetime, os.path
from PyQt5.QtCore import *
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