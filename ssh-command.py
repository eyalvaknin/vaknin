#!/usr/bin/python


import subprocess
import sys

HOST=raw_input("Type Server:")

COMMAND=raw_input("Type Command:")

ssh = subprocess.call(["ssh", "root@%s" %HOST, COMMAND] )


