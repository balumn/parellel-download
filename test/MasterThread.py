from threading import Thread
import socket


class MasterThread(Thread):
    

    def __init__(self,param,url): #recives a tuple param from listofparam and a list clientlist
        Thread.__init__(self)
        self.ip = param[0]
        self.port = param[1]
        self.sock = param[2]
        self.sequence = param[3]
        self.url = url[0]
        self.byte = url[1]
        print(" New thread started for "+self.ip+":"+str(self.port))

    def run(self):
         print("hello")
         s=socket.socket()
         s=self.sock
         msg="hello client "+str(self.sequence)
         print(type(self.sock))
         s.send(msg.encode())
         print(type(self.url))
         self.sock.send(self.url.encode())
         print(type(self.byte))
         self.sock.send(self.byte.encode())
