#!/usr/bin/env python3

'''
http://stackoverflow.com/questions/2408560/python-nonblocking-console-input
'''

import sys
import threading
import queue

def add_input(input_queue):
	while True:
		input_queue.put(sys.stdin.read(1))

input_queue = queue.Queue()
input_thread = threading.Thread(target=add_input, args=(input_queue,))
input_thread.daemon = True
input_thread.start()

def getLine():
	out=[]
	while True:
		if not input_queue.empty():
			got=input_queue.get()
			if got!='\n':
				out.append(got)
			else:
				return ''.join(out)
		else:
			return None

def testGetLine():
	while True:
		line = getLine()
		if line is not None:
			print('line', line)

def bInput(prompt):
	writef(prompt)
	while True:
		line = getLine()
		if line is not None:
			return line

def writef(text):
	sys.stdout.write(text)
	sys.stdout.flush()

'''
from: https://thecodeninja.net/2014/12/udp-chat-in-python/

page contents:

UDP Chat in Python Using Socket
Here I will share a very basic UDP chat application in Python using sockets.
It can work in point-to-point or broadcast mode.
For Point-to-Point, enter IP and Port.
For Broadcasting mode set the last byte of IP address to 255. i.e. 192.168.0.255.
'''

import socket

ohost = bInput("Please Enter OUT-HOST-IP: ")
if not ohost: ohost = '127.0.0.1'
iport = int(bInput("Please Enter IN-PORT: "))
oport = int(bInput("Please Enter OUT-PORT: "))

send_address = (ohost, oport) # Set the address to send to
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # Create Datagram Socket (UDP)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Make Socket Reusable
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Allow incoming broadcasts
s.setblocking(False) # Set socket to non-blocking mode
s.bind(('', iport)) #Accept Connections on port
print("Accepting connections on port", iport)

import time

while True:
	try:
		message, address = s.recvfrom(8192) # Buffer size is 8192. Change as needed.
		if message:
			print(address, "> ", message.decode())
	except BlockingIOError:
		pass
 
	line = getLine()
	if(line != None):
		data_to_send=line.rstrip('\n')
		print(send_address,'<',data_to_send)
		s.sendto(data_to_send.encode(), send_address)
	else:
		time.sleep(1)
