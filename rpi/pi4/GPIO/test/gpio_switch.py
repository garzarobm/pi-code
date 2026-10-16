import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(22,GPIO.IN)

# input of the switch will change the state of the LED
while True:
 GPIO.output(4,GPIO.input(22))
 time.sleep(0.05)
 