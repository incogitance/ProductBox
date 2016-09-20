#!/usr/bin/env python

import sys
import RPi.GPIO as gpio
from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (3280,2464)


try:
    picamt = sys.argv[1]
except:
    picamt = 0

picamt = int(picamt)
print(picamt)
step = 200
stepsb = 200 / picamt
print(stepsb)

gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.output(13,False)

PicCounter = 0
StepCounter = 0
WaitTime = .006

while picamt > PicCounter:
  if StepCounter == stepsb:
     print("Taking pic number %s" %(PicCounter))
     time.sleep(1)
     camera.capture('/var/www/html/images/image'+str(PicCounter)+'.jpg')
    # time.sleep(1)
     PicCounter += 1
  for StepCounter in range(0,stepsb):
     gpio.output(7,True)
     time.sleep(WaitTime)
     gpio.output(7,False)
     time.sleep(WaitTime)
     StepCounter += 1


gpio.cleanup()
