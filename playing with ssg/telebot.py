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

TEXT = '1'

count=0
ser = serial.Serial('/dev/ttyUSB0', 9600)

def send_email():

	logging.info("Sending Email")
	try:	
			smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	except Exception:
		return 0

	smtpserver.ehlo() 
	smtpserver.starttls()

	smtpserver.ehlo 
	if (smtpserver.login(GMAIL_USER, GMAIL_PASS) > 0):

		header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER

		header = header + '\n' + 'Subject:' + SUBJECT + '\n'

		print header

		msg = header + '\n' + 'Vash koteika hochet srat! Hochet srat, hochet srat, hochet-hochet-hochet srat!' + ' \n\n'

		smtpserver.sendmail(GMAIL_USER, TO, msg)

		smtpserver.close()
		return 1 
	else:
		return 0

while True:
	
	message = ser.readline()

	if message[0] == TEXT:
		now = datetime.datetime.now()
		logging.info("***!yep, that's alert on arduino!***")
		logging.info(str(now))
		f = open('/home/pi/telebot/python-telegram-bot/sample.txt', 'a')
		f.write('***!yep, that is alert on arduino!***'  )
		f.close()

	else:
		if count > 1800:
			now = datetime.datetime.now()
			logging.info(str(now))
			logging.info(message)
			
			count = 0

			f = open('/home/pi/telebot/python-telegram-bot/sample.txt', 'a')
			f.write(message)
			f.close()

		else:
			count = count + 1
	time.sleep(0.5)
