from picamera import PiCamera
from time import sleep

camera = PiCamera()

## 	Resolution 	Aspect Ratio 	Framerates 	Video 	Image 	FoV 	Binning
#1 	1920x1080 	16:9 	0.1-30fps 	x 	  	Partial 	None
#2 	3280x2464 	4:3 	0.1-15fps 	x 	x 	Full 	None
#3 	3280x2464 	4:3 	0.1-15fps 	x 	x 	Full 	None
#4 	1640x1232 	4:3 	0.1-40fps 	x 	  	Full 	2x2
#5 	1640x922  	16:9 	0.1-40fps 	x 	  	Full 	2x2
#6 	1280x720  	16:9 	40-90fps  	x 	  	Partial 	2x2
#7 	640x480 	  4:3 	40-90fps  	x 	  	Partial 	2x2


resolution = '3280x2464'
camera.start_preview()
sleep(5)
camera.capture(image{counter}.jpg)
sleep(5)
camera.stop_preview()
