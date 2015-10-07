#!/usr/bin/env python3
import os, re
path=r'/home/ruan/git/stm/'
namespace={}
data=[]
for file in os.listdir(path):
     if re.match('A\d{6}\.\d{6}\.L\d{4}\.VERT',file): namespace[int(file.split('.')[2][2:])]=file
keys=sorted([x for x in namespace.keys()])
with open(os.path.join(path,namespace[keys[0]]),'rb') as fo:
    for line in fo.readlines()[526:]:
        data.append([line.decode('ascii').split('\t')[1],])
for i in keys:
    with open(os.path.join(path,namespace[i]),'rb') as fo:
        j=0
        for line in fo.readlines()[526:]:
            data[j].append(line.decode('ascii').split('\t')[5])
            j+=1
with open(os.path.join(path,'final.txt'),'w') as fout:
    for line in data:
        for num in line:
            fout.write(num+'\t')
        fout.write('\n')
