from socket import *
host='localhost'
port=8081
s=socket(AF_INET,SOCK_DGRAM)
while True:
    msg=input("Enter: ")
    s.sendto(msg, (host,port))