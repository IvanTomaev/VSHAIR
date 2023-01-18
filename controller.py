import socket
import tkinter as tk

# import numpy as np
# import cv2
class controller:
    def __init__(self):
        self.port = 2000
        self.clientIp = ('192.168.31.31', '192.168.43.202','orange.local')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.pastKey = ''
        flag = True
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.clientIp[1], self.port))
            print('connection established')
        except:
            print('error')
            flag = False
            pass
        if flag:

            self.startSequence()

    def pause(self, key):
        self.socket.send('z'.encode())

    def startSequence(self):
        window = tk.Tk()
        Label = tk.Label(None, text = 'Keyboard input')
        window.bind('<KeyPress>', self.keyboard)
        window.bind('<KeyRelease>', self.pause)
        window.bind()
        Label.pack()
        window.mainloop()



    def keyboard(self, key):
        if key.char != self.pastKey:
            self.socket.send(key.char.encode())
            self.pastKey = key.char
        else:
            pass

    # def video(self):
    #     data = ''
    #     while True:
    #         package = self.sock.recv(1)
    #         if not package:
    #             nparr = np.frombytes(data, np.uint8)
    #             frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #             cv2.imshow('frame', frame)
    #             data = ''
    #             break
    #         else:
    #             data += package





if __name__ == "__main__":
    controller = controller()
