from picamera import PiCamera
from picamera import Color
import time
x=100
y=100
b=10
camera=PiCamera()
#for n in range(0,22,1):
    #camera.resolution=(x,y)
    #x=x+200
    #y=y+200
    #camera.annotate_text='hello world!'
    #camera.annotate_text_size=50
    #camera.brightness=b
    #b=b+10
    #camera.annotate_background=Color('blue')
'''for n in camera.IMAGE_EFFECTS:
    camera.image_effect=n
    camera.annotate_text=camera.image_effect
    camera.annotate_text_size=100'''

for n in camera.EXPOSURE_MODES:
    camera.exposure_mode=n
    camera.annotate_text=camera.exposure_mode
    camera.annotate_text_size=100
    camera.capture('/home/pi/ywryantseng/camera/pictures/image'+str(n)+'.jpg')

    
for n in camera.AWB_MODES:
    camera.awb_mode=n
    camera.annotate_text=camera.awb_mode
    camera.annotate_text_size=100
    camera.capture('/home/pi/ywryantseng/camera/pictures/image'+str(n)+'.jpg')

    

