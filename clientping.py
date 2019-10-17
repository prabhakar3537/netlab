import time
import socket
import sys
from datetime import datetime
try:
        s=socket.socket(socket.AF_INET, socket.SOCK_RAW,socket.IPPROTO_ICMP)
except socket.error:
        print("")
        #print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
class ipheader:
	types=0
	code=0
	checksum=0
	iden=0
	seq=0
class echoreq:
	head=ipheader()
	times=int(round(time.time()*1000))
	datas="req"
ecreq=echoreq()
ecreq.head.iden=ecreq.head.iden+1
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(),8890))
try:
       message = raw_input("Enter the input: ")
       sock.sendall(message)
finally:
       print("")
sock.close()
