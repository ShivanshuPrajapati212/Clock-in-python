from tkinter import *
from datetime import datetime

root = Tk()

root.geometry("1080x720")\

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")
    am_pm = now.strftime("%p")

    time_label = Label(text=f"{current_hour}:{current_minute}:{current_second}",font="comicsansm 180 bold",bg="black",fg="white",padx=2000,pady=2000)
    time_label.pack(anchor='center',fill=X)


    root.mainloop()