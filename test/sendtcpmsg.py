#!/usr/bin/env python

import socket
import urllib.request
import urllib.response
import os
import select

def send_tcp_message(tcpaddress):
        TCP_IP = tcpaddress
        TCP_PORT = 9001
        BUFFER_SIZE = 1024
        msg="Reporting Client "
        print(TCP_IP,TCP_PORT)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP,TCP_PORT))
        s.send(msg.encode())
        print("tcp conn from client send to server!!!")
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
        print("file downloading... plz wait")
        data = urllib.request.urlopen(req).read()
        print("file download complete!!!")
        #data.encode()
        #@TODO assign directory path for download

        #@TODO path :https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
        downloadFolder = "C://Project/parellel-download"
        if not (os.path.isdir("C://Project/parellel-download")):
            os.makedirs("C://Project/parellel-download")
        downloadPath = downloadFolder + "/" + "temp_file"
        f=open(downloadPath,'wb')
        print("data is downloded in client side and is abt to write...")
        
        
        #for chunk in data1:   #verify if nessary
        #        s.sendall(chunk.encode())
        f.write(data)
        print("data write completed at client side and waiting for server...")
        f.close()
        write_list=[s]
        with open(downloadPath,'rb') as f:
            #d=f.read(4096)
            #while d:
            #    s.send(d)
            #    d=f.read(4096)
            #    print(d)
            readable, writable, errored = select.select([],write_list, [])   #check if reciving socket is ready
            for i in writable:
                if i is s:
                    print("file about to send..")
                    s.sendfile(f)   
        s.close()
        print("file send :::")
