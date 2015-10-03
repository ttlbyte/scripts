#!/usr/bin/python
import sys
fo=open('geometry.in','r');
fw=open('output','w');
line=fo.readline();
while(len(line)>2):
#	if (((float(line.split()[3])-0.024)>0.000001)and((float(line.split()[3])-0.21)<0.0001)):
	if ((float(line.split()[3])-5.6)<0.00001):
		fw.write(line);
		fw.write("constrain_relaxation .true.\n");
	else:
		fw.write(line);
	line=fo.readline();
fw.close();
fo.close();
