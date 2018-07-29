import time
import numpy as np
import cv2

class BaseCamera:
    def __init__(self):
        self.frame = None
        self.on = False

    def run_threaded(self):
        return self.frame

class JevoisCamera(BaseCamera):
    def __init__(self, camera_id=0):
        super(JevoisCamera, self).__init__()
        self.camera_id = camera_id
        # initialize the frame and the variable used to indicate
        # if the thread should be stopped
        print('Connecting to Jevois Camera.')
        # A handle to the capture session in Jevois.
        self.capture = cv2.VideoCapture(self.camera_id)
        time.sleep(2)
        if self.capture.isOpened():
            print('JeVois Connected.')
            self.on = True
        else:
            print('Unable to connect. Are you sure you are using the right camera id ?')

    def run(self):
        success, frame = self.capture.read()
        if success:
            self.frame = frame
        return frame

    def update(self):
        # keep looping infinitely until the thread is stopped
        # if the thread indicator variable is set, stop the thread
        while self.on:
            success, frame = self.capture.read()
            if success:
                self.frame = frame

    def shutdown(self):
        # indicate that the thread should be stopped
        self.on = False
        print('Stopping JeVois')
        self.capture.release()
        time.sleep(.5)
