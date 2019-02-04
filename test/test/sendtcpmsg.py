#!/usr/bin/env python

import socket

def send_tcp_message(tcpaddress):
        TCP_IP = tcpaddress
        TCP_PORT = 9001
        BUFFER_SIZE = 1024
        msg="hello Sever i am client"
        print(TCP_IP,TCP_PORT)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP,TCP_PORT))
        s.send(msg.encode())
        msg=s.recv(BUFFER_SIZE)
        print (msg)
        url=s.recv(BUFFER_SIZE)
        print (url)
        byte=s.recv(BUFFER_SIZE)
        print (byte)

        #download starts here

        a=byte                                                              #check if recived as string NOT byte
        req = urllib.request.Request(url, headers={'Range':x})
        data = urllib.request.urlopen(req).read()
        print(data)

       #s.close()
