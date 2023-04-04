import sys, random, sqlite3
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MyItem import MyItem
from Buy_cat_button import Buy_cat_button
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