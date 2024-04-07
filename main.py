from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")
root.geometry('1950x1200')
root.minsize(1950,1200)
root.maxsize(1950,1200)

def time():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000,time)



label = Label(font=('Calibri',250,'bold'),background="black",foreground="cyan",anchor='center',padding=(200,320))
label.pack(anchor='center',side='top',fill='both')
time()

mainloop()