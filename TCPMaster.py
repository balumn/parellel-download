import socket
from threading import Thread
from socketserver import ThreadingMixIn
import listen

TCP_IP = 'localhost'
TCP_PORT = 12021
BUFFER_SIZE = 1024

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print(" New thread started for "+ip+":"+str(port))

    def run(self):
        filename='mytext.txt'
        f = open(filename,'rb')
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                #print('Sent ',repr(l))
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.sock.close()
                break

class broadCast:
    def call(self):
        TCP_IP = ''
        TCP_PORT = 12021
        BUFFER_SIZE = 1024
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpsock.bind((TCP_IP, TCP_PORT))
        threads = []  
        msg = socket.gethostbyname(socket.gethostname())
        dest = ('localhost',10100)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(msg.encode(), dest)
        print("Looking for replies; press Ctrl-C to stop.")
        while True:

            # newthread = ClientThread(ip,port,conn)
            # newthread.start()
            # threads.append(newthread)

            # try
            # (buf,address)=s.recvfrom(10100)
            # if not len(buf):
            #     break
            lis=listen.Listen()
            lis.start()
            # print("received from %s: %s" %(address, buf))
        s.close()

        