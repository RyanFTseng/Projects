from picamera import PiCamera
import time

camera=PiCamera()
for n in range(0,100,1):
    camera.capture('/home/pi/ywryantseng/camera/pictures/image'+str(n)+'.jpg')


