# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys,res

class Ui_MainWindow(object):
    def setTime(self):
        time = QtCore.QTime.currentTime()
        text = time.toString("HH:mm")
        self.lbl_clock.setText(text)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("#MainWindow{\n"
"                background: url(:/images/images/background.png);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.widget.setStyleSheet("QPushButton#btn_alarm{    \n"
"    border-radius:15px;\n"
"}\n"
"QPushButton#btn_calendar{    \n"
"    border-radius:15px;\n"
"}\n"
"QPushButton#btn_weather{    \n"
"    border-radius:15px;\n"
"}\n"
"QPushButton#btn_notes{    \n"
"    border-radius:15px;\n"
"}\n"
"QPushButton#btn_swatch{    \n"
"    border-radius:15px;\n"
"}\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.lbl_clock = QtWidgets.QLabel(self.widget)
        self.lbl_clock.setGeometry(QtCore.QRect(330, 70, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(43)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_clock.setFont(font)
        self.lbl_clock.setObjectName("lbl_clock")
        self.btn_alarm = QtWidgets.QPushButton(self.widget)
        self.btn_alarm.setGeometry(QtCore.QRect(120, 200, 81, 81))
        self.btn_alarm.setStyleSheet("background-image: url(:/images/images/alarm.png);")
        self.btn_alarm.setText("")
        self.btn_alarm.setObjectName("btn_alarm")
        self.btn_calendar = QtWidgets.QPushButton(self.widget)
        self.btn_calendar.setGeometry(QtCore.QRect(240, 200, 81, 81))
        self.btn_calendar.setStyleSheet("background-image: url(:/images/images/calendar.png);")
        self.btn_calendar.setText("")
        self.btn_calendar.setObjectName("btn_calendar")
        self.btn_weather = QtWidgets.QPushButton(self.widget)
        self.btn_weather.setGeometry(QtCore.QRect(360, 200, 81, 81))
        self.btn_weather.setStyleSheet("background-image: url(:/images/images/weather.png);")
        self.btn_weather.setText("")
        self.btn_weather.setObjectName("btn_weather")
        self.btn_notes = QtWidgets.QPushButton(self.widget)
        self.btn_notes.setGeometry(QtCore.QRect(480, 200, 81, 81))
        self.btn_notes.setStyleSheet("background-image: url(:/images/images/notes.png);")
        self.btn_notes.setText("")
        self.btn_notes.setObjectName("btn_notes")
        self.btn_swatch = QtWidgets.QPushButton(self.widget)
        self.btn_swatch.setGeometry(QtCore.QRect(600, 200, 81, 81))
        self.btn_swatch.setStyleSheet("background-image: url(:/images/images/stopwatch.png);")
        self.btn_swatch.setText("")
        self.btn_swatch.setObjectName("btn_swatch")
        self.btn_quit = QtWidgets.QPushButton(self.widget)
        self.btn_quit.setGeometry(QtCore.QRect(340, 550, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.btn_quit.setFont(font)
        self.btn_quit.setStyleSheet("QPushButton#btn_quit    {    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#btn_quit:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#btn_quit:pressed{    \n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.btn_quit.setObjectName("btn_quit")
        MainWindow.setCentralWidget(self.centralwidget)

        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        font.setBold(True)
        self.lbl_clock.setFont(font)
        self.lbl_clock.setStyleSheet("color:#039ea1;")
        timer = QtCore.QTimer(MainWindow)
        timer.timeout.connect(self.setTime)
        timer.start(1000)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_clock.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#039ea1;\">15 : 15</span></p></body></html>"))
        self.btn_quit.setText(_translate("MainWindow", "Quit"))
