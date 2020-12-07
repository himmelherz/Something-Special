import time
import logging
import serial

import smtplib

# add filemode="w" to overwrite
logging.basicConfig(filename="sample.log", level=logging.INFO)
 
import datetime

now = datetime.datetime.now()

TO = 'nozarishi@gmail.com'

GMAIL_USER = 'nozarishi@gmail.com'

GMAIL_PASS = 'Mementomori10'

SUBJECT = 'Intrusion!!'

TEXT = '*alert*'

count=0
ser = serial.Serial('/dev/ttyUSB0', 115200)

while True:
	
	message = ser.readline()
	print(message)
	now = datetime.datetime.now()

	f = open('/home/pi/telebot/python-telegram-bot/sample.txt', 'a')
	f.write(message)
	f.write(str(now))
	f.close()


