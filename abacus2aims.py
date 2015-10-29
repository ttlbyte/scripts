#!/usr/bin/env python

import sys, os
if os.path.exists('STRU'):
	pass;
else:
	print("STRU file does not exist!\n")
	exit(-1);
vectorlist=[]
vectorlists=[]
atomtype=[]
atom_coor=[]
atom_coor_full=[]
b2a=0.52917706

with open('STRU', 'r') as fin:
	line=fin.readline();
	while(len(line)>0):
		while(line[0]=='\s'):
			line=line[1:]
		if len(line)<=1:
			line=fin.readline();
			continue;
		if line[0]=='#':
			pass;
		if line.split()[0]=='ATOMIC_SPECIES':
			line=fin.readline()
			while(len(line)>9):
				atomtype.append(line.split()[0])
				line=fin.readline()
			continue;
		if line.split()[0]=='LATTICE_CONSTANT':
			line=fin.readline()
			cons=float(line.split()[0])
		if line.split()[0]=='LATTICE_VECTORS':
			for i in range(3):
				line=fin.readline();
				if len(line)<5:line=fin.readline()
				vectorlist.append([line.split()[0], line.split()[1], line.split()[2]])
		if line.split()[0]=='ATOMIC_POSITIONS':
			line=fin.readline()
			coor=line.split()[0]
		if line.split()[0] in atomtype:
			line=fin.readline()
			line=fin.readline()
			num=int(line.split()[0])
			for i in range(num):
				line=fin.readline()
				list=line.split()
				atom_coor.append([list[0], list[1], list[2], list[3], list[4], list[5]])
			atom_coor_full.append(atom_coor)
			atom_coor=[]
		line=fin.readline()

for i in vectorlist:
	vectorlists.append([float(i[0])*cons*b2a, float(i[1])*cons*b2a, float(i[2])*cons*b2a])


if coor=='Cartesian':
	for list in atom_coor_full:
		for j in list:
			j[0]=str('%.8f' % (float(j[0])*b2a))
			j[1]=str('%.8f' % (float(j[1])*b2a))
			j[2]=str('%.8f' % (float(j[2])*b2a))


with open('geometry.in', 'w') as fo:
	for i in vectorlists:
		fo.write('lattice_vector\t')
		for j in i:
			fo.write(str("%.8f" % j)+'  ')
		fo.write('\n')
	if coor=='Cartesian':
		for i in range(len(atomtype)):
			for j in atom_coor_full[i]:
				fo.write('atom\t'+j[0]+' '+j[1]+' '+j[2]+' '+atomtype[i]+'\n')
				if not(int(j[3]) and int(j[4]) and int(j[5])):
					fo.write('constrain_relaxation .true.\n')
				elif not(int(j[3])):
					fo.write('constrain_relaxation x \n')
				elif not(int(j[4])):
					fo.write('constrain_relaxation y \n') 
				elif not(int(j[5])):
					fo.write('constrain_relaxation z \n') 
	else:
	 	for i in range(len(atomtype)):
			for j in atom_coor_full[i]:
				fo.write('atom_frac\t'+j[0]+' '+j[1]+' '+j[2]+' '+atomtype[i]+'\n')
				if not(int(j[3]) and int(j[4]) and int(j[5])):
					fo.write('constrain_relaxation .true.\n')
				elif not(int(j[3])):
					fo.write('constrain_relaxation x \n') 
				elif not(int(j[4])):
					fo.write('constrain_relaxation y \n')
				elif not(int(j[5])):
					fo.write('constrain_relaxation z \n')
