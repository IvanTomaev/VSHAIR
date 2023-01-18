#! /usr/bin/env python3
import numpy as np
import cv2
import rospy


class videoCapture:
    def __init__(self):
        rospy.init_node('camera')
        self.capture()

    def capture(self):
        video = cv2.VideoCapture(0)
        while True:
            ret, frame = video.read()
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) == ord('q'):
                break
        video.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    camera = videoCapture()