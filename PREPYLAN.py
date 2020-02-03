#!/usr/bin/env python 

import getpass
import sys
import telnetlib

HOST = "4.4.4.4"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")

tn.write("int loop  99\n")
tn.write("ip add 99.99.99.4 255.255.255.255\n") 

tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
