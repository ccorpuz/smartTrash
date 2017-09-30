#testscript.py 
import RPi.GPIO as GPIO
import time
import os

#Change testPin to whichever pin your switch is connected to
testPin = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(testPin,GPIO.IN)

while True:
  if (GPIO.input(testPin)):
    print "Lid is open!"
