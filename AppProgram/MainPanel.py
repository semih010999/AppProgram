import sys
from time import time
from timeit import Timer
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox,QMainWindow
from MainWindow import Ui_MainWindow
from datetime import datetime
import requests
import pygame



#---------main window----------#
class mainwindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.ui.btn_alarm.clicked.connect(self.gotoalarm)
        self.ui.btn_calendar.clicked.connect(self.gotocalendar)
        self.ui.btn_weather.clicked.connect(self.gotoweather)
        self.ui.btn_notes.clicked.connect(self.gotonotes)
        self.ui.btn_swatch.clicked.connect(self.gotostopwatch)
        self.ui.btn_quit.clicked.connect(self.quit)

    def gotoalarm(self):
        self.close()
        self.cams = alarmWindow()
        self.cams.show()

    def gotocalendar(self):
        self.close()
        self.cams = calendarWindow()
        self.cams.show()
    
    def gotoweather(self):
        self.close()
        self.cams = weatherWindow()
        self.cams.show()

    def gotonotes(self):
        self.close()
        self.cams = notesWindow()
        self.cams.show()

    def gotostopwatch(self):
        self.close()
        self.cams = stopwatchWindow()
        self.cams.show()

    def quit(self):
        cevap=QMessageBox.question(self,"QUİT","Are you sure you want to exit ?",\
                        QMessageBox.Yes | QMessageBox.No)
        if cevap==QMessageBox.Yes:
            sys.exit(app.exec_())
        else:
            self.show()


#--------alarm window---------#
class alarmWindow(QMainWindow):
    def __init__(self):
        super(alarmWindow,self).__init__()
        loadUi("alarmWindow.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.btn_set.clicked.connect(self.alarm)
        self.btn_home.clicked.connect(self.gotohome)
    
    def alarm(self):
        alarmH = self.line_hour.text()
        alarmM = self.line_minute.text()

        while True:
            now = datetime.now()
            dt = datetime.strftime(now, '%H:%M') 

            if dt == f"{alarmH}:{alarmM}":
                pygame.init()
                pygame.mixer.music.load("music1.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.event.get()
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
    
    def gotohome(self):
        self.close()
        self.cams = mainwindow()
        self.cams.show()

#--------calendar window---------#
class calendarWindow(QMainWindow):
    def __init__(self):
        super(calendarWindow,self).__init__()
        loadUi("calendarWindow.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.btn_home.clicked.connect(self.gotohome)

    def gotohome(self):
        self.close()
        self.cams = mainwindow()
        self.cams.show()

#--------weather window---------#
class weatherWindow(QMainWindow):
    def __init__(self):
        super(weatherWindow,self).__init__()
        loadUi("weatherWindow.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.btn_search.clicked.connect(self.main)
        self.btn_home.clicked.connect(self.gotohome)

    def getWeather(self, city):
        url = "https://api.openweathermap.org/data/2.5/weather"
        api_key = "e37c96a665ebbe193571819abd0d697a"
        icon_url = "http://openweathermap.org/img/wn/10d@2x.png"
        parametre = {'q':city,'appid':api_key,'lang':'en'}
        data = requests.get(url,params = parametre).json()
        if data:
            cityy = data['name'].capitalize()
            country = data['sys']['country']
            temp = int(data['main']['temp'] - 273.15)
            icon = data['weather'][0]['icon']
            condition = data['weather'][0]['description']
            return (cityy,country,temp,icon,condition)

    def main(self):
        city = self.line_city.text()
        weather = self.getWeather(city)
        if weather:
            location = '{},{}'.format(weather[0],weather[1])
            self.lbl_location.setText(location)
            temp = '{}°C'.format(weather[2])
            self.lbl_temp.setText(temp)
            condition = weather[4]
            self.lbl_condition.setText(condition)

    def gotohome(self):
        self.close()
        self.cams = mainwindow()
        self.cams.show()

#--------notes window---------#
class notesWindow(QMainWindow):
    def __init__(self):
        super(notesWindow,self).__init__()
        loadUi("notesWindow.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.btn_home.clicked.connect(self.gotohome)
        self.btn_save.clicked.connect(self.save_text)

    def save_text(self):
        text=self.note_edit.toPlainText()
        with open("new file.txt", 'w') as f:
            f.write(text)

        answer=QMessageBox.about(self, "File Saved", "File Saved Sucsessful!")
                    

    def gotohome(self):
        self.close()
        self.cams = mainwindow()
        self.cams.show()

#--------stopwatch window---------#
class stopwatchWindow(QMainWindow):
    def __init__(self):
        super(stopwatchWindow,self).__init__()
        loadUi("stopwatchWindow.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.btn_start.clicked.connect(self.start)
        self.btn_pause.clicked.connect(self.pause)
        self.btn_reset.clicked.connect(self.reset)
        self.btn_home.clicked.connect(self.gotohome)
        self.update_time = ''
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        timer = Timer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)
        self.count = 0
        self.flag = False

        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(45)
        font.setBold(True)
        self.lbl_swatch.setFont(font)
        self.lbl_swatch.setStyleSheet("color:#039ea1;")
        self.lbl_swatch.setGeometry(QtCore.QRect(355, 70, 201, 91))

    def showTime(self):
        if self.flag:
            self.count+= 1

        text = str(self.count / 10)
        self.lbl_swatch.setText(text)
  
    def start(self):
        self.flag = True
  
    def pause(self):
        self.flag = False
  
    def reset(self):
        self.flag = False
        self.count = 0
        self.lbl_swatch.setText(str(self.count))

    def gotohome(self):
        self.close()
        self.cams = mainwindow()
        self.cams.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())