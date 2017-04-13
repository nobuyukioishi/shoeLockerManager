import picamera
from time import sleep
from fractions import Fraction

sleep_time = 10
shut_sp = 1250000
iso_val = 450
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    # Set a framerate of 1/6fps, then set shutter
    # speed to 6s and ISO to 800
    
    while True:
        camera.framerate = Fraction(1, 6)
        camera.shutter_speed = shut_sp
        camera.exposure_mode = 'off'
        camera.iso = iso_val
        # Give the camera a good long time to measure AWB
        # (you may wish to use fixed AWB instead)
        sleep(10)
        # Finally, capture an image with a 6s exposure. Due
        # to mode switching on the still port, this will take
        # longer than 6 seconds
        camera.capture('var/www/html/image.jpg')
        sleep(sleep_time)

# import os
# import time

# TIMEBETWEEN = 30

# frameCount = 0
# while 1:
#     imageNumber = str(frameCount).zfill(7)
#     os.system("raspistill -w 640 -h 480 -o var/www/html/image.jpg")
#     time.sleep(TIMEBETWEEN - 6) #Takes roughly 6 seconds to take a picture



