import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

D={'one':pd.Series([1,2,3],index=['A','B','C']),
    'two':pd.Series([1,2,3,4],index=['A','B','C','D'])}

df=pd.DataFrame(D)
df['Three']=pd.Series([1,2,3,4],index=['A','B','C','D'])
df['Four']=df['one']+df['Three']
print(df['Four'].dtype)
print(df['Four'].astype(float))
print(df['Four'].dtype)



plt.suptitle("this is the super title")
x=np.array([1,2,3,4,5,6,7,8,9])
y=np.array(['500','55','77','88','90','130','270','300','370'])
z=np.array([200,300,1000,500,10,50,800,1000,100])

x=np.array(['A','B','C','D','E','F','G','H','I'])
#plt.scatter(x,y,alpha=(z/1000),s=10,c='r')
#plt.colorbar()

y=y.astype(int)


#plt.barh(x,y,height=.1)
#plt.show()
#y=np.array([40,150,150,100,30,60,90,150,150])
plt.bar(x,y,width=.1)
plt.show()
#The histogram is a popular graphing tool. 
# It is used to summarize discrete or continuous data that are measured on an interval scale. 
# It is often used to illustrate the major features of the distribution of the data in a convenient form.
#plt.hist(y)
#plt.show()
#labels=np.array(['40','150','100','30','60','90'])
#plt.pie(y,explode=[0,.1,0,0,0,0],labels=labels)
#plt.legend(title="data")
#plt.show()

