#! /usr/bin/env python3
import rospy
import socket
from std_msgs.msg import String


class robot:

    def on_shutdown(self):
        rospy.loginfo("shutdown")

    def __init__(self):
        self.port = 2000
        self.socket = socket.socket()
        rospy.init_node('main')
        self.publisher = rospy.Publisher('controlTopic', String, queue_size=10)
        rospy.on_shutdown(self.on_shutdown)
        self.startSequence()

   

    def startSequence(self):
        self.socket.bind(('',self.port))
        self.socket.listen(1)
        self.conn, self.addr = self.socket.accept()
        while True:
            key = self.conn.recv(1024)
            self.keyboard(key)

    def keyboard(self, key):
        key = key.decode()
        keySet = {'w', 'a', 's', 'd', 'z'}
        if key in keySet:
            self.publisher.publish(key)
        elif key == '\x1b':
            rospy.signal_shutdown()
if __name__=='__main__':
    robot = robot()       
