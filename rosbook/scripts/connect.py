#! /usr/bin/env python3
from smbus import SMBus
import time
import rospy
from std_msgs.msg import String


class controller:
    def __init__(self):
        rospy.init_node('controller')
        self.subscriber = rospy.Subscriber('controlTopic', String, self.callback)
        self.speed = 200
        self.__leftMotorPWM = 0
        self.__leftMotorDir = 1
        self.__rightMotorPWM = 0
        self.__rightMotorDir = 1
        rospy.spin()
    def forward(self):
        self.__leftMotorPWM = self.speed
        self.__leftMotorDir = 1
        self.__rightMotorPWM = self.speed
        self.__rightMotorDir = 1
        self.sendData()

    def backward(self):
        self.__leftMotorPWM = self.speed
        self.__leftMotorDir = 0
        self.__rightMotorPWM = self.speed
        self.__rightMotorDir = 0
        self.sendData()

    def left(self):
        self.__leftMotorPWM = self.speed
        self.__leftMotorDir = 0
        self.__rightMotorPWM = self.speed
        self.__rightMotorDir = 1
        self.sendData()

    def right(self):
        self.__leftMotorPWM = self.speed
        self.__leftMotorDir = 1
        self.__rightMotorPWM = self.speed
        self.__rightMotorDir = 0
        self.sendData()

    def stop(self):
        self.__leftMotorPWM = 0
        self.__leftMotorDir = 0
        self.__rightMotorPWM = 0
        self.__rightMotorDir = 0
        self.sendData()

    def callback(self, data):
        rospy.loginfo(data.data)
        command = data.data
        if command == 'w':
            self.forward()
        elif command == 'd':
            self.right()
        elif command == 's':
            self.backward()
        elif command == 'a':
            self.left()
        else:
            self.stop()

    def getData(self):
        return [self.__leftMotorPWM, self.__leftMotorDir, self.__rightMotorPWM, self.__rightMotorDir]
    def sendData(self):
        bus = SMBus(3)
        time.sleep(0.1)
        bus.write_i2c_block_data(0x39, 0x00, self.getData())
        bus.close()
        time.sleep(0.1)

if __name__ == "__main__":
    controller = controller()
