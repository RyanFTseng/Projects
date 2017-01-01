import RPi.GPIO as GPIO
import time
from picamera import PiCamera
camera=PiCamera()
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.IN)
a=1
while True:
    if GPIO.input(12)==0:
        print('a')
        camera.capture('/home/pi/ywryantseng/camera/pictures/frame'+str(a)+'.jpg')
        a=a+1
    if GPIO.input(12)==1:
        GPIO.cleanup()
        exit()            

