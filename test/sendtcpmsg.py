#!/usr/bin/env python

import socket
import urllib.request
import urllib.response
import os

def send_tcp_message(tcpaddress):
        TCP_IP = tcpaddress
        TCP_PORT = 9001
        BUFFER_SIZE = 1024
        msg="hello Sever i am client"
        print(TCP_IP,TCP_PORT)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP,TCP_PORT))
        s.send(msg.encode())
        #msg=s.recv(BUFFER_SIZE)
        #print (msg)
        url=s.recv(BUFFER_SIZE)
        print (url.decode())
        byte=s.recv(BUFFER_SIZE)
        print (byte)

        #download starts here

        x=byte.decode()  #this variable might by named x as param to range                                                             #check if recived as string NOT byte
        url=url.decode()
        req = urllib.request.Request(url, headers={'Range':x})
        data = urllib.request.urlopen(req).read()
        #data.encode()
        #@TODO assign directory path for download

        #@TODO path :https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
        
        f=open("downloadpath",'wb')
        #for chunk in data.iter_content():   #verify if nessary
        f.write(data) 
        f.close()
        f=open("downloadpath",'rb')
        #send downloaded code back to master
        s.sendfile(f)#try send all or loop send 
        s.close()
        print("file send :::")