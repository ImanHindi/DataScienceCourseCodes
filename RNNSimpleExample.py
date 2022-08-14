from tabnanny import verbose
from matplotlib import units
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense , SimpleRNN


def converttomatrix(data,step):
    x,y=[],[]
    for i in range(len(data)-step):
        d=i+step
        x.append(data[i:d,])
        y.append(data[d,])

    return np.array(x),np.array(y)
n=1000
tp=800

t=np.arange(0,n)
x=np.sin(.02*t)+2*np.random.randn(n)

df=pd.DataFrame(x)
print(df.head())

plt.plot(df)
plt.show()
values=df.values
train,test=values[0:tp,:],values[tp:n,:]


step=4
#test=np.repeat(test[-1,],step)
test = np.append(test, np.repeat(test[-1,], step))
train = np.append(train, np.repeat(test[-1,], step))


trainx,trainy=converttomatrix(train,step)
testx,testy=converttomatrix(test,step)


trainx=np.reshape(trainx,(trainx.shape[0],1,trainx.shape[1]))
testx=np.reshape(testx,(testx.shape[0],1,testx.shape[1]))


model=Sequential()

model.add(SimpleRNN(units=32,input_shape=(1,step),activation='relu'))
model.add(Dense(8,activation="relu"))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer='rmsprop')
model.summary()

model.fit(trainx,trainy,epochs=100,batch_size=16,verbose=2)
trainpredict=model.predict(trainx)
testpredict=model.predict(testx)
predicted=np.concatenate((trainpredict,testpredict),axis=0)
trainscore=model.evaluate(trainx,trainy,verbose=0)
print(trainscore)
