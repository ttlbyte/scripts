#!/usr/bin/env python
# encoding: utf-8


import numpy as np
import getopt,sys
import matplotlib.pyplot as plt

print "initial aims is to plot partial dos for FHI-aims! "
print "=================================================="
print "You can use it for plotting other things"
print "reading data from commandline"
print "Usage:plotdos.py -o offset x x_col -y y_col file1 file2 ..."
color_sequence = ['#1f77b4',  '#ff7f0e', '#ffbb78', '#2ca02c','#aec7e8',
                  '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
                  '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f',
                  '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']

fig, ax = plt.subplots(1,1,figsize=(10,6))
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.xlabel('Energy/eV')

filename='pdos.dat'
x=0
y=1
off_coef=0
fig_title=' '

def readdata(fa):
    fo=open(fa)
    data=np.genfromtxt(fo,comments='#',usecols=(x,y))
    X=[]
    Y=[]
    for i in data:
        X.append(i[0])
        Y.append(i[1])
    #X=asarray(X)
    #Y=asarray(Y)
    return X,Y




if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:],'o:x:y:t:')
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)
    for i in opts:
        if i[0]=='-x':
            x=int(i[1])
        if i[0]=='-y':
            y=int(i[1])
        if i[0]=='-o':
            off_coef=float(i[1])
        if i[0]=='-t':
            fig_title=i[1]
    namespace=args
    num_of_line=len(namespace)
    if num_of_line == 0:
        namespace.append(filename)
    majors=[]
    for i in namespace:
        majors.append(i.split('/')[-1].split('.')[0])
    offset = range(10)
    x_axis=[]
    y_axis=[]
    labelspace=[]
    for i in namespace:
        tmp_x,tmp_y = readdata(i)
        x_axis.append(tmp_x)
        y_axis.append(tmp_y)
    for i in range(num_of_line):
       tmp,= plt.plot(np.array(x_axis[i]),np.array(y_axis[i])+off_coef*offset[i], lw=2.5,color=color_sequence[i],label=majors[i])
       labelspace.append(tmp)
    plt.legend(handles=labelspace)
    plt.title(fig_title)
    plt.show()

