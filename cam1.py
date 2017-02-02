import picamera
import time
import os
os.chdir ("/home/pi/Desktop/camera")
height=input("enter the height->")
width=input("enter the width->")
count=input("enter the image count->")
camera = picamera.PiCamera()
camera.resolution = (height,width)
for i in range(count):
      print 'capturing',
      camera.capture('Frompy'+str(i)+'.png')
camera.close()

