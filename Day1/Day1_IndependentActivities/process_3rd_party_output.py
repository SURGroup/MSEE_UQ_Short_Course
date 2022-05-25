import numpy as np
import meshio

def read_output(index):
    #Here you can read output files generated from the model runs
    mesh = meshio.read('./OutputFiles/cube_medium_hexa_'+str(index)+'.vtk')
    point_displacements=mesh.point_data['u']
    z_disp=list()
    for disp in point_displacements:
        z_disp.append(disp[2])
    return min(z_disp)