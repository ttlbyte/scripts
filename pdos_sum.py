#!/usr/bin/env python
# encoding: utf-8

import re
import numpy as np
import os

match=re.compile('atom_project')
namespace=[]
data=[]
for file in os.listdir('.'):
    if re.match(match,file):namespace.append(file)
output=open("pdos.dat",'w')
a=namespace[0]
sam=open(a)
lines=sam.readlines()
for i in lines:
    if i.startswith('#'):
        output.write(i)
sam.close()
sam=open(a)
data=np.genfromtxt(sam,comments='#')
sam.close()
namespace=namespace[1:]
for i in namespace:
    tmp=open(i)
    datatmp=np.genfromtxt(tmp,comments='#')
    tmp.close()
    if len(data[0])==len(datatmp[0]):
        for j in range(len(data)):
            for k in range(len(data[0])-1):
                data[j][k+1] = data[j][k+1] + datatmp[j][k+1]
    elif len(data[0])<len(datatmp[0]):
        for j in range(len(data)):
            for k in range(len(data[0])-1):
                data[j][k+1] = data[j][k+1] + datatmp[j][k+1]
            for n in datatmp[k+2]:
                data[j].append(n)
    else:
        for j in range(len(data)):
            for k in range(len(datatmp[0])-1):
                data[j][k+1] = data[j][k+1] + datatmp[j][k+1]

prefix='    '
posfix='\n'
for i in data:
    line=''
    for j in i:
        line=line+str("%10.8f" % j)+'        '
    line=prefix+line[:-8]+posfix
    output.write(line)
output.close()
