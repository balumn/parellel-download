#!/usr/bin/env python3

import socket
import traceback
import os
import sendmsg

host = ''
port = 10100
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host,port))
while 1:
    try:
        message, address = s.recvfrom(10104)
        print("Got data from", address)
        ss=sendmsg.SendMsg()
        ss.send(address)
    except (KeyboardInterrupt, SystemExit):      
        raise
    except:
        traceback.print_exc()
s.close()        
