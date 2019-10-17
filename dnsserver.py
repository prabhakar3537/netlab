from socket import *
import sys
host='localhost'
port=8081
s=socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))
while True:
    conn,addr=s.recvfrom(1024)
    z=gethostbyname(conn)
    if(z==conn):
        try:
            zx=gethostbyaddr(conn)
            print("Domain Name= "+zx[0])
        except:
            print("Unknown Host")
    else:
        try:
            print("IP address= "+z)
        except:
            print("Unkown Host")