#!/usr/bin/env python 

import getpass
import sys
import telnetlib


user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

f = open('MANAGEMENT')

for line in f:
	print "DEL LOOPBACK 100 " + (line)
	HOST =  line 

	tn = telnetlib.Telnet(HOST)
	tn.read_until("Username: ")
	tn.write(user + "\n")

	if password:
    		tn.read_until("Password: ")
    		tn.write(password + "\n")

	tn.write("conf t\n")
	tn.write("no int lo100\n")

	tn.write("end\n")
	tn.write("wr\n")
	tn.write("exit\n")

	print tn.read_all()
 
