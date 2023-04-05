import sys, random, sqlite3
import  datetime, os.path
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *
from MyItem import MyItem

class Task(QMainWindow):

    def __init__(self):
        super().__init__()
        self.height = 314
        self.line = 0
        self.very_temp_line = 0
        self.prevSender = None
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.setStyleSheet("background-color: #E5DBE9")
        self.add_task()
        self.cat()
        self.TaskList()
        self.InitWindow()
    def InitWindow(self):
        self.setGeometry(650,50,700,762)
        self.setFixedSize(QSize(700,762))
    def add_task(self):
        self.labelTask = QLineEdit(self)
        self.labelTask.setGeometry(51, 209, 598, 50)
        self.labelTask.setStyleSheet("background: #ffffff; border-radius: 25px;padding: 0px 45px; font-family:Inter; font:24px; font-weight:bold;")
        self.labelTask.setPlaceholderText(" Add new task")

        # self.labelPlus = QPushButton(self)
        # self.labelPlus.setGeometry(61, 218, 29, 29)
        # self.labelPlus.setStyleSheet("background: #F6F0B7; border-radius: 14px;")
        self.labelPlus = MyItem('', self)
        self.labelPlus.xcor = 61
        self.labelPlus.ycor = 218
        self.labelPlus.xsize = 29
        self.labelPlus.ysize = 29
        self.labelPlus.setStyleSheet("background: #F6F0B7; border-radius: 14px;")
        self.labelPlus.resize_obj()
        pixmap = QPixmap('source/plus.png')
        Icon = QIcon(pixmap)
        self.labelPlus.setIcon(Icon)
        self.labelPlus.clicked.connect(self.action)

    def action(self):
        if self.labelTask.text()!='':
            if self.line != 18:
                self.height = self.height+57
                self.TaskAdd(self.height)


    def cat(self):
        self.labelCat = QLabel(self)
        pixmap = QPixmap('source/TaskCat.png')
        self.labelCat.setPixmap(pixmap)
        self.labelCat.setGeometry(213, 0, 254, 208)

    def TaskList(self):
        self.labelTaskList = QLabel("  Task list", self)
        self.labelTaskList.setGeometry(51, 314, 127, 50)
        self.labelTaskList.setStyleSheet("background: #8350AA; border-radius: 25px; font-family:Inter; font:24px; font-weight:bold; color:#ffffff;  ")

    def TaskAdd(self, height):
        height = self.height

        self.taskListHell = QLabel(self)
        self.taskListHell.setGeometry(51, height, 598, 50)
        self.taskListHell.setStyleSheet("background: #ffffff; border-radius: 25px;padding: 0px 45px; font-family:Inter; font:24px; font-weight:bold;")
        self.taskListHell.setObjectName(f'{self.line}')
        self.line += 1
        self.taskListHell.setText(self.labelTask.text())
        self.labelTask.setText('')

        self.circle = QLabel(self)
        self.circle.setGeometry(69, height + 20, 9, 9)
        self.circle.setStyleSheet("background:#8350AA; border-radius: 4px")
        self.circle.setObjectName(f'{self.line}')
        self.line += 1

        self.acceptBtn = QPushButton(self)
        self.acceptBtn.setGeometry(606, height + 10, 29, 29)
        self.acceptBtn.setIcon(QIcon('source/accept.png'))
        self.acceptBtn.setIconSize(QSize(29, 29))
        self.acceptBtn.setStyleSheet("background:transparent")
        self.acceptBtn.setObjectName(f'{self.line}')
        self.line += 1

        self.acceptBtn.clicked.connect(self.actionClose)

        self.taskListHell.show()
        self.circle.show()
        self.acceptBtn.show()

    def actionClose(self):
        sender = self.sender()
        self.prevSender = sender
        first_lab = int(sender.objectName()) - 2
        flag_first = 0
        flag_line = 0
        flag_circle = 0
        flag_btn = 0
        temp_height = 0
        try:
            if self.sender().objectName() == '2':
                temp_height = 371

            if self.sender().objectName() == '5':
                temp_height = 428

            if self.sender().objectName() == '8':
                temp_height = 485

            if self.sender().objectName() == '11':
                temp_height = 542

            if self.sender().objectName() == '14':
                temp_height = 599

            if self.sender().objectName() == '17':
                temp_height = 656

            temp_line = self.line

            if int(self.sender().objectName()) == self.line - 1:
                for j in range(0,3):
                    res = self.findChild(QObject, str(first_lab))
                    res.deleteLater()
                    first_lab += 1
                    self.line -=1
                    self.height = temp_height - 57
            else:
                for i in range(int(self.sender().objectName())+1, self.line):
                    if flag_first < 3:
                        res = self.findChild(QObject, str(first_lab))
                        res.deleteLater()
                        flag_first+=1
                        temp_line -= 1
                    if flag_line == 0:
                        res = self.findChild(QObject, str(i))
                        res.setObjectName(str(first_lab))
                        flag_line = 1
                        self.height = self.height - 57
                        res.setGeometry(51, temp_height, 598, 50)
                        first_lab += 1
                        continue
                    if flag_circle == 0:
                        res = self.findChild(QObject, str(i))
                        res.setObjectName(str(first_lab))
                        res.setGeometry(69, temp_height+20, 9, 9)
                        first_lab += 1
                        flag_circle = 1
                        continue
                    if flag_btn == 0:
                        res = self.findChild(QObject, str(i))
                        res.setObjectName(str(first_lab))
                        res.setGeometry(606, temp_height + 10, 29, 29)
                        first_lab += 1
                        flag_line = 0
                        flag_circle = 0
                        flag_btn = 0
                        temp_height = temp_height + 57
                        self.height = temp_height - 57
                        self.line = temp_line

        except:
            print('Как же хочется жить')


