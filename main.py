import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("bidgo.ui", self)

        # PAGE 1
        self.btn_page_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))

        # PAGE 2
        self.btn_page_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))

        # PAGE 3
        self.btn_page_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))

        # PAGE 4
        self.btn_page_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
class MyGui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.lcdTime = QtWidgets.QLCDNumber(self)
        self.lcdTime.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdTime.setDigitCount(8)

        self.time = QtCore.QTime(0, 0, 0)

        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.lcdTime)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)

    def timerEvent(self):
        #        global time
        self.time = self.time.addSecs(1)
        #        print(self.time.toString("hh:mm"))
        self.lcdTime.display(self.time.toString("hh:mm:ss"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    #MainWindow.show()
    #w = MyGui()
    #w.resize(300, 120)
    #w.show()
    sys.exit(app.exec_())