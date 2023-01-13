import tkinter as tk #We'll mostly depend on this
import time #just to get the time

class GUI:

    def __init__(self):
        self.root = tk.Tk() 
        self.root.title("Digital Clock")

        #Label means the text just like paragraph in html
        self.clock = tk.Label(self.root, font=("Calibri", 90), bg="grey", fg="black")
        self.clock.pack()

        self.get_time() #call the function inside class

        self.frame = tk.Frame(self.root) #this is the frame that the button will go inside it
        self.frame.columnconfigure(0,weight=1) # I don't know about these
        self.frame.columnconfigure(0, weight=1)

        #below is buttons
        self.button1 = tk.Button(self.frame,text="Black",bg="Black",fg="Black",width=5,height=3,command=(self.make_black))
        self.button1.grid(row=0,column=0,sticky="news")
        self.button2 = tk.Button(self.frame,text="White",bg="White",width=5,height=3, command=(self.make_white))
        self.button2.grid(row=0,column=1,sticky="news")

        self.frame.pack(side="bottom")

        self.copyRight = tk.Label(self.root,text="by Jalal")
        self.copyRight.pack(side="bottom",anchor="s")
        self.root.mainloop()

    def get_time(self):

        self.clock.update() #update the time
        timeVar = time.strftime("%I:%M:%S %p")#hr:min:sec am/pm

        self.clock.config(text=timeVar) #this is to show it in window I guess

        self.clock.after(200, self.get_time) #for every 2ms, call the function again


    def make_black(self):

        self.clock.destroy() #we did this in order not to stack up
        self.clock = tk.Label(self.root, font=("Calibri", 90), bg="Black", fg="White")
        self.get_time() #This calls the function again so we could show it again after destroy
        self.clock.pack(side="top") #to keep it at top
    def make_white(self):

        self.clock.destroy()
        self.clock = tk.Label(self.root, font=("Calibri", 90), bg="White", fg="black")
        self.get_time()
        self.clock.pack(side="top")

GUI()# call the class
