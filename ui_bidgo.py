# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bidgoHppenW.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 850)
        MainWindow.setMinimumSize(QSize(700, 850))
        MainWindow.setMaximumSize(QSize(700, 850))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setEnabled(True)
        self.main_widget.setMinimumSize(QSize(350, 200))
        self.main_widget.setMaximumSize(QSize(350, 200))
        self.main_widget.setAutoFillBackground(True)
        self.horizontalLayoutWidget = QWidget(self.main_widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 351, 51))
        self.top_bar = QHBoxLayout(self.horizontalLayoutWidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.horizontalLayoutWidget)
        self.btn_page_1.setObjectName(u"btn_page_1")

        self.top_bar.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.horizontalLayoutWidget)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setStyleSheet(u"")

        self.top_bar.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.horizontalLayoutWidget)
        self.btn_page_3.setObjectName(u"btn_page_3")

        self.top_bar.addWidget(self.btn_page_3)

        self.btn_page_4 = QPushButton(self.horizontalLayoutWidget)
        self.btn_page_4.setObjectName(u"btn_page_4")

        self.top_bar.addWidget(self.btn_page_4)

        self.verticalLayoutWidget = QWidget(self.main_widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 50, 352, 152))
        self.Content = QVBoxLayout(self.verticalLayoutWidget)
        self.Content.setObjectName(u"Content")
        self.Content.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.verticalLayoutWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(350, 150))
        self.stackedWidget.setMaximumSize(QSize(350, 150))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setMinimumSize(QSize(350, 150))
        self.page_1.setMaximumSize(QSize(350, 150))
        self.label_1 = QLabel(self.page_1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(10, 10, 121, 61))
        font = QFont()
        font.setPointSize(20)
        self.label_1.setFont(font)
        self.label_1.setAlignment(Qt.AlignCenter)
        self.checkBox = QCheckBox(self.page_1)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(180, 70, 61, 16))
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, -20, 351, 101))
        font1 = QFont()
        font1.setPointSize(40)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.radioButton = QRadioButton(self.page_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(120, 110, 80, 18))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 351, 151))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setMinimumSize(QSize(350, 150))
        self.page_4.setMaximumSize(QSize(350, 150))
        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 351, 151))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_4)

        self.Content.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.main_widget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Conentration App", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Page 3", None))
        self.btn_page_4.setText(QCoreApplication.translate("MainWindow", u"Page 4", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Page 3", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Page 4", None))
    # retranslateUi

