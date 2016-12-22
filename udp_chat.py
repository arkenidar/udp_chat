#!/usr/bin/env python3


'''
from: https://thecodeninja.net/2014/12/udp-chat-in-python/

page contents:

UDP Chat in Python Using Socket
Here I will share a very basic UDP chat application in Python using sockets.
It can work in point-to-point or broadcast mode.
For Point-to-Point, enter IP and Port.
For Broadcasting mode set the last byte of IP address to 255. i.e. 192.168.0.255.
Port number is HEX, remove the base 16 to make it decimal.
'''

import socket
import sys, select
 
# Read a line. Using select for non blocking reading of sys.stdin
def getLine():
	i,o,e = select.select([sys.stdin],[],[],0.0001)
	for s in i:
		if s == sys.stdin:
			input = sys.stdin.readline()
			return input
	return False
 
ohost = input("Please Enter OUT-HOST-IP: ")
if not ohost: ohost = '127.0.0.1'
iport = int(input("Please Enter IN-PORT: "))
oport = int(input("Please Enter OUT-PORT: "))

 
send_address = (ohost, oport) # Set the address to send to
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # Create Datagram Socket (UDP)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Make Socket Reusable
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Allow incoming broadcasts
s.setblocking(False) # Set socket to non-blocking mode
s.bind(('', iport)) #Accept Connections on port
print("Accepting connections on port", iport)
 
while 1:
	try:
		message, address = s.recvfrom(8192) # Buffer size is 8192. Change as needed.
		if message:
			print(address, "> ", message.decode())
	except BlockingIOError:
		pass
 
	input = getLine()
	if(input != False):
		data_to_send=input.rstrip('\n').encode()
		print('sending',data_to_send,'to', send_address)
		s.sendto(data_to_send, send_address)
