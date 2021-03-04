from picamera import PiCamera
import time 
import threading
from SocketClient import Socket
imagecounter = 0
camera = PiCamera()
#camera.resolution=(100,100)
camera.rotation=180
camera_ready=True
def captureimage():
    global imagecounter
    imagename = ('/home/shares/public/images_4mar/test%s.jpg' % imagecounter)
    camera.capture(imagename)
    imagecounter+=1
    camera_thread = threading.Thread(target = send_image_to_server, args=(imagename,))
    camera_thread.start()
def send_image_to_server(imagename):
    s=Socket()
    s.start()
    s.sendimage(imagename)
    print("done")
        

# for i in range(100):
#     camera.capture('/home/shares/public/images_3mar/YellowRight/imageR%s.jpg' % i)
# for i in range(5):
#     camera.zoom=(-0.7,0.32,0.6,0.6)
#     camera.capture('/home/shares/public/images_3mar/W/imageL%s.jpg' % i)
#     camera.zoom=(0.18,0.32,0.5,0.5)
#     camera.capture('/home/pi/Desktop/Images/imageC%s.jpg' % i)
#     camera.zoom=(0.7,0.32,0.6,0.6)
#     camera.capture('/home/pi/Desktop/Images/imageR%s.jpg' % i)
captureimage()
captureimage()
captureimage()
captureimage()
captureimage()


    
