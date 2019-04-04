#!/usr/bin/env python

import socket
import urllib.request
import urllib.response
import os
import select
from shutil import copyfileobj
from urllib.error import HTTPError
from urllib.error import URLError
import time

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
        #req = urllib.request.Request(url, headers={'Range':x})
        #print("file downloading... plz wait")
        #data = urllib.request.urlopen(req).read()
        #print("file download complete!!!")
        #data.encode()
        #@TODO assign directory path for download
        downloadFolder = "C://Project/parellel-download/"
        if not (os.path.isdir("C://Project/parellel-download")):
            os.makedirs("C://Project/parellel-download/")
        #downloadPath = downloadFolder + "/" + "temp_file"
        #f=open(downloadPath,'wb')
        #print("data is downloded in client side and is abt to write...")
        
        
        #for chunk in data1:   #verify if nessary
        #        s.sendall(chunk.encode())
        #f.write(data)
        #print("data write completed at client side and waiting for server...")
        #f.close()
        ###############

        downloadname =str(url.split('/')[-1])#gives proper filename
        downloadpath=downloadFolder+downloadname
        print(downloadpath)
        req = urllib.request.Request(url, headers={'Range':x})
        #while remaining_download_tries > 0 :
        print("starting download")
        try:
            print("file downloading try 1")

            #raise HTTPError()
            with urllib.request.urlopen(url) as fsrc,open(downloadpath,'w+b')as fdst: #NamedTemporaryFile(delete=False) replace open () with Named..() for temp file download
                copyfileobj(fsrc, fdst,16*1024)
                print("file downloading complete in try 1")
                fdst.close()
                #raise HTTPError()
        except (HTTPError, URLError) as error:
            print("file downloading failed ...1.. retrying...")
            print("retring in 5 seconds...")
            time.sleep(5)
            #2
            try:
                fdst.close()
                print("file downloading try 2")
                with urllib.request.urlopen(url) as fsrc,open(downloadpath,'w+b')as fdst: #NamedTemporaryFile(delete=False) replace open () with Named..() for temp file download
                    copyfileobj(fsrc, fdst,16*1024)
                    print("file downloading complete in try 2")
                    fdst.close()
            except (HTTPError, URLError) as error:
                print("file downloading failed ...2.. retrying...")
                print("retring in 15 seconds...")
                time.sleep(15)
                #3
                try:
                    fdst.close()
                    print("file downloading try 3")
                    with urllib.request.urlopen(url) as fsrc,open(downloadpath,'w+b')as fdst: #NamedTemporaryFile(delete=False) replace open () with Named..() for temp file download
                        copyfileobj(fsrc, fdst,16*1024)
                        print("file downloading complete in try 3")
                        fdst.close()
                except (HTTPError, URLError) as error:
                    print("file downloading failed ...3.. aborting...")
                    print("link expired or not found program is exiting")
                
                else:
                    print("Complete in try3")
                
                #3
            
            else:
                print("Complete in try2")
            
            #2
        
        else:
            print("Complete in try1")
        #1
        ##################
        #@TODO path :https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
        
        write_list=[s]
        with open(downloadpath,'rb') as f:
            #d=f.read(4096)
            #while d:
            #    s.send(d)
            #    d=f.read(4096)
            #    print(d)
            readable, writable, errored = select.select([],write_list, [])   #check if reciving socket is ready
            for i in writable:
                if i is s:
                    print("file sending.....")
                    s.sendfile(f)   
        s.close()
        print("file send :::")
