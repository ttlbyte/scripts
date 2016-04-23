#!/usr/bin/env python
from ase import io
atoms = io.read('/home/ruan/Documents/ZnO_slab/aims.cif')
atoms.write('POSCAR", format = 'vasp')
