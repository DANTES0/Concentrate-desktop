import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):

        super().__init__()
        self.title = "123"
        self.top = 150
        self.width = 640
        self. height = 640
        self.left = 150

        self.lcdTime = QtWidgets.QLCDNumber(self)
        self.lcdTime.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdTime.setDigitCount(8)
        self.lcdTime.move(150,300)
        self.lcdTime.resize(320,60)
        self.time = QtCore.QTime(0, 0, 0)

        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.lcdTime)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def timerEvent(self):
        #        global time
        self.time = self.time.addSecs(1)
        #        print(self.time.toString("hh:mm"))
        self.lcdTime.display(self.time.toString("hh:mm:ss"))


    def paintEvent(self,event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        painter.drawEllipse(130,150,350,350)



class MyGui(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()
        # self.title = "123"
        # self.InitWindow()
        # self.top = 150
        # self.right = 350
        # self. bottom = 350
        # self.left = 150
        self.lcdTime = QtWidgets.QLCDNumber(self)
        self.lcdTime.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdTime.setDigitCount(8)

        self.time = QtCore.QTime(0, 0, 0)

        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.lcdTime)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)
#It is comment
    def timerEvent(self):
        #        global time
        self.time = self.time.addSecs(1)
        #        print(self.time.toString("hh:mm"))
        self.lcdTime.display(self.time.toString("hh:mm:ss"))


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    App.setStyleSheet("""
    QWidget.QLCDNumber {
        background-color: "transparent";
        font: bold italic large "Times New Roman"
    }
    """)
    sys.exit(App.exec_())
    # app = QtWidgets.QApplication(sys.argv)
    # w = MyGui()
    # w.resize(150, 200)
    # w.show()
    # sys.exit(app.exec_())