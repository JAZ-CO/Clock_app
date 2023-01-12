import tkinter as tk
import time

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Digital Clock")

        self.clock = tk.Label(self.root, font=("Calibri", 90), bg="grey", fg="black")
        self.clock.pack()
        self.get_time()

        self.frame = tk.Frame(self.root)
        self.frame.columnconfigure(0,weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.button1 = tk.Button(self.frame,bg="Black",width=5,height=3,command=(self.make_black))
        self.button1.grid(row=0,column=0,sticky="news")
        self.button2 = tk.Button(self.frame,bg="White",width=5,height=3, command=(self.make_white))
        self.button2.grid(row=0,column=1,sticky="news")

        self.frame.pack(side="bottom")

        self.copyRight = tk.Label(self.root,text="by Jalal")
        self.copyRight.pack(side="bottom",anchor="s")
        self.root.mainloop()

    def get_time(self):

        self.clock.update()
        timeVar = time.strftime("%I:%M:%S %p")
        self.clock.config(text=timeVar)

        self.clock.after(200, self.get_time)


    def make_black(self):

        self.clock.destroy()
        self.clock = tk.Label(self.root, font=("Calibri", 90), bg="Black", fg="White")
        self.get_time()
        self.clock.pack(side="top")
    def make_white(self):

        self.clock.destroy()
        self.clock = tk.Label(self.root, font=("Calibri", 90), bg="White", fg="black")
        self.get_time()
        self.clock.pack(side="top")

GUI()
