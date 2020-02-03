#!/usr/bin/env python 

import getpass
import sys
import telnetlib

HOST = "2.2.2.2"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("conf t\n")

tn.write("int loop  99\n")
tn.write("ip add 99.99.99.2 255.255.255.255\n") 

tn.write("end\n")
tn.write("wr\n")
tn.write("exit\n")

print tn.read_all()
