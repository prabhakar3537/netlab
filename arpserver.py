from socket import *
host='localhost'
port=8000
ipaddr=["192.168.117.100","192.168.117.101","192.168.117.114"]
macaddr=["44:45:ff:78:df:45","45:cc:45:89:ab:df","44:87:fc:67:da:bb"]
s=socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))
while True:
    msg,addr=s.recvfrom(1000)
    try:
        index=ipaddr.index(msg)        
        print(macaddr[index])
    except:
        print("Invalid IP Address")
conn.close()
