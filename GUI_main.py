
import tkinter as tk # this is for python3
import TCPMaster

class Application(tk.Frame):
    def master_function(self):               #enter code to trigger master mode
        #print("hi there, everyone!")
        mas=TCPMaster.broadCast()
        mas.call()

    def client_function(self):               #enter code to trigger client mode
        print("hi there, everyone!")


    def createWidgets(self):
        self.QUIT = tk.Button(self)

        # master button
        self.master = tk.Button(self)
        self.master["text"] = "MASTER",
        self.master["command"] = self.master_function
        self.master.pack({"side": "left"})

        # Client button
        self.client = tk.Button(self)
        self.client["text"] = "CLIENT",
        self.client["command"] = self.client_function
        self.client.pack({"side": "left"})
        
        # Quit 
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = tk.Tk()
app = Application(master=root)

def display_about(self):                      #enter about details here
    print("Add about here");

# menu here
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
# filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=display_about)
app.mainloop()
root.destroy()