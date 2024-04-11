import numpy as np

def rotation_x(vec,angle):
    rot = np.array([[1,0,0],[0,np.cos(angle),-np.sin(angle)],[0,np.sin(angle),np.cos(angle)]])
    return np.matmul(rot,vec)
    
def rotation_y(vec,angle):
    rot = np.array([[np.cos(angle),0,np.sin(angle)],[0,1,0],[-np.sin(angle),0,np.cos(angle)]])
    return np.matmul(rot,vec)

def rotation_z(vec,angle):
    rot = np.array([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,1]])
    return np.matmul(rot,vec)
    
def rotation_xyz(vec,angles):
    #xyz cardan order
    return rotation_z(rotation_y(rotation_x(vec,angles[0]),angles[1]),angles[2])
