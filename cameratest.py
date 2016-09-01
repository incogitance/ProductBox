from picamera import PiCamera
from time import sleep

camera = PiCamera()
resolution = '3280x2464'
camera.start_preview()
sleep(100)
camera.stop_preview()
