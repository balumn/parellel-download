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
         readable, writable, errored = select.select(read_list, [], [])
         for s in readable:
             if s is self.sock:
                      
                    part=self.sock.recv(2048)
                    download = "/download/"
                    directory=os.path.dirname(download)
                    if not os.path.exists(directory):
                        os.mkdir(directory)
                    downloadpath=directory
                    #os.path.join(downloadpath,temp)
                    f=open(downloadpath,wb)
                    f.write(data) 
                    f.close()
                    #print(part)