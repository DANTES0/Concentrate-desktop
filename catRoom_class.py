import sys, random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Shop_item(QWidget):
    def __init__(self, xcor: int, ycor: int, cat_image_path: str, price: int, cat_name: str, shadow_color: str):
        super().__init__()
        self.based = QFrame(self)
        self.based.setGeometry(xcor, ycor, 155, 189)
        self.based.setStyleSheet("background: #000000;")
        self.based.shadow = QLabel(self)
        self.based.shadow.setParent(self.based)
        self.based.shadow.setGeometry(3, 9, 152, 180)
        self.based.shadow.setStyleSheet(f"background: {shadow_color}; border-radius: 30px")
        self.based.shop_item_bg = QLabel(self)
        self.based.shop_item_bg.setParent(self.based)
        self.based.shop_item_bg.setGeometry(0, 0, 146, 180)
        self.based.shop_item_bg.setStyleSheet("background: #FFFFFF; border-radius: 30px")
        self.based.shop_item_bg.cat_image = QLabel(self)
        self.based.shop_item_bg.cat_image.setParent(self.based.shop_item_bg)
        img = QPixmap(cat_image_path)
        self.based.shop_item_bg.cat_image.setPixmap(img)
        self.based.shop_item_bg.cat_image.setGeometry(1, 38, 143, 95)
        self.based.shop_item_bg.cat_image.setStyleSheet("background: transparent;")
        self.based.shop_item_bg.cat_image.setAlignment(Qt.AlignCenter)
        #self.based.shop_item_bg.cat_image.move(self.based.shop_item_bg.rect().center())
        self.based.shop_item_bg.cat_name = QLabel(self)
        self.based.shop_item_bg.cat_name.setParent(self.based.shop_item_bg)
        self.based.shop_item_bg.cat_name.setGeometry(0, 8, 146, 26)
        self.based.shop_item_bg.cat_name.setText(cat_name)
        self.based.shop_item_bg.cat_name.setObjectName("cat_name")
        self.based.shop_item_bg.cat_name.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        self.based.shop_item_bg.cat_name.setAlignment(Qt.AlignCenter)
        self.buy_cat_button = Buy_cat_button(price)
        self.buy_cat_button.setParent(self.based.shop_item_bg)
        self.buy_cat_button.show()
    def makeParent(self, object: QWidget):
        self.setParent(object)
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
        self.setText(self.changed_text)
        if self.changed_style == True:
            self.setObjectName("buy_cat_button_hover")
            self.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        self.anim.setDirection(QAbstractAnimation.Forward)
        self.anim.start()
    def leaveEvent(self, event: QEvent) -> None:
        self.resize_obj()
        self.setText(self.based_text)
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
class Buy_cat_button(QPushButton):
    def __init__(self, price: int):
        #*args, **kwargs
        super().__init__()
        self.xcor = 24
        self.ycor = 138
        self.xsize = 97
        self.ysize = 31
        self.price = price
        self.setGeometry(self.xcor, self.ycor, self.xsize, self.ysize)
        self.setIcon(QIcon("source/Coin.png"))
        self.setLayoutDirection(Qt.RightToLeft)
        self.setText(str(self.price))
        #self.setObjectName("buy_cat_button")
        #self.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        self.setStyleSheet("background: #D8B5E9; border: 1.5px dashed #29002F; border-radius: 15px;font-family: 'Inter'; font-style: normal; font-weight: 700; font-size: 15px; line-height: 15px; text-align: center;padding: 0px 15px 0px 5px;")
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.clicked.connect(self.aboba)
        # Animation
        self.zoom_factor = 1.1

        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setEasingCurve(QEasingCurve.InOutSine)
        self.anim.setDuration(150)
    def aboba(self):
            print("Я РАБОТАЮ")

    def enterEvent(self, event: QEvent) -> None:
        #self.resize_obj()
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

        self.setText("BUY")
        #self.setObjectName("buy_cat_button_hover")
        #self.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        self.setStyleSheet("background: #5ee672; border: 1.5px dashed #29002F; border-radius: 15px; font-family: 'Inter'; font-style: normal; font-weight: 700; font-size: 16px; line-height: 15px; text-align: center; padding: 0px 20px 0px 5px;")
        self.anim.setDirection(QAbstractAnimation.Forward)
        self.anim.start()
    def leaveEvent(self, event: QEvent) -> None:
        #self.resize_obj()
        self.setGeometry(self.xcor, self.ycor, self.xsize, self.ysize)
        self.setText(str(self.price))
        #self.setObjectName("buy_cat_button")
        #self.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        self.setStyleSheet("background: #D8B5E9; border: 1.5px dashed #29002F; border-radius: 15px;font-family: 'Inter'; font-style: normal; font-weight: 700; font-size: 15px; line-height: 15px; text-align: center;padding: 0px 15px 0px 5px;")
        self.anim.setDirection(QAbstractAnimation.Backward)
        self.anim.start()
class CatRoom(QMainWindow):
    def __init__(self):
        super().__init__()  # super() lets you avoid referring to the base class explicitly
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.setStyleSheet("background-image: url(source/CatRoomBg.png);")
        self.prevSender = None

        self.init_Ui()
        self.InitWindow()
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
    def init_Ui(self):
        #  ининициализация кнопки для входа в магазин
        self.storeButton_load = MyItem(self)
        self.storeButton_load.xcor = 559
        self.storeButton_load.ycor = 8
        self.storeButton_load.xsize = 41
        self.storeButton_load.ysize = 41
        self.storeButton_load.setStyleSheet("background:#8350AA; border-radius: 10px;")
        self.storeButton_load.setIcon(QIcon('source/store_icon.svg'))

        self.storeButton_load.clicked.connect(self.storeButton_load_store)
        self.storeButton_load.resize_obj()
        self.storeButton_load.show()
    def load_store(self):
        #  фрейм серого фона для магазина
        self.mywidget = QFrame()

        #  тёмный прозрачный фон магазина
        self.bg = QFrame()
        self.bg.setGeometry(0, 0, 700, 762)
        self.bg.setFixedSize(QSize(700, 762))
        self.bg.setStyleSheet("background:#000000; background: rgba(0, 0, 0, 0.6);")
        self.bg.setParent(self)
        self.bg.show()

        #  кнопка закрытия магазина
        self.mywidget.storeButton_exit = MyItem(self)
        self.mywidget.storeButton_exit.xcor = 559
        self.mywidget.storeButton_exit.ycor = 8
        self.mywidget.storeButton_exit.xsize = 41
        self.mywidget.storeButton_exit.ysize = 41
        self.mywidget.storeButton_exit.setStyleSheet("background:#8350AA; border-radius: 10px;")
        self.mywidget.storeButton_exit.setIcon(QIcon('source/store_icon.svg'))

        self.mywidget.storeButton_exit.clicked.connect(self.storeButton_exit_store)
        self.mywidget.storeButton_exit.resize_obj()
        self.mywidget.storeButton_exit.show()

        #  серый фон магазина
        self.mywidget.setGeometry(83, 60, 700, 762)
        self.mywidget.setFixedSize(QSize(534, 667))
        self.mywidget.setParent(self)
        self.mywidget.setStyleSheet("background:#D9D9D9; border-radius: 60px;")
        self.mywidget.show()

        self.cat_1 = Shop_item(0, 0, "source/Sleeper.png", 5642, "Sleeper", "#456B81")
        self.cat_1.makeParent(self.mywidget)
        self.cat_1.show()
        self.cat_1.setGeometry(30, 36, 155, 189)

        self.cat_2 = Shop_item(0, 0, "source/Jokey.png", 5642, "Jokey", "#456B81")
        self.cat_2.makeParent(self.mywidget)
        self.cat_2.show()
        self.cat_2.setGeometry(194, 36, 155, 189)

        self.cat_3 = Shop_item(0, 0, "source/Frisky.png", 5642, "Frisky", "#456B81")
        self.cat_3.makeParent(self.mywidget)
        self.cat_3.show()
        self.cat_3.setGeometry(358, 36, 155, 189)

        self.cat_4 = Shop_item(0, 0, "source/Dreamer.png", 5642, "Dreamer", "#454781")
        self.cat_4.makeParent(self.mywidget)
        self.cat_4.show()
        self.cat_4.setGeometry(29, 235, 155, 189)

        self.cat_5 = Shop_item(0, 0, "source/Fluffy.png", 1234, "Fluffy", "#454781")
        self.cat_5.makeParent(self.mywidget)
        self.cat_5.show()
        self.cat_5.setGeometry(194, 235, 155, 189)

        self.cat_6 = Shop_item(0, 0, "source/Mr_Chief.png", 2345, "Mr.Chief", "#454781")
        self.cat_6.makeParent(self.mywidget)
        self.cat_6.show()
        self.cat_6.setGeometry(358, 235, 155, 189)

        self.cat_7 = Shop_item(0, 0, "source/Prince.png", 1000, "Prince", "#81455E")
        self.cat_7.makeParent(self.mywidget)
        self.cat_7.show()
        self.cat_7.setGeometry(124, 442, 155, 189)

        self.cat_8 = Shop_item(0, 0, "source/Kirill.png", 5134, "Kirill", "#81455E")
        self.cat_8.makeParent(self.mywidget)
        self.cat_8.show()
        self.cat_8.setGeometry(288, 442, 155, 189)