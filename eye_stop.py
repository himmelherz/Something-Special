from RPi import GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(25, False)
GPIO.output(24, False)
GPIO.output(23, False)
GPIO.output(17, False)
GPIO.output(22, False)

GPIO.cleanup()