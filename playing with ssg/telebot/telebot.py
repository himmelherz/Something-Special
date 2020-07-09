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
ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:
	
	message = ser.readline()
	print(message)
	if ((message[0] == '*') and (message[1]) == 'a'):
		now = datetime.datetime.now()
		logging.info("***!yep, that's alert on arduino!***")
		logging.info(str(now))
		f = open('/home/pi/telebot/python-telegram-bot/sample.txt', 'a')
		f.write('*alert*'  )
		f.close()
		count = count + 1
		print(count)


	else:
		if count > 180:
			now = datetime.datetime.now()
			logging.info(str(now))
			logging.info(message)
			
			count = 0

			f = open('/home/pi/telebot/python-telegram-bot/sample.txt', 'a')
			f.write(message)
			f.close()

		else:
			count = count + 1
			print(count)
	time.sleep(0.5)
