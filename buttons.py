from Tkinter import *
master = Tk()

def callback():

    execfile("script.py")
b = Button(master, text="OK", command=callback)
b.pack()
mainloop()

