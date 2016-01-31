import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
l=[5,6,19,26]
m=[26,19,6,5]
GPIO.setup(l,GPIO.OUT)
GPIO.setup(12,GPIO.IN)
GPIO.setup(22,GPIO.IN)
def light():
    GPIO.output(l,True)
    time.sleep(1)
    GPIO.output(l,False)
    time.sleep(1)
def seq():
    for x in l:
        GPIO.output(x,True)
        time.sleep(0.1)
        GPIO.output(x,False)
        time.sleep(0.1)
def bseq():
    for x in l:
        GPIO.output(x,True)
        time.sleep(0.1)
        GPIO.output(x,False)
        time.sleep(0.1)
    for x in m:
        GPIO.output(x,True)
        time.sleep(0.02)
        GPIO.output(x,False)
        time.sleep(0.02)
def sec():
    for x in range(1,6,1):
        GPIO.output(l,True)
        time.sleep(x)
        GPIO.output(l,False)
        time.sleep(x)
    for x in range(6,1,1):
        GPIO.output(l,True)
        time.sleep(x)
        GPIO.output(l,False)
        time.sleep(x)
while True:
    try:
        print(GPIO.input(22),GPIO.input(12))
        if GPIO.input(12)==1:     
            light()
        if GPIO.input(12)==0:
            if GPIO.input(22)==1:
                bseq()
            else:   
                seq()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
        
