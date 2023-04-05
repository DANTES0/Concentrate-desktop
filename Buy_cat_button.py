import sys, random, sqlite3
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MyItem import MyItem
from Money import Money_lable
from PyQt5.QtMultimedia import QSound
class Buy_cat_button(QPushButton):
    def __init__(self, price: int):
        #*args, **kwargs
        super().__init__()
        self.xcor = 24
        self.ycor = 138
        self.xsize = 97
        self.ysize = 31
        self.price = price
        self.cat_name = ''

        if self.price == 540:
            self.cat_name = 'Sleeper'
        if self.price == 1080:
            self.cat_name = 'Jokey'
        if self.price == 2160:
            self.cat_name = 'Frisky'
        if self.price == 5540:
            self.cat_name = 'Dreamer'
        if self.price == 9540:
            self.cat_name = 'Fluffy'
        if self.price == 12540:
            self.cat_name = 'Mr.Chief'
        if self.price == 50000:
            self.cat_name = 'Prince'
        if self.price == 99999:
            self.cat_name = 'Kirill'
        self.setGeometry(self.xcor, self.ycor, self.xsize, self.ysize)
        self.setIcon(QIcon("source/Coin.png"))
        self.setLayoutDirection(Qt.RightToLeft)
        self.setText(str(self.price))
        self.setStyleSheet("background: #D8B5E9; border: 1.5px dashed #29002F; border-radius: 15px;font-family: 'Inter'; font-style: normal; font-weight: 700; font-size: 15px; line-height: 15px; text-align: center;padding: 0px 15px 0px 5px;")
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.clicked.connect(self.aboba)
        # Animation
        self.zoom_factor = 1.1

        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setEasingCurve(QEasingCurve.InOutSine)
        self.anim.setDuration(150)

        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute(f"SELECT Bought FROM Cats WHERE Cost = {self.price}")
        self.test = self.cur.fetchone()
        self.data_base.close()

        if self.test[0] == 1:
            self.setText("Sold")
            self.setStyleSheet(
                "background: #D9D9D9; border: 1.5px dashed #29002F; border-radius: 15px;font-family: 'Inter'; font-style: normal; font-weight: 700; font-size: 15px; line-height: 15px; text-align: center;padding: 0px 30px 0px 5px;"
                "color: #29002F;")
            self.setIcon(QIcon("source"))
            self.setEnabled(False)

    def aboba(self):
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute("SELECT money FROM money")
        self.money = self.cur.fetchone()
        self.data_base.close()
        self.temp_price = self.money[0]
        if self.temp_price >= self.price:
            self.temp_price = self.temp_price - self.price
            self.data_base = sqlite3.connect('details.db')
            self.cur = self.data_base.cursor()
            self.cur.execute(f"UPDATE money SET money = {self.temp_price}")
            self.data_base.commit()
            self.cur.execute(f"UPDATE Cats SET Bought = 1 WHERE Cost = {self.price}")
            self.data_base.commit()
            self.data_base.close()
            self.setText("Sold")
            self.setStyleSheet(
                "background: #D9D9D9; border: 1.5px dashed #29002F; border-radius: 15px;font-family: 'Inter'; font-style: normal; font-weight: 700; font-size: 15px; line-height: 15px; text-align: center;padding: 0px 30px 0px 5px;"
                "color: #29002F;")
            self.setIcon(QIcon("source"))
            self.setEnabled(False)
            if self.price == 99999:
                QSound('source/buy_kirill.wav', self).play()

            # self.moneyLable = QPushButton(self)
            # self.moneyLable.setGeometry(600, 7, 93, 41)
            # self.moneyLable.setIcon(QIcon("source/Coin.png"))
            # self.moneyLable.setLayoutDirection(Qt.RightToLeft)
            # self.moneyLable.setText(str(self.money[0]))
            # self.moneyLable.setStyleSheet(
            #     "background: #8350AA;border-radius: 20px;font-family: 'Inter'; font-style: normal; color:#ffffff; font-weight: 700; font-size: 22px; line-height: 15px; text-align: center;padding: 0px 10px 0px 5px;")
            # self.moneyLable.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            # self.moneyLable.show()


        print(self.cat_name)
        print("Я РАБОТАЮ")

    def enterEvent(self, event: QEvent) -> None:
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute(f"SELECT Bought FROM Cats WHERE Cost = {self.price}")
        self.test = self.cur.fetchone()
        self.data_base.close()
        # self.resize_obj()
        self.setGeometry(self.xcor, self.ycor, self.xsize, self.ysize)
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

        if self.test[0] == 1:
            self.setText("Sold")
            self.setStyleSheet(
                "background: #D9D9D9; border: 1.5px dashed #29002F; border-radius: 15px;font-family: 'Inter'; font-style: normal; font-weight: 700; font-size: 15px; line-height: 15px; text-align: center;padding: 0px 30px 0px 5px;"
                "color: #29002F; text-align:center;")
            self.setIcon(QIcon("source"))
            self.setEnabled(False)
            self.anim.setDirection(QAbstractAnimation.Forward)
            self.anim.start()
        else:
            self.setText("BUY")
            self.setStyleSheet("background: #5ee672; border: 1.5px dashed #29002F; border-radius: 15px; font-family: 'Inter'; font-style: normal; font-weight: 700; font-size: 16px; line-height: 15px; text-align: center; padding: 0px 20px 0px 5px;")
            self.anim.setDirection(QAbstractAnimation.Forward)
            self.anim.start()
    def leaveEvent(self, event: QEvent) -> None:
        # self.resize_obj()
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute(f"SELECT Bought FROM Cats WHERE Cost = {self.price}")
        self.test = self.cur.fetchone()
        self.data_base.close()
        self.setGeometry(self.xcor, self.ycor, self.xsize, self.ysize)
        if self.test[0] == 1:
            self.setText("Sold")
            self.setStyleSheet(
                "background: #D9D9D9; border: 1.5px dashed #29002F; border-radius: 15px;font-family: 'Inter'; font-style: normal; font-weight: 700; font-size: 15px; line-height: 15px; text-align: center;padding: 0px 30px 0px 5px;"
                "color: #29002F; text-align:center;")
            self.setIcon(QIcon("source"))
            self.setEnabled(False)
            self.anim.setDirection(QAbstractAnimation.Backward)
            self.anim.start()
        else:
            self.setText(str(self.price))
            self.setStyleSheet("background: #D8B5E9; border: 1.5px dashed #29002F; border-radius: 15px;font-family: 'Inter'; font-style: normal; font-weight: 700; font-size: 15px; line-height: 15px; text-align: center;padding: 0px 15px 0px 5px;")
            self.anim.setDirection(QAbstractAnimation.Forward)
            self.anim.start()