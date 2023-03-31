import sys, random, sqlite3
import  datetime, os.path
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *

class Task(QMainWindow):

    def __init__(self):
        super().__init__()
        self.height = 314
        self.line = 0
        self.prevSender = None
        self.title = "Meow concentration"
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.setWindowIcon(QtGui.QIcon('source/cat.ico'))
        self.setStyleSheet("background-color: #E5DBE9")
        self.add_task()
        self.cat()
        self.TaskList()
        # self.TaskAdd(self.height)
        self.InitWindow()
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(650,50,700,762)
        self.setFixedSize(QSize(700,762))
    def add_task(self):
        self.labelTask = QLineEdit(self)
        self.labelTask.setGeometry(51, 209, 598, 50)
        self.labelTask.setStyleSheet("background: #ffffff; border-radius: 25px;padding: 0px 45px; font-family:Inter; font:24px; font-weight:bold;")
        self.labelTask.setPlaceholderText(" Add new task")

        self.labelPlus = QPushButton(self)
        self.labelPlus.setGeometry(61, 218, 29, 29)
        self.labelPlus.setStyleSheet("background: #F6F0B7; border-radius: 14px;")
        pixmap = QPixmap('source/plus.png')
        Icon = QIcon(pixmap)
        self.labelPlus.setIcon(Icon)
        self.labelPlus.clicked.connect(self.action)

    def action(self):
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
        self.taskListHell.setStyleSheet("background:#ffffff; border-radius:24px;")
        self.taskListHell.setObjectName(f'{self.line}')
        self.line += 1
        self.taskListHell.setText(self.labelTask.text())
        self.labelTask.setText('')
        # print(self.taskListHell.objectName())

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
        print(int(self.sender().objectName()))
        flag_first = 0
        flag_line = 0
        flag_circle = 0
        flag_btn = 0
        flag_height = 0
        try:
            # if self.sender().objectName() == '2':
            for i in range(int(self.sender().objectName())+1, self.line):
                print(f'Общий лайн {self.line}')
                if flag_first < 3:
                    res = self.findChild(QObject, str(first_lab))
                    res.deleteLater()
                    flag_first+=1
                if flag_line == 0:
                    res = self.findChild(QObject, str(i))
                    print(f'Наш height = {self.height}')
                    print(f' Меняем --> {res.objectName()}')
                    res.setObjectName(str(first_lab))
                    print (f'на это {first_lab}')
                    flag_line = 1
                    self.height = self.height - 57
                    res.setGeometry(51, self.height, 598, 50)
                    first_lab += 1
                    continue
                if flag_circle == 0:
                    res = self.findChild(QObject, str(i))
                    print(f'Наш height = {self.height}')
                    print(f' Меняем --> {res.objectName()}')
                    res.setObjectName(str(first_lab))
                    print(f'на это {first_lab}')
                    res.setGeometry(69, self.height+20, 9, 9)
                    first_lab += 1
                    flag_circle = 1
                    continue
                if flag_btn == 0:
                    res = self.findChild(QObject, str(i))
                    print(f'Наш height = {self.height}')
                    print(f' Меняем --> {res.objectName()}')
                    res.setObjectName(str(first_lab))
                    print(f'на это {first_lab}')
                    res.setGeometry(606, self.height + 10, 29, 29)
                    first_lab += 1
                    flag_line = 0
                    flag_circle = 0
                    flag_btn = 0

                    # res = self.findChild(QObject, '0')
                    # res.deleteLater()
                    # res = self.findChild(QObject, '1')
                    # res.deleteLater()
                    # res = self.findChild(QObject, '2')
                    # res.deleteLater()
                # res = self.findChild(QObject, '3')
                # res.setGeometry(51,371,598,50)
                # res = self.findChild(QObject, '4')
                # res.setGeometry(69,371+20, 9, 9 )
                # res = self.findChild(QObject, '5')
                # res.setGeometry(606,371+10, 29, 29)

            # if self.sender().objectName() == '4':
            #     res = self.findChild(QObject, '3')
            #     res.deleteLater()
            #     res = self.findChild(QObject, '2')
            #     res.deleteLater()

        except:
            print('Как же хочется жить')


