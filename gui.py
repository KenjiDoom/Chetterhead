from tkinter.ttk import *
from tkinter import * 
import tkinter as tk
import socket 

# Creating the box
window = Tk()
window.title('ChetterHead')
window.geometry('400x400')
PORT = 6060

mylabel = Label(window, text = 'Send a message to server', font = ("Purisa", 12))
mylabel.grid(row=0, column=0, sticky="NESW")

#selected = IntVar()

def recv_message():
    pass

def send_message():
    message_data = message.get()
    user_data = user.get()
    empty = ""
    sending = message_data + ":" + user_data
    message.delete(0, tk.END)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), PORT))
    s.sendall(sending.encode())
    s.close()

def closeBox():
    window.destroy() 


btn = Button(window, text='Send', command=send_message)
btn1 = Button(window, text='quit', command=closeBox) #Closes the window after 


btn.grid(column=0, row=3, sticky=tk.W)
btn1.grid(column=1, row=3, sticky=tk.W)

# Message to send to server entry box
message = tk.Entry(window, width=40)
message.grid(row=2, column=0)

# User exntry box here
user = tk.Entry(window, width=20)
user.grid(row=1, column=0)



window.mainloop()

