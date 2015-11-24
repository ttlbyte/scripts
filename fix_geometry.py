#!/usr/bin/python
import sys, os
fo=open('geometry.in','r');
fw=open('output','w');
line=fo.readline();
while(len(line)>2):
	if len(line.split())<5:
		fw.write(line);
	elif ((float(line.split()[3])-5.6)<0.00001):
		fw.write(line);
		fw.write("constrain_relaxation .true.\n");
	else:
		fw.write(line);
	line=fo.readline();
fw.close();
fo.close();

os.system('mv output geometry.in')
