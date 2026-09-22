# -*- coding: utf-8 -*-

# What it does: Prints the multi-line text entered into the text edit
# Wiring:       No wiring needed (GUI application)
# Expected output: A window with a text edit, the content is printed when "Confirm" is pressed
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/pyQT5/widgets/input/text_edit

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 100, 191, 71))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.fun)   # Button signal and slot definition
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Confirm"))

    # Callback function
    def fun(self):
        print(self.textEdit.toPlainText())   # Print the content of the text edit

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
