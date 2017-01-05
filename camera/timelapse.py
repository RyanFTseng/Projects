import time
from os import system
from picamera import PiCamera
camera=PiCamera()
a=1
'''print('interval')
x=int(input())'''

for n in range (0,20,1):
    camera.capture('/home/pi/ywryantseng/camera/pictures/image'+str(a)+'.jpg')
    a=a+1
    time.sleep(30)
system('convert -delay 10 -loop 0 /home/pi/ywryantseng/camera/pictures/image*.jpg timelapse.gif')
