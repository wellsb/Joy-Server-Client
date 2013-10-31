#!/usr/bin/env python

import sys
import socket
from subprocess import call
import os

#create server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 1010))
server.listen(1)
conn, addr = server.accept()
print "\nServer Started"
print 'Connect: ', addr
data = 'nothing'

while True:
	if (data == 'quit') or (data == ''):
		print "\nClosing Socket"
		server.close()
		break
	data = conn.recv(1024)
	print 'RECV: ', data
	#conn.sendall(data)
	
	if data:
		got = data.split(',',3)
		print "got 0: "+str(got[0]) #y L\R
		print "got 1: "+str(got[1]) #x U\D
		print "got 1: "+str(got[2]) #Throt

		os.system("echo 0=%s > /dev/servoblaster" % (got[0])) #base
		os.system("echo 1=%s > /dev/servoblaster" % (got[1])) #arm

sys.exit()
