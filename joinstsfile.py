#!/usr/bin/env python3
import os
path='/home/ruan/git/stm/'
#path为文件所在目录，windows下如‘D:\\data\\’,直接覆盖源文件，请注意保存原始数据
for file in os.listdir(path):
    os.rename(os.path.join(path,file),os.path.join(path,file.split('.')[2][2:]))
filenu = len(os.listdir(path)) + 1
data=[]
with open(os.path.join(path,'001'),'rb') as fo:
    for line in fo.readlines()[526:]:
        data.append([line.decode('ascii').split('\t')[1],line.decode('ascii').split('\t')[5]])
j=2
while j<filenu :
    with open(os.path.join(path,str(j).zfill(3)),'rb') as fo:
        i=0
        for line in fo.readlines()[526:]:
            data[i].append(line.decode('ascii').split('\t')[5])
            i+=1
    j+=1
with open(os.path.join(path,'final.txt'),'w') as fout:
    i=len(data)
    j=len(data[0])
    k=0
    while k<i:
        l=0
        while l<j:
            fout.write(data[k][l])
            fout.write('\t')
            l+=1
        fout.write('\n')
        k=k+1
