import sys, random, sqlite3
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MyItem import MyItem
from Buy_cat_button import Buy_cat_button
from Shop_item import Shop_item
from Money import Money_lable


global a

class CatRoom(QMainWindow):
    def __init__(self):
        super().__init__()  # super() lets you avoid referring to the base class explicitly
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.setStyleSheet("background-image: url(source/CatRoomBg.png);")
        self.prevSender = None
        self.data_base = sqlite3.connect("details.db")
        self.cur = self.data_base.cursor()
        self.cur.execute("SELECT money FROM money")
        self.moneyExpo = self.cur.fetchone()
        self.data_base.close()

        #self.init_Ui()
        self.Cat_on_lable()

        #  тёмный прозрачный фон магазина
        self.bg = QWidget(self)
        self.bg.setGeometry(0, 0, 700, 762)
        self.bg.setFixedSize(QSize(700, 762))
        self.bg.setStyleSheet("background:#000000; background: rgba(0, 0, 0, 0.6);")

        eff = QGraphicsOpacityEffect(self.bg)
        self.bg.setGraphicsEffect(eff)
        self.bg.abba = QPropertyAnimation(eff, b"opacity")

        self.bg.abba.setDuration(800)
        self.bg.abba.setStartValue(0)
        self.bg.abba.setEndValue(0.6)
        self.bg.abba.setEasingCurve(QEasingCurve.OutQuart)

        self.bg.hide()

        #  фрейм серого фона для магазина
        self.mywidget = QFrame()

        self.mywidget.store_slide = QPropertyAnimation(self.mywidget, b"geometry")
        self.mywidget.store_slide.setDuration(1000)
        self.mywidget.store_slide.setStartValue(QRect(710, 60, 564, 667))
        self.mywidget.store_slide.setEndValue(QRect(83, 60, 564, 667))
        self.mywidget.store_slide.setEasingCurve(QEasingCurve.OutQuint)

        self.cat_1 = Shop_item(0, 0, "source/Sleeper.png", 540, "Sleeper", "#456B81")
        self.cat_2 = Shop_item(0, 0, "source/Jokey.png", 1080, "Jokey", "#456B81")
        self.cat_3 = Shop_item(0, 0, "source/Frisky.png", 2160, "Frisky", "#456B81")
        self.cat_4 = Shop_item(0, 0, "source/Dreamer.png", 5540, "Dreamer", "#454781")
        self.cat_5 = Shop_item(0, 0, "source/Fluffy.png", 9540, "Fluffy", "#454781")
        self.cat_6 = Shop_item(0, 0, "source/Mr_Chief.png", 12540, "Mr.Chief", "#454781")
        self.cat_7 = Shop_item(0, 0, "source/Prince.png", 50000, "Prince", "#81455E")
        self.cat_8 = Shop_item(0, 0, "source/Kirill.png", 99999, "Kirill", "#81455E")

        self.cat_1.hide()
        self.cat_2.hide()
        self.cat_3.hide()
        self.cat_4.hide()
        self.cat_5.hide()
        self.cat_6.hide()
        self.cat_7.hide()
        self.cat_8.hide()

        self.storeButton_load = MyItem(self)
        self.storeButton_load.xcor = 650
        self.storeButton_load.ycor = 8
        self.storeButton_load.xsize = 41
        self.storeButton_load.ysize = 41
        self.storeButton_load.setStyleSheet("background:#8350AA; border-radius: 10px;")
        self.storeButton_load.setIcon(QIcon('source/store_icon.svg'))

        self.storeButton_load.clicked.connect(self.storeButton_load_store)
        self.storeButton_load.resize_obj()

        self.Bought_cat()
        self.create_money()
        self.timer()
        self.InitWindow()
    def Cat_on_lable(self):
        self.Sleeper = QLabel(self)
        self.Sleeper.setPixmap(QPixmap('source/Sleeper_Room'))
        self.Sleeper.setGeometry(30,360,133,93)
        self.Sleeper.setStyleSheet("background: transparent")
        self.Sleeper.hide()

        self.Jokey = QLabel(self)
        self.Jokey.setPixmap(QPixmap('source/Jokey_Room'))
        self.Jokey.setGeometry(455,130,106,105)
        self.Jokey.setStyleSheet("background:transparent")
        self.Jokey.hide()

        self.Frisky = QLabel(self)
        self.Frisky.setPixmap(QPixmap('source/Frisky_Room'))
        self.Frisky.setGeometry(523, 345, 163, 102)
        self.Frisky.setStyleSheet("background:transparent")
        self.Frisky.hide()

        self.Dreamer = QLabel(self)
        self.Dreamer.setPixmap(QPixmap('source/Dreamer_Room'))
        self.Dreamer.setGeometry(183, 415, 153, 101)
        self.Dreamer.setStyleSheet("background:transparent")
        self.Dreamer.hide()

        self.Fluffy = QLabel(self)
        self.Fluffy.setPixmap(QPixmap('source/Fluffy_Room'))
        self.Fluffy.setGeometry(345, 217, 97, 72)
        self.Fluffy.setStyleSheet("background:transparent")
        self.Fluffy.hide()

        self.Mr_Chief = QLabel(self)
        self.Mr_Chief.setPixmap(QPixmap('source/Mr_Chief_Room'))
        self.Mr_Chief.setGeometry(128, 468, 217, 134)
        self.Mr_Chief.setStyleSheet("background:transparent")
        self.Mr_Chief.hide()

        self.Prince = QLabel(self)
        self.Prince.setPixmap(QPixmap('source/Prince_Room'))
        self.Prince.setGeometry(550, 540, 143, 155)
        self.Prince.setStyleSheet("background:transparent")
        self.Prince.hide()

        self.Kirill = QLabel(self)
        self.Kirill.setPixmap(QPixmap('source/Kirill_Room'))
        self.Kirill.setGeometry(44, 595, 213, 133)
        self.Kirill.setStyleSheet("background:transparent")
        self.Kirill.hide()

    def Bought_cat(self):
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute(f'SELECT Cost, Bought FROM Cats')
        self.test = self.cur.fetchall()
        self.data_base.close()
        for row in self.test:
            if row[1] == 1 and row[0] == 540:
                self.Sleeper.show()
            if row[1] == 1 and row[0] == 1080:
                self.Jokey.show()
            if row[1] == 1 and row[0] == 2160:
                self.Frisky.show()
            if row[1] == 1 and row[0] == 5540:
                self.Dreamer.show()
            if row[1] == 1 and row[0] == 9540:
                self.Fluffy.show()
            if row[1] == 1 and row[0] == 12540:
                self.Mr_Chief.show()
            if row[1] == 1 and row[0] == 50000:
                self.Prince.show()
            if row[1] == 1 and row[0] == 99999:
                self.Kirill.show()
    def UpdateCat_Room(self, path, xcor, ycor, xsize, ysize, cat_name):
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute(f'SELECT Bought FROM Cats WHERE Cost = {cat_name}')
        self.test = self.cur.fetchone()
        self.data_base.close()
        if self.test[0] == 1:
            self.PicLabel = QLabel(self)
            self.PicLabel.setPixmap(QPixmap(path))
            self.PicLabel.setGeometry(xcor, ycor, xsize, ysize)
            self.PicLabel.setStyleSheet("background: transparent;")
    def InitWindow(self):
        self.setGeometry(650, 50, 700, 762)
        self.setFixedSize(QSize(700, 762))
    def storeButton_load_store(self):
        print("'Enter Store' button clicked!")
        self.storeButton_load.hide()
        self.load_store()
    def storeButton_exit_store(self):
        #  закрытие всех виджетов магазина
        print("'Exit Store' button clicked!")

        self.bg.abba.setDirection(QAbstractAnimation.Backward)
        self.bg.abba.start()

        self.mywidget.store_slide.setDirection(QAbstractAnimation.Backward)
        self.mywidget.store_slide.start()

        # self.mywidget.storeButton_exit.slide_store_button.setDirection(QAbstractAnimation.Backward)
        # self.mywidget.storeButton_exit.slide_store_button.start()

        self.money.hide()
        #self.money.setGeometry(0,0,0,0)

        self.storeButton_load.show()

        self.mywidget.storeButton_exit.hide()
        self.data_base = sqlite3.connect('details.db')
        self.cur = self.data_base.cursor()
        self.cur.execute(f'SELECT Cost, Bought FROM Cats')
        self.test = self.cur.fetchall()
        self.data_base.close()
        for row in self.test:
            if row[1] == 1 and row[0] == 540:
                self.Sleeper.show()
            if row[1] == 1 and row[0] == 1080:
                self.Jokey.show()
            if row[1] == 1 and row[0] == 2160:
                self.Frisky.show()
            if row[1] == 1 and row[0] == 5540:
                self.Dreamer.show()
            if row[1] == 1 and row[0] == 9540:
                self.Fluffy.show()
            if row[1] == 1 and row[0] == 12540:
                self.Mr_Chief.show()
            if row[1] == 1 and row[0] == 50000:
                self.Prince.show()
            if row[1] == 1 and row[0] == 99999:
                self.Kirill.show()
    def create_money(self):
        self.money = Money_lable()
        self.money.setParent(self)
        self.money.setGeometry(585,7,111,41)
        self.money.setStyleSheet("background: transparent")
        self.money.hide()

    def timer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.updateMoney)
        timer.start(100)
    def updateMoney(self):
        self.money.updateM()

    def init_Ui(self):
        #  ининициализация кнопки для входа в магазин
        self.storeButton_load = MyItem(self)
        self.storeButton_load.xcor = 650
        self.storeButton_load.ycor = 8
        self.storeButton_load.xsize = 41
        self.storeButton_load.ysize = 41
        self.storeButton_load.setStyleSheet("background:#8350AA; border-radius: 10px;")
        self.storeButton_load.setIcon(QIcon('source/store_icon.svg'))

        self.storeButton_load.clicked.connect(self.storeButton_load_store)
        self.storeButton_load.resize_obj()
        self.storeButton_load.show()

    def load_store(self):
        #self.storeButton_load.close()

        self.bg.abba.setDirection(QAbstractAnimation.Forward)
        self.bg.abba.start()

        self.bg.show()

        #  кнопка закрытия магазина
        self.mywidget.storeButton_exit = MyItem(self)
        self.mywidget.storeButton_exit.setStyleSheet("background:#8350AA; border-radius: 10px;")
        self.mywidget.storeButton_exit.setIcon(QIcon('source/store_icon.svg'))

        self.mywidget.storeButton_exit.clicked.connect(self.storeButton_exit_store)
        self.mywidget.storeButton_exit.resize_obj()
        self.mywidget.storeButton_exit.show()

        self.data_base = sqlite3.connect("details.db")
        self.cur = self.data_base.cursor()
        self.cur.execute("SELECT money FROM money")
        money = self.cur.fetchone()
        self.data_base.close()
        self.money.setParent(self)
        self.money.show()

        if money[0] >= 100 and money[0] <= 999:
            self.mywidget.storeButton_exit.xcor = 555
            self.mywidget.storeButton_exit.ycor = 8
            self.mywidget.storeButton_exit.xsize = 41
            self.mywidget.storeButton_exit.ysize = 41
            self.mywidget.storeButton_exit.setGeometry(self.mywidget.storeButton_exit.xcor, self.mywidget.storeButton_exit.ycor,
                                                       self.mywidget.storeButton_exit.xsize, self.mywidget.storeButton_exit.ysize)
            self.money.setGeometry(600,7,93,41)
        if money[0] < 100:
            self.mywidget.storeButton_exit.xcor = 579
            self.mywidget.storeButton_exit.ycor = 8
            self.mywidget.storeButton_exit.xsize = 41
            self.mywidget.storeButton_exit.ysize = 41
            self.mywidget.storeButton_exit.setGeometry(self.mywidget.storeButton_exit.xcor,
                                                       self.mywidget.storeButton_exit.ycor,
                                                       self.mywidget.storeButton_exit.xsize,
                                                       self.mywidget.storeButton_exit.ysize)
            self.money.setGeometry(626,7,111,41)
        if money[0] > 999:
            self.mywidget.storeButton_exit.xcor = 549
            self.mywidget.storeButton_exit.ycor = 8
            self.mywidget.storeButton_exit.xsize = 41
            self.mywidget.storeButton_exit.ysize = 41
            self.mywidget.storeButton_exit.setGeometry(self.mywidget.storeButton_exit.xcor,
                                                       self.mywidget.storeButton_exit.ycor,
                                                       self.mywidget.storeButton_exit.xsize,
                                                       self.mywidget.storeButton_exit.ysize)
            self.money.setGeometry(596,7,97,41)
        if money[0] > 9999:
            self.mywidget.storeButton_exit.xcor = 535
            self.mywidget.storeButton_exit.ycor = 8
            self.mywidget.storeButton_exit.xsize = 41
            self.mywidget.storeButton_exit.ysize = 41
            self.mywidget.storeButton_exit.setGeometry(self.mywidget.storeButton_exit.xcor,
                                                       self.mywidget.storeButton_exit.ycor,
                                                       self.mywidget.storeButton_exit.xsize,
                                                       self.mywidget.storeButton_exit.ysize)
            self.money.setGeometry(582,7,111,41)

        #  серый фон магазина
        self.mywidget.setGeometry(83, 60, 700, 762)
        self.mywidget.setFixedSize(QSize(534, 667))
        self.mywidget.setParent(self)
        self.mywidget.setStyleSheet("background:#D9D9D9; border-radius: 60px;")

        self.mywidget.store_slide.setDirection(QAbstractAnimation.Forward)
        self.mywidget.store_slide.start()

        self.mywidget.show()

        self.cat_1.makeParent(self.mywidget)
        self.cat_1.show()
        self.cat_1.setGeometry(30, 36, 155, 189)

        self.cat_2.makeParent(self.mywidget)
        self.cat_2.show()
        self.cat_2.setGeometry(194, 36, 155, 189)

        self.cat_3.makeParent(self.mywidget)
        self.cat_3.show()
        self.cat_3.setGeometry(358, 36, 155, 189)

        self.cat_4.makeParent(self.mywidget)
        self.cat_4.show()
        self.cat_4.setGeometry(29, 235, 155, 189)

        self.cat_5.makeParent(self.mywidget)
        self.cat_5.show()
        self.cat_5.setGeometry(194, 235, 155, 189)

        self.cat_6.makeParent(self.mywidget)
        self.cat_6.show()
        self.cat_6.setGeometry(358, 235, 155, 189)

        self.cat_7.makeParent(self.mywidget)
        self.cat_7.show()
        self.cat_7.setGeometry(124, 442, 155, 189)

        self.cat_8.makeParent(self.mywidget)
        self.cat_8.show()
        self.cat_8.setGeometry(288, 442, 155, 189)
