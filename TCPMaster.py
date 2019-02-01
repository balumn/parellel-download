import socket
#from threading import Thread
#from socketserver import ThreadingMixIn


#class broadCast:
    #def call(self):
TCP_IP = ''
TCP_PORT = 9001
BUFFER_SIZE = 1024
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcpsock:
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind((TCP_IP, TCP_PORT))
    #threads = []  
    # msg = socket.gethostbyname(socket.gethostname())
dest = ('localhost',10100)
msg="hello"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto(msg.encode(), dest)
print("Looking for replies; press Ctrl-C to stop.")
while True:
    tcpsock.listen(5)
    print ("Waiting for incoming connections...")
    (conn, (ip,port)) = tcpsock.accept()
    msg=tcpsock.recv(1024)
    print ('Got connection from ', (ip,port))
    print(msg)
