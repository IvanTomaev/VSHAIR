#! /usr/bin/env python3
import socket
import numpy as np
import cv2
# import multiprocessing as mp
# import rospy
import time
import sys
import pickle
import struct

# class zatichka:
#     def __init__(self):
#         self.socket = socket.socket()
#         self.socket.bind(('', 2000))
#         self.socket.listen(1)
#         self.conn, self.addr = self.socket.accept()
#         while True:
#             data = self.conn.recv(1024)
#             print(data.decode())
#
# def start():
#     d = zatichka()


class videoCapture:
    def __init__(self):
        # process = mp.Process(target = start)
        # process.start()
        self.sock = socket.socket()
        self.sock.bind(('', 4000))
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()
        rospy.init_node('camera')
        self.capture()

    def capture(self):
        video = cv2.VideoCapture(0)


        while True:
            ret, frame = video.read()
            data = pickle.dumps(frame)
            message = struct.pack("Q", len(data)) + data
            self.conn.sendall(message)
            cv2.imshow('Video', frame)
            time.sleep(0.05)
            if cv2.waitKey(1) == ord('q'):
                break
        video.release()
        cv2.destroyAllWindows()



            
           

    
    
    


if __name__ == "__main__":
    camera = videoCapture()
    
    

