import sys
from PyQt5 import QtCore, QtWidgets


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
    app = QtWidgets.QApplication(sys.argv)
    w = MyGui()
    w.resize(300, 120)
    w.show()
    sys.exit(app.exec_())