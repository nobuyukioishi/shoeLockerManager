import picamera
from time import sleep
from fractions import Fraction

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    # Set a framerate of 1/6fps, then set shutter
    # speed to 6s and ISO to 800

    for shut_sp in range(1000000,3000000,250000):
        for iso_val in range(250,550,25):
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
            camera.capture('images/iso'+str(iso_val)+'shut_sp'+str(shut_sp)+'.jpg')