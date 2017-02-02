import picamera
import time
import os.path
height=input("enter the height->")
width=input("enter the width->")
count=input("enter the image count->")
camera = picamera.PiCamera()
camera.resolution = (height,width)
for i in range(count):
      print 'capturing',
      camera.capture('Frompy'+str(i)+'.png')
save_path = 'home/Desktop/camera'
completed_images = os.path.join(save_path, filename)
camera.close()     
