import socket
import tkinter as tk
import threading
from PIL import ImageTk, Image, ImageFile
# import numpy as np
import cv2
import time
class controller:
    def __init__(self):
        self.port = 2000
        self.clientIp = ('192.168.31.31', '192.168.43.202', 'orange.local')
        self.pastKey = ''
        flag = True
        self.mainSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.videoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.videoSocket.bind(('', 4000))
        self.videoThread = threading.Thread(target=self.video)
        self.videoThread.start()
        try:
            self.mainSocket.connect(('192.168.31.102', self.port))
            print('connection established')
        except:
            print('error')
            flag = False
            pass
        if flag:
            self.window = tk.Tk()
            self.Label = tk.Label(None, text='Keyboard input')
            self.window.bind('<KeyPress>', self.keyboard)
            self.window.bind('<KeyRelease>', self.pause)
            self.window.bind()
            self.Label.pack()
            img = Image.open(r'image.jpg')
            img = img.resize((640, 480), Image.ANTIALIAS)
            v = ImageTk.PhotoImage(img)
            self.panel = tk.Label(image=v)
            self.panel.pack()
            img.close()
            self.startSequence()




    def pause(self, key):
        self.mainSocket.send('z'.encode())

    def startSequence(self):


        self.window.mainloop()

    def video(self):
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        time.sleep(1)
        while True:
            self.videoSocket.listen(1)
            conn, addr = self.videoSocket.accept()
            print('connected')
            image = open(r'video.jpg', 'wb')
            data = 'a'
            while data:
                data = conn.recv(2048)
                image.write(data)
            image.close()
            print('received')
            img = Image.open(r'video.jpg')
            img = img.resize((640, 480), Image.ANTIALIAS)
            v = ImageTk.PhotoImage(img)
            self.panel.config(image=v)
            self.panel.image = v
            img.close()
    def keyboard(self, key):
        if key.char != self.pastKey:
            self.mainSocket.send(key.char.encode())
            self.pastKey = key.char
        else:
            pass



class test:
    def __init__(self):
        self.socket = socket.socket()
        self.socket.bind(('', 4000))
        self.socket.listen(1)
        self.conn, self.addr = self.socket.accept()
        while True:
            self.conn.send(input().encode())

if __name__ == "__main__":
    controller = controller()
