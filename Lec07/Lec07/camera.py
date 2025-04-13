import cv2
import time
import numpy as np



class Camera(object):
    def __init__(self):
        if cv2.__version__.startswith('2'):
            PROP_FRAME_WIDTH = cv2.cv.CV_CAP_PROP_FRAME_WIDTH
            PROP_FRAME_HEIGHT = cv2.cv.CV_CAP_PROP_FRAME_HEIGHT
        elif cv2.__version__.startswith('3') or cv2.__version__.startswith('4'):
            PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
            PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT

        self.video = cv2.VideoCapture(0 , cv2.CAP_V4L)
        #self.video = cv2.VideoCapture(1)
        #self.video.set(PROP_FRAME_WIDTH, 640)
        #self.video.set(PROP_FRAME_HEIGHT, 480)
        self.video.set(PROP_FRAME_WIDTH, 320)
        self.video.set(PROP_FRAME_HEIGHT, 240)
    def __del__(self):
        self.video.release()
    def get_frame(self,count):
        success, image = self.video.read()

        rows, cols = image.shape[:2]
        M = cv2.getRotationMatrix2D((cols/2, rows/2), (count%8)*45, 1)
        rotation = cv2.warpAffine(image, M, (cols, rows))
        #cv2.imshow('Rotation', rotation)

        ret, jpeg = cv2.imencode('.jpg', rotation)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        return jpeg.tostring()
                






