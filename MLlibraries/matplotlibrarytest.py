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



#df.replace('')
plt.suptitle("this is the super title")
x=np.array([1,2,3,4,5,6,7,8,9])
y=np.array([43,55,77,88,90,130,270,300,370])
plt.subplot(3,2,1)
plt.plot(x,y)
plt.title("title1")
x1=np.array([1,2,3,4,5,6,7,8,9])
y1=np.array([43,55,77,88,90,130,270,300,370])
plt.subplot(3,2,2)
plt.plot(x,y)
plt.title("title1")


x3=np.array([1,2,3,4,5,6,7,8,9])
y3=np.array([43,55,77,88,90,130,270,300,370])

plt.subplot(3,2,3)
plt.plot(x,y)
plt.title("title1")


x4=np.array([1,2,3,4,5,6,7,8,9])
y4=np.array([43,55,77,88,90,130,270,300,370])
plt.subplot(3,2,4)

plt.plot(x,y)
plt.title("title1")


x5=np.array([1,2,3,4,5,6,7,8,9])
y5=np.array([43,55,77,88,90,130,270,300,370])
plt.subplot(3,2,5)

plt.plot(x,y)
plt.title("title1")

x6=np.array([1,2,3,4,5,6,7,8,9])
y6=np.array([43,55,77,88,90,130,270,300,370])

plt.subplot(3,2,6)

plt.plot(x,y)
plt.title("title1")

#plt.xlabel('time')
#plt.ylabel('temp')
#plt.title('test')
plt.grid(axis='x',color='green',linestyle='--',linewidth=.5)
plt.show()




