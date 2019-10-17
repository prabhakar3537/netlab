from socket import *
host='localhost'
port=8081
s=socket(AF_INET,SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn,addr=s.accept()
print("Connected Successfuly")
while True:
    msg=conn.recv(1000)
    print("Client: ",msg.decode())
    reply=input("Enter Message: ")
    conn.sendall(reply.encode())
conn.close()