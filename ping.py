from socket import *
import os
import sys
import struct
import time
import select
import binascii  

ICMP_ECHO_REQUEST = 8
packets_lost = 0
min_rtt = 1000000
max_rtt = 0
SEQ = 0

def MyChecksum(hexlist):

    summ=0
    carry=0

    for i in range(0,len(hexlist),2):
        summ+=(hexlist[i]<< 8)  + hexlist[i+1]
        carry=summ>>16
        summ=(summ & 0xffff)  + carry
    while( summ != (summ & 0xffff)):
        carry=summ>>16
        summ=summ & 0xffffffff  + carry

    summ^=0xffff

    return summ
    
def receiveOnePing(mySocket, ID, timeout, destAddr, seq):

    timeLeft = timeout
    global min_rtt
    global max_rtt
    global packets_lost
    global SEQ
    global bytes
    
    while 1: 
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []:
            packets_lost += 1       
            print("Request timed out.")
            delay = -1
            return delay

        timeReceived = time.time() 
        recPacket, addr = mySocket.recvfrom(1024)
        
        if (addr[0] == destAddr):
            ICMP_header = recPacket[20:28] 
            time_pack = recPacket[28:36]  
            type, code, checkSum, packetID, SEQ = struct.unpack("bbHHh", ICMP_header) 
            time_sent = struct.unpack("d", time_pack) 
            delay = (timeReceived - time_sent[0])*1000 
            checksum = MyChecksum(recPacket[20:])
            
            bytes_header = recPacket[3:4]
            bytes = struct.unpack("b", bytes_header)
            if (packetID == ID and type == 0 and code == 0 and checksum == 0 and seq == SEQ):
                if (delay < min_rtt):
                    min_rtt = delay   
                if (delay > max_rtt):
                    max_rtt = delay   
                return delay    
        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            packets_lost += 1
            print("Request timed out.")
            delay = -1
            return delay
    
def sendOnePing(mySocket, destAddr, ID, seq):
    myChecksum = 0

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, seq)
    data = struct.pack("d", time.time())

    myChecksum = MyChecksum ([i for i in header] + [i for i in data])
    
    myChecksum = htons(myChecksum)
        
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, seq)
    packet = header + data
    
    mySocket.sendto(packet, (destAddr, 1)) 

def doOnePing(destAddr, timeout, seq): 

    icmp = getprotobyname("icmp")

    mySocket = socket(AF_INET, SOCK_RAW, icmp)
    
    myID = os.getpid() & 0xFFFF  
    sendOnePing(mySocket, destAddr, myID, seq)
    delay = receiveOnePing(mySocket, myID, timeout, destAddr, seq)
    mySocket.close()
    return delay
    
def ping(host, howmany, timeout=1):

    try: 
        dest = gethostbyname(host)
    except error:
        print("\nINVALID HOST NAME")
        return 0
    print("Pinging " + dest + " using Python:")
    print("")
    pings = int(howmany)
    seq = 1
    
    while (pings != 0):
        delay = doOnePing(dest, timeout, seq)
        if (delay != -1):
            print("Reply from " + dest + ": " "Bytes: " + str(bytes[0]) + "   time = %.3f ms" % delay + "   seq # = " + str(SEQ))
        pings -= 1
        seq += 1
        time.sleep(1)
    if (packets_lost == 0): 
        perc_lost = 0
    if (packets_lost != 0):
        perc_lost = (packets_lost/int(howmany)) * 100
    received = int(howmany) - packets_lost
    print("\nPing statistics for: " + dest)
    print(" Packets: Sent = " + howmany + ", Received = " + str(received) + ", Lost = " + str(packets_lost) + " (" + str(perc_lost) +"% loss)")
    if (perc_lost != 100):
        print("Approximate RTT in milli-seconds: ")
        print(" Minimum = %.3f ms" % min_rtt + ", Maximum = %.3f ms" % max_rtt)
host=input("Enter Host: ")
nos=input("Enter Number of packets to be sent: ")       
ping(host,nos)
