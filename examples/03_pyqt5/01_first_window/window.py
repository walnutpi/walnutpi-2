# -*- coding: utf-8 -*-

# What it does: Shows a first PyQt5 window with a push button and a label
# Wiring:       No wiring needed (GUI application)
# Expected output: A 480x320 window titled "WalnutPi" with a PushButton and "Hello WalnutPi"
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/pyQT5/first_window

# pyQT5 For WalnutPi

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 90, 91, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WalnutPi"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "Hello WalnutPi"))

#################
#  Main program #
#################
import sys

# [Optional] Allow Thonny to run remotely
import os
os.environ["DISPLAY"] = ":0.0"

# [Optional] Fix missing display on 2K+ resolution monitors
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

# Main entry, build and show the window
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()   # Create the window object
ui = Ui_MainWindow()                   # Create the window object designed with PyQt5
ui.setupUi(MainWindow)                 # Initialize the window
MainWindow.show()                      # Show the window

# [Recommended] Allow the terminal to interrupt the window with Ctrl+C for easier debugging
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
timer = QtCore.QTimer()
timer.start(100)   # You may change this if you wish
timer.timeout.connect(lambda: None)   # Let the interpreter run each 100 ms

sys.exit(app.exec_())   # Exit the process when the window closes
