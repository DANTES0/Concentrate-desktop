import sys, random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *
import stats_class, timer_class


app = QtWidgets.QApplication(sys.argv)
# global widget
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle("Meow concentration")
widget.setWindowIcon(QtGui.QIcon('source/cat.ico'))
widget.setGeometry(650,50,700,850)
timer = timer_class.Timer()
stats = stats_class.Statistics()
widget.addWidget(timer)
widget.addWidget(stats)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")