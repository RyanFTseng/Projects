import RPi.GPIO as GPIO
import time
from picamera import PiCamera
camera=PiCamera()
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.IN)
a=1
while True:
    try:
        if GPIO.input(12)==1:
            print('a')
            camera.capture('/home/pi/ywryantseng/camera/pictures/image'+str(a)+'.jpg')
            a=a+1
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()            
