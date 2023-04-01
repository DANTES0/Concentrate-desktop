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
        self.based.shop_item_bg.cat_image.setGeometry(12, 45, 128, 80)
        self.based.shop_item_bg.cat_image.setStyleSheet("background: transparent;")
        self.based.shop_item_bg.cat_name = QLabel(self)
        self.based.shop_item_bg.cat_name.setParent(self.based.shop_item_bg)
        self.based.shop_item_bg.cat_name.setGeometry(0, 0, 140, 40)
        self.based.shop_item_bg.cat_name.setText(cat_name)
        self.based.shop_item_bg.cat_name.setObjectName("cat_name")
        self.based.shop_item_bg.cat_name.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        self.based.shop_item_bg.test = QPushButton(self)
        self.based.shop_item_bg.test.setParent(self.based.shop_item_bg)
        self.based.shop_item_bg.test.setGeometry(24, 138, 97, 31)
        self.based.shop_item_bg.test.setIcon(QIcon("source/Coin.png"))
        self.based.shop_item_bg.test.setLayoutDirection(Qt.RightToLeft)
        self.based.shop_item_bg.test.setText(str(price))
        self.based.shop_item_bg.test.setStyleSheet("background: #D8B5E9; border: 1.5px dashed #29002F; border-radius: 15px;font-family: 'Inter'; font-style: normal; font-weight: 700; font-size: 15px; line-height: 15px; text-align: center;padding: 0px 15px 0px 5px;")
        self.based.shop_item_bg.test.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.zoom_factor = 1.1
        self.anim = QPropertyAnimation(self.based.shop_item_bg.test, b"geometry")
        self.anim.setEasingCurve(QEasingCurve.InOutSine)
        self.anim.setDuration(150)
        #self.buy_cat_button = Buy_cat_button(price)
        #self.buy_cat_button.setParent(self.shop_item_bg)
        #self.buy_cat_button.show()
    def makeParent(self, object: QWidget):
        self.setParent(object)

    # def renderItem(self, object: QFrame):
    #     self.based.setParent(object)
    #     self.based.show()
    #     self.based.shadow.show()
    #     self.based.shop_item_bg.show()
    #     #self.based.shop_item_bg.test.setParent(object)
    #     self.based.shop_item_bg.test.show()
    def enterEvent(self, event: QEvent) -> None:
        #self.resize_obj()
        self.based.shop_item_bg.test.setGeometry(24, 138, 97, 31)
        self.based.shop_item_bg.test.initial_rect = self.based.shop_item_bg.test.geometry()
        self.based.shop_item_bg.test.final_rect = QRect(
            0,
            0,
            int(self.based.shop_item_bg.test.initial_rect.width() * self.zoom_factor),
            int(self.based.shop_item_bg.test.initial_rect.height() * self.zoom_factor),
        )
        self.based.shop_item_bg.test.final_rect.moveCenter(self.based.shop_item_bg.test.initial_rect.center())
        self.anim.setStartValue(self.based.shop_item_bg.test.initial_rect)
        self.anim.setEndValue(self.based.shop_item_bg.test.final_rect)

        self.based.shop_item_bg.test.setText("BUY")
        #self.setObjectName("buy_cat_button_hover")
        #self.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        self.based.shop_item_bg.test.setStyleSheet("background: #5ee672; border: 1.5px dashed #29002F; border-radius: 15px; font-family: 'Inter'; font-style: normal; font-weight: 700; font-size: 16px; line-height: 15px; text-align: center; padding: 0px 20px 0px 5px;")
        self.anim.setDirection(QAbstractAnimation.Forward)
        self.anim.start()
    def leaveEvent(self, event: QEvent) -> None:
        #self.resize_obj()
        self.based.shop_item_bg.test.setGeometry(24, 138, 97, 31)
        self.based.shop_item_bg.test.setText("1000")
        #self.setObjectName("buy_cat_button")
        #self.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        self.based.shop_item_bg.test.setStyleSheet("background: #D8B5E9; border: 1.5px dashed #29002F; border-radius: 15px;font-family: 'Inter'; font-style: normal; font-weight: 700; font-size: 15px; line-height: 15px; text-align: center;padding: 0px 15px 0px 5px;")
        self.anim.setDirection(QAbstractAnimation.Backward)
        self.anim.start()
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
        self.title = "Meow concentration"
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.setWindowIcon(QtGui.QIcon('source/cat.ico'))
        self.setStyleSheet("background-image: url(source/CatRoomBg.png);")
        self.prevSender = None

        self.init_Ui()
        self.InitWindow()
    def InitWindow(self):
        self.setWindowTitle(self.title)
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
        self.mywidget.button_1.close()
        self.mywidget.button_2.close()
        self.mywidget.button_3.close()
        self.mywidget.button_4.close()
        self.mywidget.button_5.close()
        self.mywidget.button_6.close()
        self.mywidget.button_7.close()
        self.mywidget.button_8.close()
        self.mywidget.shadow_1.close()
        self.mywidget.shadow_2.close()
        self.mywidget.shadow_3.close()
        self.mywidget.shadow_4.close()
        self.mywidget.shadow_5.close()
        self.mywidget.shadow_6.close()
        self.mywidget.shadow_7.close()
        self.mywidget.shadow_8.close()
        self.mywidget.cat_1.close()
        self.mywidget.cat_2.close()
        self.mywidget.cat_3.close()
        self.mywidget.cat_4.close()
        self.mywidget.cat_5.close()
        self.mywidget.cat_6.close()
        self.mywidget.cat_7.close()
        self.cat_8.close()
        self.mywidget.cat_name_1.close()
        self.mywidget.cat_name_2.close()
        self.mywidget.cat_name_3.close()
        self.mywidget.cat_name_4.close()
        self.mywidget.cat_name_5.close()
        self.mywidget.cat_name_6.close()
        self.mywidget.cat_name_7.close()
        self.cat_name_8.close()
        self.buy_cat_1_button.close()
        self.buy_cat_2_button.close()
        self.buy_cat_3_button.close()
        self.buy_cat_4_button.close()
        self.buy_cat_5_button.close()
        self.buy_cat_6_button.close()
        self.buy_cat_7_button.close()
        self.buy_cat_8_button.close()
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

        #  тень кнопки 1
        self.mywidget.shadow_1 = QLabel()
        self.mywidget.shadow_1.setGeometry(116, 105, 152, 180)
        self.mywidget.shadow_1.setParent(self)
        self.mywidget.shadow_1.setStyleSheet("background:#455D81; border-radius: 30px;")
        self.mywidget.shadow_1.show()

        #  кнопка 1
        self.mywidget.button_1 = QLabel(self)
        self.mywidget.button_1.setGeometry(113, 96, 146, 180)
        self.mywidget.button_1.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_1.show()

        #  котик для кнопки 1
        self.mywidget.cat_1 = QLabel(self)
        pixmap = QPixmap('source/Sleeper.png')
        self.mywidget.cat_1.setPixmap(pixmap)
        self.mywidget.cat_1.setGeometry(133, 133, 106, 106)
        self.mywidget.cat_1.setStyleSheet("background:transparent")
        self.mywidget.cat_1.show()

        #  текст для кнопки 1
        self.mywidget.cat_name_1 = QLabel(self)
        self.mywidget.cat_name_1.setGeometry(137, 105, 100, 40)
        self.mywidget.cat_name_1.setText("Sleeper")
        self.mywidget.cat_name_1.setObjectName("cat_name")
        self.mywidget.cat_name_1.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        self.mywidget.cat_name_1.show()

        #  кнопка покупки кота 1
        self.buy_cat_1_button = Buy_cat_button(1000)
        self.buy_cat_1_button.setParent(self.mywidget.button_1)
        self.buy_cat_1_button.show()

        #  тень кнопки 2
        self.mywidget.shadow_2 = QLabel()
        self.mywidget.shadow_2.setGeometry(280, 105, 152, 180)
        self.mywidget.shadow_2.setParent(self)
        self.mywidget.shadow_2.setStyleSheet("background:#455D81; border-radius: 30px;")
        self.mywidget.shadow_2.show()

        #  кнопка 2
        self.mywidget.button_2 = QLabel(self)
        self.mywidget.button_2.setGeometry(277, 96, 146, 180)
        self.mywidget.button_2.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_2.show()

        #  котик для кнопки 2
        self.mywidget.cat_2 = QLabel(self)
        pixmap = QPixmap('source/Jokey.png')
        self.mywidget.cat_2.setPixmap(pixmap)
        self.mywidget.cat_2.setGeometry(283, 110, 138, 131)
        self.mywidget.cat_2.setStyleSheet("background:transparent")
        self.mywidget.cat_2.show()

        #  текст для кнопки 2
        self.mywidget.cat_name_2 = QLabel(self)
        self.mywidget.cat_name_2.setGeometry(316, 105, 100, 40)
        self.mywidget.cat_name_2.setText("Jokey")
        self.mywidget.cat_name_2.setObjectName("cat_name")
        self.mywidget.cat_name_2.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        self.mywidget.cat_name_2.show()

        #  кнопка покупки кота 2
        self.buy_cat_2_button = Buy_cat_button(1000)
        self.buy_cat_2_button.setParent(self.mywidget.button_2)
        self.buy_cat_2_button.show()

        #  тень кнопки 3
        self.mywidget.shadow_3 = QLabel()
        self.mywidget.shadow_3.setGeometry(444, 105, 152, 180)
        self.mywidget.shadow_3.setParent(self)
        self.mywidget.shadow_3.setStyleSheet("background:#455D81; border-radius: 30px;")
        self.mywidget.shadow_3.show()

        #  кнопка 3
        self.mywidget.button_3 = QLabel(self)
        self.mywidget.button_3.setGeometry(441, 96, 146, 180)
        self.mywidget.button_3.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_3.show()

        #  котик для кнопки 3
        self.mywidget.cat_3 = QLabel(self)
        pixmap = QPixmap('source/Frisky.png')
        self.mywidget.cat_3.setPixmap(pixmap)
        self.mywidget.cat_3.setGeometry(455, 145, 133, 83)
        self.mywidget.cat_3.setStyleSheet("background:transparent")
        self.mywidget.cat_3.show()

        #  текст для кнопки 3
        self.mywidget.cat_name_3 = QLabel(self)
        self.mywidget.cat_name_3.setGeometry(481, 105, 100, 40)
        self.mywidget.cat_name_3.setText("Frisky")
        self.mywidget.cat_name_3.setObjectName("cat_name")
        self.mywidget.cat_name_3.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        self.mywidget.cat_name_3.show()

        #  кнопка покупки кота 3
        self.buy_cat_3_button = Buy_cat_button(1000)
        self.buy_cat_3_button.setParent(self.mywidget.button_3)
        self.buy_cat_3_button.show()

        #  тень кнопки 4
        self.mywidget.shadow_4 = QLabel()
        self.mywidget.shadow_4.setGeometry(116, 311, 152, 180)
        self.mywidget.shadow_4.setParent(self)
        self.mywidget.shadow_4.setStyleSheet("background:#454781; border-radius: 30px;")
        self.mywidget.shadow_4.show()

        #  кнопка 4
        self.mywidget.button_4 = QLabel(self)
        self.mywidget.button_4.setGeometry(113, 304, 146, 180)
        self.mywidget.button_4.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_4.show()

        #  котик для кнопки 4
        self.mywidget.cat_4 = QLabel(self)
        pixmap = QPixmap('source/Dreamer.png')
        self.mywidget.cat_4.setPixmap(pixmap)
        self.mywidget.cat_4.setGeometry(115, 330, 139, 124)
        self.mywidget.cat_4.setStyleSheet("background:transparent")
        self.mywidget.cat_4.show()

        #  текст для кнопки 4
        self.mywidget.cat_name_4 = QLabel(self)
        self.mywidget.cat_name_4.setGeometry(136, 310, 100, 40)
        self.mywidget.cat_name_4.setText("Dreamer")
        self.mywidget.cat_name_4.setObjectName("cat_name")
        self.mywidget.cat_name_4.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        self.mywidget.cat_name_4.show()

        #  кнопка покупки кота 4
        self.buy_cat_4_button = Buy_cat_button(1000)
        self.buy_cat_4_button.setParent(self.mywidget.button_4)
        self.buy_cat_4_button.show()

        #  тень кнопки 5
        self.mywidget.shadow_5 = QLabel()
        self.mywidget.shadow_5.setGeometry(280, 311, 152, 180)
        self.mywidget.shadow_5.setParent(self)
        self.mywidget.shadow_5.setStyleSheet("background:#454781; border-radius: 30px;")
        self.mywidget.shadow_5.show()

        # кнопка 5
        self.mywidget.button_5 = QLabel(self)
        self.mywidget.button_5.setGeometry(277, 304, 146, 180)
        self.mywidget.button_5.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_5.show()

        #  котик для кнопки 5
        self.mywidget.cat_5 = QLabel(self)
        pixmap = QPixmap('source/Fluffy.png')
        self.mywidget.cat_5.setPixmap(pixmap)
        self.mywidget.cat_5.setGeometry(300, 354, 97, 72)
        self.mywidget.cat_5.setStyleSheet("background:transparent")
        self.mywidget.cat_5.show()

        #  текст для кнопки 5
        self.mywidget.cat_name_5 = QLabel(self)
        self.mywidget.cat_name_5.setGeometry(318, 310, 100, 40)
        self.mywidget.cat_name_5.setText("Fluffy")
        self.mywidget.cat_name_5.setObjectName("cat_name")
        self.mywidget.cat_name_5.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        self.mywidget.cat_name_5.show()

        #  кнопка покупки кота 5
        self.buy_cat_5_button = Buy_cat_button(1000)
        self.buy_cat_5_button.setParent(self.mywidget.button_5)
        self.buy_cat_5_button.show()

        # #  тень кнопки 6
        # self.mywidget.shadow_6 = QLabel()
        # self.mywidget.shadow_6.setGeometry(444, 311, 152, 180)
        # self.mywidget.shadow_6.setParent(self)
        # self.mywidget.shadow_6.setStyleSheet("background:#454781; border-radius: 30px;")
        # self.mywidget.shadow_6.show()
        #
        # #  кнопка 6
        # self.mywidget.button_6 = QLabel(self)
        # self.mywidget.button_6.setGeometry(441, 304, 146, 180)
        # self.mywidget.button_6.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        # self.mywidget.button_6.show()
        #
        # #  котик для кнопки 6
        # self.mywidget.cat_6 = QLabel(self)
        # pixmap = QPixmap('source/Mr_Chief.png')
        # self.mywidget.cat_6.setPixmap(pixmap)
        # self.mywidget.cat_6.setGeometry(468, 350, 96, 79)
        # self.mywidget.cat_6.setStyleSheet("background:transparent")
        # self.mywidget.cat_6.show()
        #
        # #  текст для кнопки 6
        # self.mywidget.cat_name_6 = QLabel(self)
        # self.mywidget.cat_name_6.setGeometry(464, 310, 100, 40)
        # self.mywidget.cat_name_6.setText("Mr.Chief")
        # self.mywidget.cat_name_6.setObjectName("cat_name")
        # self.mywidget.cat_name_6.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        # self.mywidget.cat_name_6.show()
        #
        # #  кнопка покупки кота 6
        # self.buy_cat_6_button = Buy_cat_button(24, 138, 97, 31, 1000)
        # self.buy_cat_6_button.setParent(self.mywidget.button_6)
        # self.buy_cat_6_button.show()

        # #  тень кнопки 7
        # self.mywidget.shadow_7 = QLabel()
        # self.mywidget.shadow_7.setGeometry(193, 521, 152, 180)
        # self.mywidget.shadow_7.setParent(self)
        # self.mywidget.shadow_7.setStyleSheet("background:#81455E; border-radius: 30px;")
        #
        # #  кнопка 7
        # self.mywidget.button_7 = QLabel(self)
        # self.mywidget.button_7.setGeometry(190, 512, 146, 180)
        # self.mywidget.button_7.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        #
        # #  котик для кнопки 7
        # self.mywidget.cat_7 = QLabel(self)
        # pixmap = QPixmap('source/Prince.png')
        # self.mywidget.cat_7.setPixmap(pixmap)
        # self.mywidget.cat_7.setGeometry(220, 553, 90, 90)
        # self.mywidget.cat_7.setStyleSheet("background:transparent")
        #
        # #  текст для кнопки 7
        # self.mywidget.cat_name_7 = QLabel(self)
        # self.mywidget.cat_name_7.setGeometry(228, 515, 100, 40)
        # self.mywidget.cat_name_7.setText("Prince")
        # self.mywidget.cat_name_7.setObjectName("cat_name")
        # self.mywidget.cat_name_7.setStyleSheet(open('source/CatRoom_sheetstyles.qss').read())
        #
        # #  кнопка покупки кота 7
        # self.buy_cat_7_button = Buy_cat_button(24, 138, 97, 31, 1000)
        # self.buy_cat_7_button.setParent(self.mywidget.button_7)
        #
        # #  рендер кота 7
        # self.mywidget.shadow_7.show()
        # self.mywidget.button_7.show()
        # self.mywidget.cat_7.show()
        # self.mywidget.cat_name_7.show()
        # self.buy_cat_7_button.show()

        self.cat_6 = Shop_item(0, 0, "source/Mr_Chief.png", 2345, "Mr.Chief", "#81455E")
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
