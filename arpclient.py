from socket import *
host='localhost'
port=8000
s=socket(AF_INET,SOCK_DGRAM)
while True:
    msg=input("Enter IP Address: ")
    s.sendto(msg,(host,port))