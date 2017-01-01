#omxplayer video.h264
from picamera import PiCamera
import time
fr=10
camera=PiCamera()
for n in range(0,5,1):
    camera.framerate=fr
    f=fr+10
    camera.start_recording('/home/pi/ywryantseng/camera/videos/video'+str(n)+'.h264')
    time.sleep(10)
    camera.stop_recording()

