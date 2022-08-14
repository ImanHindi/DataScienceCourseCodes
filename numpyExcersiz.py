import numpy as np
import pandas as pd
x=np.array([[10, 11, 12],
            [19, 20, 21],
            [22, 23, 24]])
#return the index
#y=np.argmin(x, axis=1)
#z=np.argmin(x, axis=0)
#
#y=np.argmax(x, axis=1)
#z=np.argmax(x, axis=0)
#print(y)
#print(z)
#
##to return the exact values:
#
#y=np.max(x, axis=1)
#z=np.max(x, axis=0)
#
#print(x[np.argsort(x[:,1])]) #sorted array based on col

#print(x[np.argsort(x[1,:])]) #sorted based on row


D={'ID':pd.Series([1,2,3,4,5,6,7,8,9,10],index=[1,2,3,4,5,6,7,8,9,10]),
    'CompanyName':pd.Series(['Orange','Orange','Orange','Orange','Orange','Zain','Zain','Zain','Zain','Zain'],index=[1,2,3,4,5,6,7,8,9,10]),
    'Budget': pd.Series([100,100,100,100,100,100,100,100,100,100],index=[1,2,3,4,5,6,7,8,9,10])}
df=pd.DataFrame(D)

print(df)
Summary = df.groupby('CompanyName')['Budget'].sum()
print(Summary)