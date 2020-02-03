#!/usr/bin/env python 

import getpass
import telnetlib

#Ask for User and PW
user = raw_input('Enter your telnet username: ')
password = getpass.getpass()

#Open file called SWITCHES
f = open('ALL')

for line in f:
	print 'Backup CFG ' + (line)
	HOST = line 

	tn = telnetlib.Telnet(HOST)
	tn.read_until("Username: ")
	tn.write(user + "\n")

	if password:
    		tn.read_until("Password: ")
    		tn.write(password + "\n")

	tn.write('term len 0\n')
	tn.write('show run\n')
	tn.write('wr\n')

	tn.write("exit\n")

        readoutput = tn.read_all()
        saveoutput = open(HOST, "w")
        saveoutput.write(readoutput)
	saveoutput.close

 
