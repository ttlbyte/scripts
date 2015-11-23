#!/usr/bin/env python
import numpy as np
class grid(object):
    def __init__(self, line):
        self.x=float(line.split()[0])
        self.y=float(line.split()[1])
        self.z=float(line.split()[2])
        self.value=float(line.split()[3])

fw=open('stmimg.txt', 'w')
fo=open('grid1.txt', 'r')
line=fo.readline()
fo.close()
point=grid(line)
a=[point.z,]
b=[np.log(point.value),]
value=np.log(0.000008)
print(str(point.x)+' '+str(point.y)+' '+str(point.z)+' '+str(point.value))
with open('grid1.txt', 'r') as fo:
    for line in fo.readlines():
        point1=grid(line)
        if ((point.x==point1.x)and(point.y==point1.y)):
            a.append(point1.z)
            b.append(np.log(point1.value))
        else:
            x=np.array(a)
            y=np.array(b)
            z=np.polyfit(x,y,1)
            data=(value-z[1])/z[0]
            fw.write(str("%9.5f" % point.x)+'    '+str("%9.5f" % point.y)+'    '+str("%9.5f" % data)+'\n')
            point=point1
            a=[point.z,]
            b=[np.log(point.value),]
x=np.array(a)
y=np.array(b)
z=np.polyfit(x,y,1)
data=(value-z[1])/z[0]
fw.write(str("%9.5f" % point.x)+'    '+str("%9.5f" % point.y)+'    '+str("%9.5f" % data)+'\n')
fw.close()
