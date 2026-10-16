#!/usr/bin/env python3          
                                                                   

                                                                   

from record import *
import subprocess
import signal                   
import sys
import time
import RPi.GPIO as GPIO

BAT_GPIO = 16
LOW_BAT_GPIO= 18
LED_GPIO = 20



p = subprocess.Popen(command, shell=True)

program_running = True


def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def usb_power_off(channel):
    global p
    global usb_power 
    usb_power = False
    pid = p.pid
    os.kill(pid, signal.SIGINT)
def low_bat(channel):
    global low_bat
    low_bat_power = True




if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    # usb on or off 
    GPIO.setup(BAT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # LOW_BAT_GPIO config
    GPIO.setup(LOW_BAT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED_GPIO, GPIO.OUT)   

    GPIO.add_event_detect(BAT_GPIO, GPIO.FALLING, 
            callback=usb_power_off, bouncetime=200)
    
    signal.signal(signal.SIGINT, signal_handler)
#os.system('record')
    


while True:
    if usb_power == False:
        print("USB POWER OFF!")
        break

    else
    poll = p.poll()
    if poll is None:
        print("subprocess")
        sleep(5)
            
    else:
        p = subprocess.Popen(command, shell=True)

wifiProcess = 
WifiPath = "/home/pi/pi-code/nextcloud/

#sleep mode & try wifi
while True:
    if
    
