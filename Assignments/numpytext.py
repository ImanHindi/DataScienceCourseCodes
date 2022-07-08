import numpy as np

a=np.array([[1,2,3],[1,2,3],[1,2,3],[1,2,3]])

print(a.T)
print(a)

a.mean()

import numpy as np
#find repitition in array
#way1
values = np.array([1,2,3,1,2,4,5,6,3,2,1])
searchval = 2
ii = np.where(values == searchval)[0]
print(ii)

#way2
unique, count = np.unique(values, return_counts= True)

np.linalg.inv (a)
#merge arrays together
np.vstack(a,values)
np.hstack(a,values)

#reverse for an array
print(np.flip(values))



#The original array

arr = [11, 22, 33, 44, 55]

print("Array is :",arr)

 

res = arr[::-1] 
#reversing using list slicing

print("Resultant new reversed array:",res)