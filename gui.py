from tkinter.ttk import *
from tkinter import *
import tkinter as tk
import socket

# Creating the box
window = Tk()
window.title('ChetterHead')
window.geometry('500x500')
PORT = 6060

mylabel = Label(window, text = 'Send a message to [add user name here]', font = ("Purisa", 12))
mylabel.grid(row=0, column=0, sticky="NESW")

# Messages will be displayed here
BigWindow = Text(window, width=65)
BigWindow.grid(row=1, column=0, padx=10, pady=10)


def recv_mess():
    msg = ""
    msg = s.recv(1024)
    ser_msg = window.Message(master, text = msg.decode())
    ser_msg.config(bg='lightgreen', font=('times', 24, 'italic'))
    pass


def sending_message():
    message_data = message.get()
    user_data = user.get()
    empty = ""
    sending = message_data + ":" + user_data
    message.delete(0, tk.END)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), PORT))
    s.sendall(sending.encode())

    msg = ""
    msg = s.recv(1024)
    ser_msg = window.Message(master, text = msg.decode())
    ser_msg.config(bg='lightgreen', font=('times', 24, 'italic'))
    s.close()

def closeBox():
    window.destroy()



# User name exntry box here
user = tk.Entry(window, width=20)
user.insert(1,"Username: ")
user.grid(row=2, column=0)

# Message to send entry box
message = tk.Entry(window, width=50)
message.insert(0,"Your message: ")
message.grid(row=3, column=0)


# Buttonss to send and close window
btn = Button(window, text='Send', command=sending_message)
btn.grid(column=0, row=5)

#Closing window box
btn1 = Button(window, text='Quit', command=closeBox)
btn1.grid(column=0, row=5)


window.mainloop()

