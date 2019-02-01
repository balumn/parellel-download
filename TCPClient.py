#!/usr/bin/env python3

import socket
import traceback
import os
host = ''
port = 10100
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host,port))
message, address = s.recvfrom(10100)
print("Got data from", address)
while 1:
    try:
        TCP_IP = ''
        TCP_PORT = 9001
        BUFFER_SIZE = 1024
        #addr=tuple(address[0],TCP_PORT)
        #print(addr)
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss.connect(('localhost',9001))
        msg="hello Sever i am client"
        ss.send(msg.encode())
    except (KeyboardInterrupt, SystemExit):
        
        raise
    except:
        traceback.print_exc()
        break
