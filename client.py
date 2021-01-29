import socket 
PORT = 6060
print ("Enter a cool User Name")
username = raw_input("> ")


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), PORT))

    print ("Message you would like to send to server..")
    y = raw_input("> ")
    ting = (username + " said " + y)
    s.sendall(ting.encode())
    
    s.close()



#while True:
   # z = input("> ")
   # z = "testing"
    #s.sendall(z.encode())
    
   # msg = s.recv(1024)
   # print(msg.decode("utf-8"))
    
   # s.close()
