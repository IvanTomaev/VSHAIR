import socket
import tkinter as tk
import threading
from PIL import ImageTk, Image, ImageFile
import struct
import pickle
import numpy as np
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
        self.videoThread = threading.Thread(target=self.video)
        self.videoThread.start()
        try:
            self.mainSocket.connect(('192.168.43.202', self.port))
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
            self.window.mainloop()





    def pause(self, key):
        self.mainSocket.send('z'.encode())



    def video(self):
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        time.sleep(1)
        self.videoSocket.connect(('192.168.43.202', 4000))
        data = b''
        payload_size = struct.calcsize("Q")
        print(payload_size)
        while True:
            while len(data)< payload_size:
                packet = self.videoSocket.recv(4*1024)
                if not packet:
                    break
                data += packet
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]
            while len(data) < msg_size:
                data += self.videoSocket.recv(4 * 1024)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)
            cv2.imwrite('video.jpg', frame)
            if cv2.waitKey(1) == ord('q'):
                break
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





if __name__ == "__main__":
    controller = controller()
