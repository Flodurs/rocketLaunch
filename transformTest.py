import transforms
import numpy as np

vecA = np.array([1,0,0])
vecB = np.array([0,1,0])

angles=[np.pi,np.pi,np.pi]

print(transforms.rotation_x(vecA,np.pi/2))
print(transforms.rotation_x(vecB,np.pi/2))

print(transforms.rotation_xyz(vecA,angles))