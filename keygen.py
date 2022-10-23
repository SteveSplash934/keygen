#!/usr/bin/python3

import random
import os
def hexDump(key):
	num = 0
	for x in key:
		num += ord(x)
	return num

pwd = ""
while True:
	pwd += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-")
	if hexDump(pwd) > 415:
		pwd= ""
	elif hexDump(pwd) == 415:
		print("Found Possible key: ", pwd)


