import socket
PORT = 6060

print("Sever is up and waiting for connection..")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), PORT))
s.listen(100) # Connections to listen too 


while True:
    clientsocket, address = s.accept()
    print(f"{address} has conncected..")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.send(bytes("testing!", "utf-8"))
    #print(clientsocket.recv(1024))
    print (f"{address} said: ", clientsocket.recv(1024))
    clientsocket.close()


