import time
import picamera
import os

with picamera.PiCamera() as camera:
    camera.resolution = (1360, 1024)
    camera.framerate = 30
    camera.start_preview()
    time.sleep(2.5)
    camera.capture_sequence(['image1.jpg'], use_video_port=True)
    time.sleep(0.5)
    camera.capture_sequence(['image2.jpg'], use_video_port=True)
    os.system("cp image1.jpg /home/pi/Downloads/asd/Vehicle/")
    os.system("cp image2.jpg /home/pi/Downloads/asd/Vehicle/")
    print "Images taken"
    print "Now applying image to text"
    os.system("python3 /home/pi/Downloads/asd/Vehicle/itt.py")
