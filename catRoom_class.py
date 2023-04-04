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
        self.init_Ui()
        # self.money = Money_lable()
        # self.money.show()
        self.create_money()
        self.UpdateCat_Room('source/Sleeper_Room.png', 30, 360, 133, 93, 540)
        self.timer()
        self.InitWindow()

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
        self.mywidget.close()
        self.bg.close()
        self.cat_1.close()
        self.cat_2.close()
        self.cat_3.close()
        self.cat_4.close()
        self.cat_5.close()
        self.cat_6.close()
        self.cat_7.close()
        self.cat_8.close()
        self.storeButton_load.show()
        self.mywidget.storeButton_exit.hide()
        # self.mywidget.moneyLable.hide()
        self.money.setParent(None)
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

        self.storeButton_load.clicked.connect(self.updateMoney)
        self.storeButton_load.clicked.connect(self.storeButton_load_store)
        self.storeButton_load.resize_obj()
        self.storeButton_load.show()

    def load_store(self):
        #  фрейм серого фона для магазина
        self.mywidget = QFrame()
        #  тёмный прозрачный фон магазина
        self.bg = QWidget(self)
        self.bg.setGeometry(0, 0, 700, 762)
        self.bg.setFixedSize(QSize(700, 762))
        self.bg.setStyleSheet("background:#000000; background: rgba(0, 0, 0, 0.6);")
        self.bg.setParent(self)

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
        self.money.setParent(self.bg)
        self.money.show()
        self.bg.show()
        #*******************
        # self.mywidget.money = Money_lable()
        # self.mywidget.money.setParent(self)
        # self.mywidget.money.setGeometry(0, 0, 111, 41)
        # self.mywidget.money.setStyleSheet("background: transparent")
        # self.mywidget.money.show()
        #******************************
        # self.mywidget.moneyLable = QPushButton(self)
        # self.mywidget.moneyLable.setGeometry(600, 7, 93, 41)
        # self.mywidget.moneyLable.setIcon(QIcon("source/Coin.png"))
        # self.mywidget.moneyLable.setLayoutDirection(Qt.RightToLeft)
        # self.mywidget.moneyLable.setText(str(money[0]))
        # self.mywidget.moneyLable.setStyleSheet(
        #     "background: #8350AA;border-radius: 20px;font-family: 'Inter'; font-style: normal; color:#ffffff; font-weight: 700; font-size: 22px; line-height: 15px; text-align: center;padding: 0px 10px 0px 5px;")
        # self.mywidget.moneyLable.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # self.mywidget.moneyLable.show()

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
            # self.money.setGeometry(626, 7, 111, 41)
            # self.mywidget.moneyLable.setGeometry(626, 7, 67, 41)
        if money[0] > 999:
            self.mywidget.storeButton_exit.xcor = 549
            self.mywidget.storeButton_exit.ycor = 8
            self.mywidget.storeButton_exit.xsize = 41
            self.mywidget.storeButton_exit.ysize = 41
            self.mywidget.storeButton_exit.setGeometry(self.mywidget.storeButton_exit.xcor,
                                                       self.mywidget.storeButton_exit.ycor,
                                                       self.mywidget.storeButton_exit.xsize,
                                                       self.mywidget.storeButton_exit.ysize)
            # self.mywidget.moneyLable.setGeometry(596, 7, 97, 41)
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
            # self.mywidget.moneyLable.setGeometry(582, 7, 111, 41)
            self.money.setGeometry(582,7,111,41)

        #  серый фон магазина
        self.mywidget.setGeometry(83, 60, 700, 762)
        self.mywidget.setFixedSize(QSize(534, 667))
        self.mywidget.setParent(self)
        self.mywidget.setStyleSheet("background:#D9D9D9; border-radius: 60px;")
        self.mywidget.show()

        self.cat_1 = Shop_item(0, 0, "source/Sleeper.png", 540, "Sleeper", "#456B81")
        self.cat_1.makeParent(self.mywidget)
        self.cat_1.show()
        self.cat_1.setGeometry(30, 36, 155, 189)

        self.cat_2 = Shop_item(0, 0, "source/Jokey.png", 1080, "Jokey", "#456B81")
        self.cat_2.makeParent(self.mywidget)
        self.cat_2.show()
        self.cat_2.setGeometry(194, 36, 155, 189)

        self.cat_3 = Shop_item(0, 0, "source/Frisky.png", 2160, "Frisky", "#456B81")
        self.cat_3.makeParent(self.mywidget)
        self.cat_3.show()
        self.cat_3.setGeometry(358, 36, 155, 189)

        self.cat_4 = Shop_item(0, 0, "source/Dreamer.png", 5540, "Dreamer", "#454781")
        self.cat_4.makeParent(self.mywidget)
        self.cat_4.show()
        self.cat_4.setGeometry(29, 235, 155, 189)

        self.cat_5 = Shop_item(0, 0, "source/Fluffy.png", 9540, "Fluffy", "#454781")
        self.cat_5.makeParent(self.mywidget)
        self.cat_5.show()
        self.cat_5.setGeometry(194, 235, 155, 189)

        self.cat_6 = Shop_item(0, 0, "source/Mr_Chief.png", 12540, "Mr.Chief", "#454781")
        self.cat_6.makeParent(self.mywidget)
        self.cat_6.show()
        self.cat_6.setGeometry(358, 235, 155, 189)

        self.cat_7 = Shop_item(0, 0, "source/Prince.png", 50000, "Prince", "#81455E")
        self.cat_7.makeParent(self.mywidget)
        self.cat_7.show()
        self.cat_7.setGeometry(124, 442, 155, 189)

        self.cat_8 = Shop_item(0, 0, "source/Kirill.png", 99999, "Kirill", "#81455E")
        self.cat_8.makeParent(self.mywidget)
        self.cat_8.show()
        self.cat_8.setGeometry(288, 442, 155, 189)
