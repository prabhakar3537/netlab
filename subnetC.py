import socket
import select

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

IP = raw_input("Enter IP\n")
port = int(raw_input("Enter port\n"))
s = int(raw_input("Enter the subnet number\n"))
client.connect((IP,port))
print('connected')
client.send("S"+str(s))
temp_IP = client.recv(1024)
if(temp_IP):
	print(temp_IP)
	q = raw_input()
	if(q == "close"):
		client.send(temp_IP+"r")
