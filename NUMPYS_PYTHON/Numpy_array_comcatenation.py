# concatination two arrays
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([7,8,9])
print(np.concatenate((a,b,c)))

# stack array row wise vertically
print(np.vstack((a,b,c)))

# stack array row wise horizontally
print(np.hstack((a,b,c)))

# combine coloumn wise
print(np.column_stack((a,b,c)))

