from datetime import datetime
import pygame
import time


i = int(input("ne kadar tekrar etsin: "))
x = 0
saat = input("saat: ")
dakika = input("dakika: ")
saniye = input("saniye: ")


while True:
	suan = datetime.now()
	dt = datetime.strftime(suan, '%H:%M:%S') 
	

	if dt == f"{saat}:{dakika}:{saniye}":
		while x < i:
			pygame.init()
			pygame.mixer.music.load("music1.mp3")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy():
				pygame.event.get()
			x+=1