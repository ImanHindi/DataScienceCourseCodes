import pandas as pd
import numpy as np


s=pd.Series()
s
#series from array
data=np.array([1,2,3,4])
print(data)
s=pd.Series(data)
print(s)

#series from dictionary

data=np.array([[1,2],[3,5]])

df=pd.DataFrame(data,columns=['age','name'])
print(df)

data={'Name':['y','x','z','t'],'age':['1','2','3','4']}
df=pd.DataFrame(data,index=['x1','x2','x3','x4'])
print(df)
#retrieve data using label(index)
#s=pd.Series([1,2,3,4,5]),index=['A','B','C',]