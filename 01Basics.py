import numpy as np
a = np.array([1,2,3])
print(a)
b = np.array([[9.0,8.0,7.0],[6.0,5.0,7.8]])
print(b)
print(a.ndim, b.ndim)
print(a.shape, b.shape)
print(a.dtype, b.dtype)
print(a.itemsize, b.itemsize)
print(a.nbytes, b.nbytes)

c = np.array([1,2,3,4,5], dtype = 'int16')
print(c.dtype)
print(c.itemsize)
print(c.nbytes)