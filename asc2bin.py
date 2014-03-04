#!/usr/bin/python

import sys
import re

stdin = sys.stdin.read()

data = re.sub(r'[^a-zA-Z0-9]','', stdin)

try:
	print data.decode("hex")
except TypeError:
	print "[+] Error: Odd number of characters supplied"
	exit()
