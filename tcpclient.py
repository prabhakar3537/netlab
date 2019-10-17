from socket import *
host='localhost'
port=8081
s=socket(AF_INET,SOCK_STREAM)
s.connect((host,port))
while True:
    msg=input("Enter Message: ")
    s.sendall(msg.encode())
    reply=s.recv(1000)
    print("Server: ",reply.decode())
s.close()