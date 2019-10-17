import operator
import math
import socket
import threading
from thread import *

list_of_IP = []
list_assign = []
def decimalToBinary(n): 
    return bin(n).replace("0b","") 
#BIN TO DEC
def binaryToDecimal(n): 
    return int(n,2) 

def changeBits(binIP, n, zeroOne):
	for i in range(len(binIP)-1,len(binIP)-n-1,-1):
		binIP[i] = zeroOne
	return binIP

class SUBNET:
	s = 0
	IP = []
	n = 0
	def __init__(self, i,n):
		self.s = i
		self.n = n
		self.IP = []
	def assign(self,host,ip,tot):
		binHost = decimalToBinary(host)
		if(len(binHost) < 8):
			for j in range(8 - len(binHost)):
				binHost = '0'+binHost
		binHost = list(binHost)
		nBit = int(math.ceil(math.log(self.n,2)))
		temp = 2**nBit	
		if(temp > 256 and n > 254 and tot <255):
			print("cannot assign IP as limit it reached")
			exit()
		#print(nBit)
		#binHost = changeBits(binHost,nBit,'0')
		newStartIP = ip[0]+'.'+ip[1]+'.'+ip[2]+'.'
		ending = str(int(ip[3]) + 1)
		start = newStartIP+ending
		#binHost = changeBits(binHost,nBit,'1')
		ending = str(int(ip[3]) + temp)
		end = newStartIP+ending
		print(start)
		print(end)
		#ip = end
		for i in range(int(start.split('.')[3]),int(end.split('.')[3])+1):
			self.IP.append(newStartIP+str(i))
			#print(newStartIP+str(i))
		ip = []
		ip = list(end.split('.'))
		print(ip)
		return ip
		#print(IP)
		#print(s)
def socketFunc(conn,IP):
	
	j = 0
	while True:
		#print("i connect")
		#conn.send('Connected successfully')
		try:
			msg = conn.recv(2048)
			#print("its me")
			if(msg):
				if(msg[0] == 'S'):
					i = int(msg[1])
					while True:
						j = j%len(list_of_IP[i])
						if(list_assign[i][j] == 0):
							conn.send(list_of_IP[i][j])
							list_assign[i][j] = 1
							print(list_of_IP[i][j]+" alloted")
							break
						j = j+1
				if(msg[-1] == 'r'):
					for p in range(len(list_of_IP)):
						for q in range(len(list_of_IP[i])):
							if(list_of_IP[p][q] == msg[:-1]):
								list_assign[p][q] = 0
								print(msg[:-1]+" available")
				#print(msg)
			else:
				break
		except:
			break				
list_of_subnet = []

#for sorting list of obj  -> lO.sort(key=operator.attrgetter('s'))
ip = raw_input("Enter IP address\n")
IP_sock = ip
ip = ip.split('.')
ip = list(ip)
ip[3] = "0"
tot = 0
print(ip)
no_of_subnet = int(raw_input("Enter number of subnet\n"))
for i in range(no_of_subnet):
	n = int(raw_input("Enter number of hosts for "+str(i+1)+" subnet\n"))
	list_of_subnet.append(SUBNET(i+1,n))
list_of_subnet.sort(key=operator.attrgetter('n'),reverse = True)
for i in list_of_subnet:
	print(i.s,i.n)
	tot = tot + i.n
	ip = i.assign(int(ip[3]),ip,tot)
	list_of_IP.append(i.IP)
	list_assign.append([0]*len(i.IP))
	print(i.IP)
print("--------------------------------------------")
print(list_of_IP)
print(list_assign)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
port = int(raw_input("Enter port\n"))
server.bind((IP_sock,port))
print('server connected')
server.listen(1)
	
while True: 

    conn, addr = server.accept()
    start_new_thread(socketFunc,(conn,IP_sock)) 



