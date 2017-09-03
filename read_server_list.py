#!/usr/bin/python

filepath = raw_input("Type your file path contain server list:")

ServerList = []
with open(filepath, "r") as f:
    for line in f:
        ServerList.append(line)
#       print ServerList

i = 0
while i < len(ServerList):
    print (ServerList[i])
    i += 1


