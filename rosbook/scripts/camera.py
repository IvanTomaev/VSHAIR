#! /usr/bin/env python3
import socket
import numpy as np
import cv2
import multiprocessing as mp
import rospy
import time
import sys


class zatichka:
    def __init__(self):
        self.socket = socket.socket()
        self.socket.bind(('', 2000))
        self.socket.listen(1)
        self.conn, self.addr = self.socket.accept()
        
        while True:
            data = self.conn.recv(1024)
            print(data.decode())
            
def start():
    d = zatichka()


class videoCapture:
    def __init__(self):
        process = mp.Process(target = start)
        process.start()
        rospy.init_node('camera')
        self.capture()
        

    def capture(self):
        
        video = cv2.VideoCapture(0)
        while True:
            self.socket = socket.socket()
            self.socket.connect(('192.168.31.207',4000))
            ret, frame = video.read()
            data = cv2.imencode('.jpg', frame)[1].tostring()
            self.socket.sendall(data)
            cv2.imshow('Video', frame)
            time.sleep(0.05)
            if cv2.waitKey(1) == ord('q'):
                break
            self.socket.close()
        video.release()
        cv2.destroyAllWindows()



            
           

    
    
    


if __name__ == "__main__":
    camera = videoCapture()
    
    

