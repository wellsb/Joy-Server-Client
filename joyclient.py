#!/usr/bin/env python
import pygame
import time
import sys
import socket
#import os

def goexit():
	print "exit"
	print "\nClosing Connection"
	server.close()
	pygame.quit()
	sys.exit()

# Initialize stuff
pygame.init()
pygame.joystick.init()
pygame.display.init()

joystick_count = pygame.joystick.get_count()
#print("Number of joysticks: "+str(joystick_count))

for js in range(joystick_count):
	joystick = pygame.joystick.Joystick(js)
	joystick.init()
	
name = joystick.get_name()

#axes = joystick.get_numaxes()
#print("# of axes: "+str(axes))

#create connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('192.168.5.180', 1010))

for main in range(0,1000):
	print chr(27) + "[2J"
	print (main)
	print (name)
	pygame.event.pump()
	ax = joystick.get_axis(0)
	ay = joystick.get_axis(1)
	at = joystick.get_axis(2)
	print "Raw X:" +str(ax)
	print "Raw Y:" +str(ay)
	print "Raw T:" +str(at)
	x = int(round(((ax+1)*100)+40, 0))
	y = int(round(((ay+1)*100)+40, 0))
	t = int(round(((at+1)*100)+40, 0))
	print "X:" +str(x)
	print "X:" +str(y)
	print "T:" +str(t)
	listed = [x,y,t]
	telem = ','.join(map(str, listed))
	print telem

	server.send(telem)
	#data = server.recv(1024)
	#print 'RECV: ', repr(data)
	
	time.sleep(0.1)

goexit()