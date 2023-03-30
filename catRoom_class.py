import sys, random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


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
        self.mywidget.cat_8.close()
        self.mywidget.cat_name_1.close()
        self.mywidget.cat_name_2.close()
        self.mywidget.cat_name_3.close()
        self.mywidget.cat_name_4.close()
        self.mywidget.cat_name_5.close()
        self.mywidget.cat_name_6.close()
        self.mywidget.cat_name_7.close()
        self.mywidget.cat_name_8.close()
        self.mywidget.cat_buy_1.close()
        self.mywidget.cat_buy_2.close()
        self.mywidget.cat_buy_3.close()
        self.mywidget.cat_buy_4.close()
        self.mywidget.cat_buy_5.close()
        self.mywidget.cat_buy_6.close()
        self.mywidget.cat_buy_7.close()
        self.mywidget.cat_buy_8.close()
        self.storeButton_load.show()
        self.mywidget.storeButton_exit.hide()
    def init_Ui(self):
        #  ининициализация кнопки для входа в магазин
        self.storeButton_load = QPushButton(self)
        self.storeButton_load.setGeometry(559, 8, 41, 41)
        self.storeButton_load.setStyleSheet("background:#8350AA; border-radius: 10px;")
        self.storeButton_load.setIcon(QIcon('source/store_icon.svg'))

        self.storeButton_load.clicked.connect(self.storeButton_load_store)
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

        #  кнопка магазина
        self.mywidget.storeButton_exit = QPushButton(self)
        self.mywidget.storeButton_exit.setGeometry(559, 8, 41, 41)
        self.mywidget.storeButton_exit.setStyleSheet("background:#8350AA; border-radius: 10px;")
        self.mywidget.storeButton_exit.setIcon(QIcon('source/store_icon.svg'))

        self.mywidget.storeButton_exit.clicked.connect(self.storeButton_exit_store)
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
        self.mywidget.cat_name_1.setStyleSheet("background: transparent; font-family: 'Inter'; font-style: normal; "
                                               "font-weight: 700; font-size: 23px; line-height: 15px; "
                                               "text-align: center;")
        self.mywidget.cat_name_1.show()

        #  кнопка покупки кота 1
        self.mywidget.cat_buy_1 = QPushButton(self)
        self.mywidget.cat_buy_1.setGeometry(137, 234, 97, 31)
        self.mywidget.cat_buy_1.setIcon(QIcon("source/Coin.png"))
        self.mywidget.cat_buy_1.setText("1000")
        self.mywidget.cat_buy_1.setLayoutDirection(Qt.RightToLeft)
        self.mywidget.cat_buy_1.setStyleSheet("background: #D8B5E9; border: 1.5px dashed #29002F; border-radius: 15px;"
                                              "font-family: 'Inter'; font-style: normal; font-weight: 700; "
                                              "font-size: 15px; line-height: 15px; text-align: center; "
                                              "padding: 0px 15px 0px 5px")
        self.mywidget.cat_buy_1.show()

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
        self.mywidget.cat_name_2.setStyleSheet("background: transparent; font-family: 'Inter'; font-style: normal; "
                                               "font-weight: 700; font-size: 23px; line-height: 15px; "
                                               "text-align: center;")
        self.mywidget.cat_name_2.show()

        #  кнопка покупки кота 2
        self.mywidget.cat_buy_2 = QPushButton(self)
        self.mywidget.cat_buy_2.setGeometry(302, 234, 97, 31)
        self.mywidget.cat_buy_2.setIcon(QIcon("source/Coin.png"))
        self.mywidget.cat_buy_2.setText("1000")
        self.mywidget.cat_buy_2.setLayoutDirection(Qt.RightToLeft)
        self.mywidget.cat_buy_2.setStyleSheet("background: #D8B5E9; border: 1.5px dashed #29002F; border-radius: 15px;"
                                              "font-family: 'Inter'; font-style: normal; font-weight: 700; "
                                              "font-size: 15px; line-height: 15px; text-align: center; "
                                              "padding: 0px 15px 0px 5px")
        self.mywidget.cat_buy_2.show()

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
        self.mywidget.cat_name_3.setStyleSheet("background: transparent; font-family: 'Inter'; font-style: normal;"
                                               "font-weight: 700; font-size: 23px; line-height: 15px;"
                                               " text-align: center;")
        self.mywidget.cat_name_3.show()

        #  кнопка покупки кота 3
        self.mywidget.cat_buy_3 = QPushButton(self)
        self.mywidget.cat_buy_3.setGeometry(467, 234, 97, 31)
        self.mywidget.cat_buy_3.setIcon(QIcon("source/Coin.png"))
        self.mywidget.cat_buy_3.setText("1000")
        self.mywidget.cat_buy_3.setLayoutDirection(Qt.RightToLeft)
        self.mywidget.cat_buy_3.setStyleSheet("background: #D8B5E9; border: 1.5px dashed #29002F; border-radius: 15px;"
                                              "font-family: 'Inter'; font-style: normal; font-weight: 700; "
                                              "font-size: 15px; line-height: 15px; text-align: center; "
                                              "padding: 0px 15px 0px 5px")
        self.mywidget.cat_buy_3.show()

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
        self.mywidget.cat_name_4.setStyleSheet("background: transparent; font-family: 'Inter'; font-style: normal;"
                                               " font-weight: 700; font-size: 23px; line-height: 15px;"
                                               " text-align: center;")
        self.mywidget.cat_name_4.show()

        #  кнопка покупки кота 4
        self.mywidget.cat_buy_4 = QPushButton(self)
        self.mywidget.cat_buy_4.setGeometry(137, 442, 97, 31)
        self.mywidget.cat_buy_4.setIcon(QIcon("source/Coin.png"))
        self.mywidget.cat_buy_4.setText("1000")
        self.mywidget.cat_buy_4.setLayoutDirection(Qt.RightToLeft)
        self.mywidget.cat_buy_4.setStyleSheet("background: #D8B5E9; border: 1.5px dashed #29002F; border-radius: 15px;"
                                              "font-family: 'Inter'; font-style: normal; font-weight: 700; "
                                              "font-size: 15px; line-height: 15px; text-align: center; "
                                              "padding: 0px 15px 0px 5px")
        self.mywidget.cat_buy_4.show()

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
        self.mywidget.cat_name_5.setStyleSheet("background: transparent; font-family: 'Inter'; font-style: normal;"
                                               " font-weight: 700; font-size: 23px; line-height: 15px;"
                                               " text-align: center;")
        self.mywidget.cat_name_5.show()

        #  кнопка покупки кота 5
        self.mywidget.cat_buy_5 = QPushButton(self)
        self.mywidget.cat_buy_5.setGeometry(302, 442, 97, 31)
        self.mywidget.cat_buy_5.setIcon(QIcon("source/Coin.png"))
        self.mywidget.cat_buy_5.setText("1000")
        self.mywidget.cat_buy_5.setLayoutDirection(Qt.RightToLeft)
        self.mywidget.cat_buy_5.setStyleSheet("background: #D8B5E9; border: 1.5px dashed #29002F; border-radius: 15px;"
                                              "font-family: 'Inter'; font-style: normal; font-weight: 700; "
                                              "font-size: 15px; line-height: 15px; text-align: center; "
                                              "padding: 0px 15px 0px 5px")
        self.mywidget.cat_buy_5.show()

        #  тень кнопки 6
        self.mywidget.shadow_6 = QLabel()
        self.mywidget.shadow_6.setGeometry(444, 311, 152, 180)
        self.mywidget.shadow_6.setParent(self)
        self.mywidget.shadow_6.setStyleSheet("background:#454781; border-radius: 30px;")
        self.mywidget.shadow_6.show()

        #  кнопка 6
        self.mywidget.button_6 = QLabel(self)
        self.mywidget.button_6.setGeometry(441, 304, 146, 180)
        self.mywidget.button_6.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_6.show()

        #  котик для кнопки 6
        self.mywidget.cat_6 = QLabel(self)
        pixmap = QPixmap('source/Mr_Chief.png')
        self.mywidget.cat_6.setPixmap(pixmap)
        self.mywidget.cat_6.setGeometry(468, 350, 96, 79)
        self.mywidget.cat_6.setStyleSheet("background:transparent")
        self.mywidget.cat_6.show()

        #  текст для кнопки 6
        self.mywidget.cat_name_6 = QLabel(self)
        self.mywidget.cat_name_6.setGeometry(464, 310, 100, 40)
        self.mywidget.cat_name_6.setText("Mr.Chief")
        self.mywidget.cat_name_6.setStyleSheet("background: transparent; font-family: 'Inter'; font-style: normal;"
                                               " font-weight: 700; font-size: 23px; line-height: 15px;"
                                               " text-align: center;")
        self.mywidget.cat_name_6.show()

        #  кнопка покупки кота 6
        self.mywidget.cat_buy_6 = QPushButton(self)
        self.mywidget.cat_buy_6.setGeometry(467, 442, 97, 31)
        self.mywidget.cat_buy_6.setIcon(QIcon("source/Coin.png"))
        self.mywidget.cat_buy_6.setText("1000")
        self.mywidget.cat_buy_6.setLayoutDirection(Qt.RightToLeft)
        self.mywidget.cat_buy_6.setStyleSheet("background: #D8B5E9; border: 1.5px dashed #29002F; border-radius: 15px;"
                                              "font-family: 'Inter'; font-style: normal; font-weight: 700; "
                                              "font-size: 15px; line-height: 15px; text-align: center; "
                                              "padding: 0px 15px 0px 5px")
        self.mywidget.cat_buy_6.show()

        #  тень кнопки 7
        self.mywidget.shadow_7 = QLabel()
        self.mywidget.shadow_7.setGeometry(193, 521, 152, 180)
        self.mywidget.shadow_7.setParent(self)
        self.mywidget.shadow_7.setStyleSheet("background:#81455E; border-radius: 30px;")
        self.mywidget.shadow_7.show()

        #  кнопка 7
        self.mywidget.button_7 = QLabel(self)
        self.mywidget.button_7.setGeometry(190, 512, 146, 180)
        self.mywidget.button_7.setStyleSheet("background:#FFFFFF; border-radius: 30px;")
        self.mywidget.button_7.show()

        #  котик для кнопки 7
        self.mywidget.cat_7 = QLabel(self)
        pixmap = QPixmap('source/Prince.png')
        self.mywidget.cat_7.setPixmap(pixmap)
        self.mywidget.cat_7.setGeometry(220, 553, 90, 90)
        self.mywidget.cat_7.setStyleSheet("background:transparent")
        self.mywidget.cat_7.show()

        #  текст для кнопки 7
        self.mywidget.cat_name_7 = QLabel(self)
        self.mywidget.cat_name_7.setGeometry(228, 515, 100, 40)
        self.mywidget.cat_name_7.setText("Prince")
        self.mywidget.cat_name_7.setStyleSheet("background: transparent; font-family: 'Inter'; font-style: normal;"
                                               " font-weight: 700; font-size: 23px; line-height: 15px;"
                                               " text-align: center;")
        self.mywidget.cat_name_7.show()

        #  кнопка покупки кота 7
        self.mywidget.cat_buy_7 = QPushButton(self)
        self.mywidget.cat_buy_7.setGeometry(217, 650, 97, 31)
        self.mywidget.cat_buy_7.setIcon(QIcon("source/Coin.png"))
        self.mywidget.cat_buy_7.setText("1000")
        self.mywidget.cat_buy_7.setLayoutDirection(Qt.RightToLeft)
        self.mywidget.cat_buy_7.setStyleSheet("background: #D8B5E9; border: 1.5px dashed #29002F; border-radius: 15px;"
                                              "font-family: 'Inter'; font-style: normal; font-weight: 700; "
                                              "font-size: 15px; line-height: 15px; text-align: center; "
                                              "padding: 0px 15px 0px 5px")
        self.mywidget.cat_buy_7.show()

        #  тень кнопки 8
        self.mywidget.shadow_8 = QLabel()
        self.mywidget.shadow_8.setGeometry(357, 521, 152, 180)
        self.mywidget.shadow_8.setParent(self)
        self.mywidget.shadow_8.setStyleSheet("background:#81455E; border-radius: 30px;")
        self.mywidget.shadow_8.show()

        #  кнопка 8
        self.mywidget.button_8 = QLabel(self)
        self.mywidget.button_8.setGeometry(354, 512, 146, 180)
        self.mywidget.button_8.setStyleSheet("background:#FFFFFF; border-radius: 30px")
        self.mywidget.button_8.show()

        #  котик для кнопки 8
        self.mywidget.cat_8 = QLabel(self)
        pixmap = QPixmap('source/Kirill.png')
        self.mywidget.cat_8.setPixmap(pixmap)
        self.mywidget.cat_8.setGeometry(365, 560, 128, 80)
        self.mywidget.cat_8.setStyleSheet("background:transparent;")
        self.mywidget.cat_8.show()

        #  текст для кнопки 8
        self.mywidget.cat_name_8 = QLabel(self)
        self.mywidget.cat_name_8.setGeometry(402, 515, 100, 40)
        self.mywidget.cat_name_8.setText("Kirill")
        self.mywidget.cat_name_8.setStyleSheet("background: transparent; font-family: 'Inter'; font-style: normal;"
                                               " font-weight: 700; font-size: 23px; line-height: 15px;"
                                               " text-align: center;")
        self.mywidget.cat_name_8.show()

        #  кнопка покупки кота 8
        self.mywidget.cat_buy_8 = QPushButton(self)
        self.mywidget.cat_buy_8.setGeometry(380, 650, 97, 31)
        self.mywidget.cat_buy_8.setIcon(QIcon("source/Coin.png"))
        self.mywidget.cat_buy_8.setText("1000")
        self.mywidget.cat_buy_8.setLayoutDirection(Qt.RightToLeft)
        self.mywidget.cat_buy_8.setStyleSheet("background: #D8B5E9; border: 1.5px dashed #29002F; border-radius: 15px;"
                                              "font-family: 'Inter'; font-style: normal; font-weight: 700; "
                                              "font-size: 15px; line-height: 15px; text-align: center; "
                                              "padding: 0px 15px 0px 5px")
        #"QPushButton:hover{transform: scale(10)}"
        self.mywidget.cat_buy_8.show()
