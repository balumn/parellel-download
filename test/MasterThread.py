from threading import Thread
import socket
import os
import select

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
         read_list = [self.sock]   
         print("hello")
         msg="hello client "+str(self.sequence)
        # print(type(self.sock))
         #self.sock.send(msg.encode())
         print(self.url)
         self.sock.send(self.url.encode())
         print(self.byte)
         self.sock.send(self.byte.encode())
         
         def recvall(sock):
            BUFF_SIZE = 4096 # 4 KiB
            data = b''
            while True:
                part = sock.recv(BUFF_SIZE)
                data += part
                if len(part) < BUFF_SIZE:
                    # either 0 or end of data
                    break
            return data
         readable, writable, errored = select.select(read_list, [], [])   
         for s in readable:
             if s is self.sock:



                #while True:   
                part=recvall(self.sock)
                    #print(part)
                    
                f=open("downloadpath","wb")
                f.write(part) 
                f.close()
                print(part)