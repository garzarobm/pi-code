#!/usr/bin/env python3          
                                
import signal                   
import sys
import time
import RPi.GPIO as GPIO

BAT_GPIO = 16
LED_GPIO = 20

should_blink = False

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def usb_power_off(channel):
    global should_blink
    should_blink = not should_blink  

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(BAT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED_GPIO, GPIO.OUT)   

    GPIO.add_event_detect(BAT_GPIO, GPIO.FALLING, 
            callback=usb_power_off, bouncetime=200)
    
    signal.signal(signal.SIGINT, signal_handler)
    
    while True:
        if should_blink:
            GPIO.output(LED_GPIO, GPIO.HIGH) 
        time.sleep(0.5)
        if should_blink:
            GPIO.output(LED_GPIO, GPIO.LOW)  
        time.sleep(0.5)
