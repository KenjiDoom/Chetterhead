from tkinter import * 
import tkinter as tk

# Creating the box
window = Tk()
window.title('ChetterHead')
window.geometry('400x400')

mylabel = Label(window, text = 'Send a message to server', font = ("Purisa", 12))
mylabel.grid(row=0, column=0, sticky="NESW")

def send_message():
    pass


def closeBox():
    window.destroy() 


btn = Button(window, text='Send', command=send_message)
btn1 = Button(window, text='quit', command=closeBox) #Closes the window after 

btn.grid(column=0, row=4, sticky=tk.W)
btn1.grid(column=1, row=4, sticky=tk.E)



window.mainloop()
