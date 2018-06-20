from RPi import GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

def turn_on():
	GPIO.output(25, True) #blue_1
	GPIO.output(24, True) #red_1
	GPIO.output(23, True) #red_2
	GPIO.output(17, True) #yellow_1
	GPIO.output(22, True) #yellow_2

def turn_off():
	GPIO.output(25, False)
	GPIO.output(24, False)
	GPIO.output(23, False)
	GPIO.output(17, False)
	GPIO.output(22, False)

def brr_on():
	GPIO.output(24, True)
	GPIO.output(23, True)
	GPIO.output(25, True)

def brr_off():
	GPIO.output(24, False)
	GPIO.output(23, False)
	GPIO.output(25, False)

def introduction():
	GPIO.output(23, True)
	GPIO.output(17, True)
	sleep(0.5)
	GPIO.output(17, False)
	sleep(0.1)
	GPIO.output(17, True)
	sleep(0.5)
	GPIO.output(17, True)
	sleep(0.1)
	GPIO.output(17, False)
	sleep(0.2)
	GPIO.output(23, False)
	sleep(1.5)
	GPIO.output(24, True)
	GPIO.output(22, True)
	sleep(0.5)
	GPIO.output(22, False)
	sleep(0.1)
	GPIO.output(22, True)
	sleep(0.5)
	GPIO.output(22, True)
	sleep(0.1)
	GPIO.output(22, False)
	sleep(0.2)
	GPIO.output(24, False)
	
	sleep(1.7)

	GPIO.output(23, True)
	GPIO.output(24, True)
	GPIO.output(17, True)
	GPIO.output(22, True)
	sleep(0.5)
	GPIO.output(17, False)
	GPIO.output(22, False)
	sleep(0.1)
	GPIO.output(17, True)
	GPIO.output(22, True)
	sleep(0.5)
	GPIO.output(17, True)
	GPIO.output(22, True)
	sleep(0.1)
	GPIO.output(17, False)
	GPIO.output(22, False)
	sleep(0.5)
	GPIO.output(23, False)
	GPIO.output(24, False)

	sleep(1.5)

	GPIO.output(25, True)
	sleep(0.4)
	GPIO.output(25, False)
	GPIO.output(17, True)
	GPIO.output(22, True)
	sleep(0.4)
	GPIO.output(17, False)
	GPIO.output(22, False)
	GPIO.output(23, True)
	GPIO.output(24, True)
	sleep(0.4)
	GPIO.output(23, False)
	GPIO.output(24, False)
	

	#sleep(1)
	GPIO.output(17, True)
	GPIO.output(22, True)
	sleep(0.5)
	GPIO.output(17, False)
	GPIO.output(22, False)

	brr_on()
	GPIO.output(17, True)
	GPIO.output(22, True)

	sleep(0.7)
	
	GPIO.output(25, True)
	GPIO.output(22, True)
	GPIO.output(24, True)
	GPIO.output(17, True)
	GPIO.output(23, True)
	sleep(0.5)
	GPIO.output(24, False)
	GPIO.output(23, False)
	sleep(0.5)
	GPIO.output(17, False)
	GPIO.output(22, False)
	sleep(1)
	GPIO.output(25, False)

	sleep(1.5)

	GPIO.output(25, True)
	sleep(0.3)
	GPIO.output(25, False)
	GPIO.output(17, True)
	sleep(0.3)
	GPIO.output(17, False)
	GPIO.output(23, True)
	sleep(0.3)
	GPIO.output(23, False)
	GPIO.output(24, True)
	sleep(0.3)
	GPIO.output(24, False)
	GPIO.output(22, True)
	sleep(0.3)
	GPIO.output(22, False)
	GPIO.output(25, True)






	


	
#while True: 
sleep(2)
introduction()	

GPIO.cleanup()