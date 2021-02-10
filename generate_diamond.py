# Created by Francesco Mambretti on 25/06/2020
# Physical units in nm
# generates a diamond cell filled of trivalent patchy particles

import numpy as np
import os
import random

n_elem_cell=16 # number of particles(nanostars) in an elementary cell
sides_elem_cell=np.zeros(3)

density=$RHO #nm^-3

sides_elem_cell[0]=1
sides_elem_cell[1]=1
sides_elem_cell[2]=2.59808

# set lattice step in nm
lattice_step=round(np.cbrt(n_elem_cell/(sides_elem_cell[0]*sides_elem_cell[1]*sides_elem_cell[2]*density)),4)
print('lattice_step is '+str(lattice_step)+' nm')

for i in range (3):
	sides_elem_cell[i]*=lattice_step

#soft-center/patch-center distance and patch radius
r_sc=5.7 #nm
r_p=0.5*r_sc

coords_elem_cell=np.zeros((n_elem_cell,4)) #3 coordinates + 0/1 for z-patch up or down

####initialize coordinates
coords_elem_cell[0]=(1,0,0.433013,1)
coords_elem_cell[1]=(0.5, 0.5, 0.433013,1)
coords_elem_cell[2]=(1, 0.5, 1.29904,0)
coords_elem_cell[3]=(0.5, 0, 1.29904,0)
coords_elem_cell[4]=(0.75, 0.75, 1.08253,1)
coords_elem_cell[5]=(0.25, 0.25, 1.08253,1)
coords_elem_cell[6]=(0.25, 0.75, 1.94856,0)
coords_elem_cell[7]=(0.75, 0.25, 1.94856,0)
coords_elem_cell[8]=(1, 0, 0, 0)
coords_elem_cell[9]=(0.5, 0.5, 0, 0)
coords_elem_cell[10]=(0.75, 0.75, 0.649519,0)
coords_elem_cell[11]=(0.25, 0.25, 0.649519,0)
coords_elem_cell[12]=(1,0.5,1.73205,1)
coords_elem_cell[13]=(0.5, 0, 1.73205,1)
coords_elem_cell[14]=(0.25, 0.75, 2.38157,1)
coords_elem_cell[15]=(0.75, 0.25, 2.38157,1)

### translate them into nanometers
for i in range (16):
	for j in range(3):
        	coords_elem_cell[i][j]=coords_elem_cell[i][j]*lattice_step

#replicate elementary cell in the space
cells_x=4
cells_y=4
cells_z=2

coords_global=np.zeros((cells_x*cells_y*cells_z*n_elem_cell,3))

#choose mixing ratio
x_A=$X_A

#significant digits
sd=4

with open('config.diamond', 'w') as f:
	print(cells_x*cells_y*cells_z*n_elem_cell,file=f)
	print(density,file=f)
	counter=0

	for i in range (0,cells_x):
		for j in range (0, cells_y):
			for k in range (0, cells_z):
				for l in range (0, n_elem_cell):
					counter+=4

					#choose nanostar type
					if (random.uniform(0, 1) >= x_A):
						species=1
					else:
						species=0
					x0=coords_elem_cell[l][0]+i*sides_elem_cell[0]
					y0=coords_elem_cell[l][1]+j*sides_elem_cell[1]
					z0=coords_elem_cell[l][2]+k*sides_elem_cell[2]

	
					print(round(x0,sd),round(y0,sd),round(z0,sd),species,file=f)
					#print patches
					if (coords_elem_cell[l][3]==0):
						print(round(x0,sd),round(y0,sd),round(z0+r_sc,sd),species,file=f)
						print(round(x0,sd),round(y0+np.cos(np.pi/6)*r_sc,sd),round(z0-np.sin(np.pi/6)*r_sc,sd),species,file=f)
						print(round(x0,sd),round(y0-np.cos(np.pi/6)*r_sc,sd),round(z0-np.sin(np.pi/6)*r_sc,sd),species,file=f)

					elif(coords_elem_cell[l][3]==1):
						print(round(x0,sd),round(y0,sd),round(z0-r_sc,sd),species,file=f)
						print(round(x0,sd),round(y0-np.cos(np.pi/6)*r_sc,sd),round(z0+np.sin(np.pi/6)*r_sc,sd),species,file=f)
						print(round(x0,sd),round(y0+np.cos(np.pi/6)*r_sc,sd),round(z0+np.sin(np.pi/6)*r_sc,sd),species,file=f)
