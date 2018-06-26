import scipy, numpy as np
import numpy.core.records as ncr

#print(scipy.version.full_version)
#print(scipy.dot is numpy.dot)

a=np.array([0,1,2,3,4,5,6,7,8,9,10,11])
print(a)
print(ncr.array([0,1,2,3,4,5,6]))
print(a.ndim)
print("Shape - ",a.shape)
b=a.reshape((3,4))
print("Reshape ",b)
b[1][0]=77
print("Reassign Value ",b)
print(a*2)
print(a**2)
print([0,1,2,3,4,5,6,7,8,9,10,11]*2)
print(a>4)




