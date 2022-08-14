import tensorflow as tf


from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Activation, Dense,Flatten


model=Sequential()

layer1=Dense(8,input_shape=(4,4))
model.add(layer1)
layer2=Flatten()
model.add(layer2)
model.summary()