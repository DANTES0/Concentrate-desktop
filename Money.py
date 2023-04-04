import sys, random, sqlite3
import  datetime, os.path
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *
class Money_lable(QPushButton):
    def __init__(self):
        super().__init__()
        self.data_base = sqlite3.connect("details.db")
        self.cur = self.data_base.cursor()
        self.cur.execute("SELECT money FROM money")
        money = self.cur.fetchone()
        self.data_base.close()
        self.moneyLable = QPushButton(self)
        self.moneyLable.setGeometry(0, 0, 82, 41)
        self.moneyLable.setIcon(QIcon("source/Coin.png"))
        self.moneyLable.setLayoutDirection(Qt.RightToLeft)
        self.moneyLable.setText(str(money[0]))
        self.moneyLable.setStyleSheet(
            "background: #8350AA;border-radius: 20px;font-family: 'Inter'; font-style: normal; color:#ffffff; font-weight: 700; font-size: 22px; line-height: 15px; text-align: center;padding: 0px 10px 0px 5px;")
        self.moneyLable.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # self.moneyLable.show()

        if money[0] < 100:
            self.moneyLable.setGeometry(0, 0, 67, 41)
            # self.moneyLable.setGeometry(0, 0, 0, 0)
        if money[0] > 999:
            self.moneyLable.setGeometry(0, 0, 97, 41)
            # self.moneyLable.setGeometry(0, 0, 0, 0)
        if money[0] > 9999:
            self.moneyLable.setGeometry(0, 0, 111, 41)
            # self.moneyLable.setGeometry(0, 0, 0, 0)
    def updateM(self):
        self.data_base = sqlite3.connect("details.db")
        self.cur = self.data_base.cursor()
        self.cur.execute("SELECT money FROM money")
        money = self.cur.fetchone()
        self.data_base.close()
        self.moneyLable.setText(str(money[0]))
        if money[0] < 100:
            self.moneyLable.setGeometry(0, 0, 67, 41)
            # self.moneyLable.setGeometry(0, 0, 0, 0)
        if money[0] > 999:
            self.moneyLable.setGeometry(0, 0, 97, 41)
            # self.moneyLable.setGeometry(0, 0, 0, 0)
        if money[0] > 9999:
            self.moneyLable.setGeometry(0, 0, 111, 41)
        # self.moneyLable.setText('123')