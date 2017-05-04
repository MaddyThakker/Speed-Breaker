#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import os

__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"
__maintainer__ = "pimylifeup.com"

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#define the pin that goes to the circuit
#pin for the buzzer
GPIO.setup(13,GPIO.OUT) # pin->13 gpio->27

pin_to_circuit1 = 7 # pin to first ldr
pin_to_circuit2 = 11 #pin to second ldr
threshold1 = 450
threshold2 = 500
distance = 100
def rc_time1 (pin_to_circuit1):
    count = 0
   
    #Output on the pin for 
    GPIO.setup(pin_to_circuit1, GPIO.OUT)
    GPIO.output(pin_to_circuit1, GPIO.LOW)
    time.sleep(0.1)
    #Change the pin back to input
    GPIO.setup(pin_to_circuit1, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit1) == GPIO.LOW):
        count += 1
    return count

def rc_time2 (pin_to_circuit2):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit2, GPIO.OUT)
    GPIO.output(pin_to_circuit2, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit2, GPIO.IN)
   
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit2) == GPIO.LOW):

        count += 1 
    return count
#Catch when script is interupted, cleanup correctly
try:
    # Main loop
    while True:
#	if(rc_time1(pin_to_circuit1)==0 or rc_time2(pin_to_circuit2)==0):
#	    continue
#	GPIO.output(13,0)
	#print "HELLO"
        if(rc_time1(pin_to_circuit1)>threshold1):
            time1 = time.time()
	 #   print "FIRST "
            while(not(rc_time2(pin_to_circuit2)>threshold2)):
                continue
            time2 = time.time()
            timeElapsed = time2 - time1
            if(rc_time2(pin_to_circuit2)>threshold2):
                print timeElapsed
#		if(distance/timeElapsed > 277.778):
		if(timeElapsed < 5 and timeElapsed > 1):
			print "OVERSPEED"
#			GPIO.output(13,1)
#			time.sleep(1)
#			GPIO.output(13,0) 
			time.sleep(0.1)
			os.system("python /home/pi/Downloads/asd/Vehicle/image.py")
			time.sleep(1)
			for i in range(5):
				os.system("python gsmfinalfinal.py")
				time.sleep(1)
        # print "First " + str(rc_time1(pin_to_circuit1))
        # print "Second " + str(rc_time2(pin_to_circuit2))
#	GPIO.output(13,0)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
