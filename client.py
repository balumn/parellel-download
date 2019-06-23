import time
import socket
import urllib.request
import urllib.response
import os
import select
from shutil import copyfileobj
from urllib.error import HTTPError
from urllib.error import URLError
import time
from tkinter import ttk
import tkinter as tk # this is for python3
import tkinter.scrolledtext as st
import tkinter.filedialog as fd
import random
#from PIL import *



dpath = ""
file=0

#################################################
########## ProgressBar #########################
###############################################
def copyfileobj(fsrc, fdst, length,filesize):
    """copy data from file-like object fsrc to file-like object fdst"""
    print("obj hello")
    progress=progressbar(filesize)
    global file
    while 1:
        try:
            buf = fsrc.read(length)
            if not buf:
                break
            fdst.write(buf)
            file=fdst.tell()
            progress["value"] = file
            progress.update()
            print(file)
            #raise ConnectionError
            #progress.destroy()
           
        finally:
            pass
            #progress.destroy()
def copyfileobjr(fsrc, fdst, length,filesize):
    """copy data from file-like object fsrc to file-like object fdst"""
    global file
    progress=progressbar(filesize)
    
    while 1:
        try:
            buf = fsrc.read(length)
            if not buf:
                break
            
            fdst.write(buf)
            file=fdst.tell()
            progress["value"] = file
            progress.update()
            print(file)
        finally:
            pass
            #progress.destroy()
def progressbar(filesize):
    app.entry.destroy()
    print("prog hello")
    progress = ttk.Progressbar(master = cRoot, orient="horizontal",length=450, mode="determinate")
    progress.place(x=80,y=200)
    progress["value"] = 0
    maxbytes = filesize
    progress["maximum"] = filesize
    print("progress hello")
    return progress


def dirBox():
    global dpath
    text = fd.askdirectory(title = "Download Path")
    text = text + "/"
    print(text)
    dpath = str(text)


def hereServe():
    timeout = 20   # [seconds] #################################################################### Timeout
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        address=broadcast_recive()
        if address:
            break
    tcpaddress=str(address[0])
    print("address of master:",tcpaddress)
    app.log("\nMaster Found !\naddress of master:" + str(tcpaddress))
    send_tcp_message(tcpaddress)

def master_mode():
    cRoot.destroy()
    import master

def broadcast_recive():
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        client.bind(('', 37020))
        while True:
            data, addr = client.recvfrom(1024)
            #print("received message: %s"%data)
            print("recived from master :",addr)
            app.log("\nrecived from master :"+ str(addr))
            break;
        return addr
def send_tcp_message(tcpaddress):
        TCP_IP = tcpaddress
        TCP_PORT = 9001
        BUFFER_SIZE = 1024
        msg="Client "
        print(TCP_IP,TCP_PORT)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            time.sleep(random.randint(0,3))
            s.connect((TCP_IP,TCP_PORT))
        except:
            time.sleep(random.randint(0,4))
            s.connect((TCP_IP,TCP_PORT))
        s.send(msg.encode())
        print("tcp conn from client send to server!!!")
        app.log("\nTCP connection establishing!!!")
        url=s.recv(BUFFER_SIZE)
        print (url.decode())
        print(" \n")
        byte=s.recv(BUFFER_SIZE)
        print (byte.decode())
        #download starts here
        x=byte.decode()  #this variable might by named x as param to range                                                             #check if recived as string NOT byte
        url=url.decode()

        # 0 to file diff

        downloadFolder = dpath
        downloadname =str(url.split('/')[-1])#gives proper filename
        downloadpath=downloadFolder+downloadname
        print(downloadpath)
        # progressbar
        arr=x.split('-')
        print(arr)
        up=int(arr[1])
        print(up)
        arr2=arr[0].split('=')
        print(arr2)
        low=int(arr2[1])
        print(low)
        contentlength=up-low
        print(contentlength)
        remaining_download_tries = 5
        global file 
        
        try:
            print("starting download")
            app.log("\nStarting download")
            req = urllib.request.Request(url, headers={'Range':x})
            with urllib.request.urlopen(req) as fsrc,open(downloadpath,'wb')as fdst: #NamedTemporaryFile(delete=False) replace open () with Named..() for temp file download
                copyfileobj(fsrc,fdst,16*1024,contentlength)
                print("complete")
                app.log("\n Downloading Complete")
        except:
            #file=file+1
            
            #fdst.close()
            while remaining_download_tries > 0:
                try:
                    if file >= contentlength :
                        break
                    remaining_download_tries=remaining_download_tries-1
                    print("retrying download")
                    app.log("\n Downloading Failed\nRetrying download")

                    x='bytes='+str(file+low)+'-'+str(up)
                    print(x)
                    requ = urllib.request.Request(url, headers={'Range':x})
                    with urllib.request.urlopen(requ) as fsrc,open(downloadpath,'a+b')as fdst: #NamedTemporaryFile(delete=False) replace open () with Named..() for temp file download
                        copyfileobjr(fsrc, fdst,16*1024,contentlength)
                        print("complete")
                except:
                    fdst.close()
        if remaining_download_tries!=0:

            write_list=[s]
            with open(downloadpath,'rb') as f:
                readable, writable, errored = select.select([],write_list, [])   #check if reciving socket is ready
                for i in writable:
                    if i is s:
                        print("file sending.....")
                        app.log("\nfile sending.....please wait")
                        try:
                            
                            s.sendfile(f)
                        except:
                            filepointer=f.tell()
                            print("\nretrying file transfer to master\n")
                            s.sendfile(f,offset=filepointer)
        
            s.close()
            print("file send :::")
            app.log("\nfile send sucessfully  :-)")
        else:
            print("Download Error")
            app.log("\nDownload Error")

class Application(tk.Frame):
    def sclient(self):               #enter code to trigger master mode
        print("\n\tWelcome to PDS Downloader Client.\nSearching for masters\n\n")
        self.log("\n\tWelcome to PDS Downloader Client.\nSearching for masters\n\n")
        global urlVar
        urlVar = self.entry.get("1.0","end-1c")
        hereServe()
    def dirBox(self):
        global dpath
        text = fd.askdirectory(title = "Download Path")
        text = text + "/"
        print("Downloading path is set as :-->\n"+text)
        self.log("\nDownloading path is set as :-->\n"+text)
        dpath = str(text)
        self.insertToTextBox(dpath)
        self.entry.update()
        # activating the client mode
        self.sclient()
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        
        # progress bar
        frame2 = tk.Frame(master = cRoot)
        frame2.place(x=80,y=200)
        self.entry = tk.Text(master = frame2,width  = 50,height = 1)
        self.entry.pack()

        # button
        ok = tk.Button(cRoot, text='Directory Chooser',command=self.dirBox)
        ok.place(x=570,y=200)

        # logging
        frame1 = tk.Frame(master = cRoot)
        frame1.place(x=80,y=250)
        hello = "Choose a filepath to start download"
        self.editArea = st.ScrolledText(master = frame1,wrap = tk.WORD,width  = 58,height = 5)
        self.editArea.pack()
        # Adding some text, to see if scroll is working as we expect it
        self.editArea.insert(tk.INSERT,hello)
    def log(self,content):
        self.editArea.insert(tk.END,content)
        self.editArea.see(tk.END)
        self.editArea.update()
    def insertToTextBox(self,dpath):
        self.entry.insert(tk.INSERT,dpath)
    
   

#App
file=0
cRoot = tk.Tk()
cRoot.title("PDS Client")
cRoot.geometry("800x400")
#cRoot.iconbitmap(r"ico.xbm")
img = tk.PhotoImage(file='./logo.png')
cRoot.tk.call('wm', 'iconphoto', cRoot._w, img)
x = tk.Label(cRoot,text='Welcome to PDS App! Client Mode!').pack(side=tk.TOP,padx=10,pady=10)
# logo
image_logo = tk.PhotoImage(file="./logo.png")
label1 = tk.Label(image=image_logo)
label1.pack()

app = Application(master=cRoot)

def display_about(self):                      #enter about details here
    print("Add about here")


# menu here
menu = tk.Menu(cRoot)
cRoot.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_separator()
filemenu.add_command(label="Go Master Mode", command=master_mode)
filemenu.add_command(label="Exit", command=cRoot.quit)
helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=display_about)
app.mainloop()
cRoot.destroy()
