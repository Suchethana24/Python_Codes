import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)

# resizing the array
a.shape = (3,2)
print(a)

# printing dimension of array
a = np.arange(24)
print(a.ndim)
print(a)

# finding no.of elements in an array
print(a.size)

