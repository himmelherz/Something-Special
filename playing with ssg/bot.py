import time
k = 0
while 0<1:
	if (k == 150):
		f = open('/home/pi/telebot/python-telegram-bot/sample.txt', 'a')
		f.write('INFO:root:***!yep, that is alert on arduino!***'  )
		k = 0
		f.close()
	elif(k==60) or (k==120) or (k==180) or (k==240) or (k==300):
		
		f = open('/home/pi/telebot/python-telegram-bot/sample.txt', 'a')
		f.write('INFO:root:2019-11-28 22:46:27.720963' + '\n' )
		f.write( 'INFO:root:Temperature: 26.75 Humidity: 25.00 Real time: 29-11-2019, 02:31:02, Fri Lightness: 38' + '\n' )
		f.write( str(k) + '\n' )
		k = k+10
		f.close()
	else:
		k = k+10
	time.sleep(1)