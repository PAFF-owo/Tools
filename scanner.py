#!/bin/python3

import socket
import sys
import datetime

if len(sys.argv)  == 2:
	target = socket.gethostbyname(sys.argv[1])

else:
	print("invaild amount of arg")

try:
	for port in range(1,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print ("port {} is open".format(port))
		s.close()
except KeyboardIntreput:
	sys.exit()

except socket.gaierror:
	sys.exit()

except socket.error:
	sys.exit()
