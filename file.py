#!/bin/python3
#_*_ coding: utf8 _*_

#Start import block
import socket as sk
import getpass as gps
import os as linux
import time as delay
#End import block

hostname = sk.gethostname()
username = gps.getuser()

print ("Hi",username,"your machine is",hostname)
delay.sleep(1)
print ("Listing directory...")
delay.sleep(1)
linux.system('ls -al /usr/local/bin')