import socket 
PORT = 6060
print ("Enter a cool User Name")
username = input("[0]: ")


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), PORT))

    print ("Message you would like to send to server..")
    y = input("[0]: ")
    ting = (username + " : " + y)
    s.sendall(ting.encode())
    
    msg = "" 
    msg = s.recv(1024)
    print("messaged recv: " + msg.decode("utf-8"))
    s.close()
