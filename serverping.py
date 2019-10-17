import os
import time
import socket
from datetime import datetime
try:
	s=socket.socket(socket.AF_INET, socket.SOCK_RAW,socket.IPPROTO_ICMP)
except socket.error:
        print("")
	#print('Socket could not be created. Error Code :' + str(msg[0]) + 'Message' + msg[1])
class ipheader:
	types=8
	code=0
	checksum=0
	iden=0
	seq=0
class echoreply:
	head=ipheader()
	times=int(round(time.time()*1000))
	datas="req"
ecreply=echoreply()
ecreply.head.iden=ecreply.head.iden+1
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(),8890))
sock.listen(1)
connection, client_address = sock.accept()
try:
        data= connection.recv(16)
        if data:
                print(data[0])
                print("RTT:",(ecreply.times-int(round(time.time()*1000))))
                os.system("ping "+data)           
finally:
        sock.close()
        connection.close()
