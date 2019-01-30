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
while 1:
    try:
        message, address = s.recvfrom(10104)
        print("Got data from", address)
        ad = ''.join(str(address))
        ad1 = ad.split()
        ad2= ad1[0]
        ad3=ad2[2:15]
        print(ad3) #ad3 is ip address of master

        #replying to server
        dest = (ad3,10100)
        msg = "my speed is xxxx"
        # s.sendto(msg.encode(), dest)


        f = open('serverlist.txt', 'a')
        f.write(ad3+'\n')
        f.close()        
    except (KeyboardInterrupt, SystemExit):
        
        raise
    except:
        traceback.print_exc()