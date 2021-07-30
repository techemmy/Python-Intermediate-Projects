from playsound import playsound
from time import strftime

alarm_time = input("Enter time, format(12hrs) 'HH:MM' -> e.g (08:20) : ")

while True:
	if alarm_time == strftime("%I:%M"):
		playsound('alarm.mp3')
		break
