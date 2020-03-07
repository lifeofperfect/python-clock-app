import sys
from tkinter import *
import time

#the clock funtion
def clock():
    currentTime = time.strftime("%H:%M:%S") #strf is to stingify the time
    digital.config(text=currentTime) #gets current local time from your computer
    digital.after(200, clock) #get time every 200 mili seconds

root = Tk()#tk function
root.geometry('400x300')# size of the app

header = Label(root, text='Digital clock', font="times 25 bold") # header
header.grid(row=0, column=2)#position

digital = Label(root, font="times 50 bold", bg='white')
digital.grid(row=2, column=2, padx=100, pady=50)
clock()

label = Label(root, text="Hour  Minute  Seconds", font="times 20 bold")
label.grid(row=3, column=2)

root.mainloop()