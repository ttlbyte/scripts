#!/usr/bin/env python
etot=[]
with open('Log.txt') as fo:
	data=fo.readlines()
	last=data[0]
	for line in data:
		if line.startswith(' ETOT') and not last.startswith(' !!'):etot.append(last[8:].split(' ')[0])
		last=line
	for i in range(1,len(etot)+1):
		print(str(i)+' '+etot[i-1])
