
#training model command line:
#python CatAndDogsClassifierEdited.py --dataset C:\Users\user\Desktop\iman\MLlibraries\dogs-vs-cats\train --model output/CatAndDogsClassifier.hdf 

#testing model command line :
#    python CatAndDogsClassifiertesterEdited.py --model output/CatAndDogsClassifier.hdf --test-images C:\Users\user\Desktop\iman\MLlibraries\dogs-vs-cats\test




# import the necessary packages
from cgi import test
from random import seed
import random
from os import listdir, makedirs
from shutil import copyfile

from turtle import color
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Activation
from keras.optimizers import SGD,Adam
from keras.layers import Dense,Conv2D,MaxPooling2D,Flatten,Dropout
from keras.utils import np_utils 
from keras.callbacks import EarlyStopping
from keras.preprocessing.image import ImageDataGenerator
from imutils import paths #A series of convenience functions to make basic
# image processing functions such as translation, rotation, resizing,
# skeletonization, and displaying Matplotlib images easier with OpenCV 
import numpy as np
import argparse
import cv2
import os

def image_to_feature_vector(image, size=(128, 128)):
	# resize the image to a fixed size, then flatten the image into
	# a list of raw pixel intensities
	return cv2.resize(image, size)
#
#
#
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
ap.add_argument("-m", "--model", required=True,
	help="path to output model file")
args = vars(ap.parse_args())
# grab the list of images that we'll be describing
print("[INFO] describing images...")
imagePaths = list(paths.list_images(args["dataset"]))
# initialize the data matrix and labels list
data = []
labels = []
#
### create data generators
train_datagen = ImageDataGenerator(#rescale=1.0/255.0,
	width_shift_range=0.1, height_shift_range=0.1, horizontal_flip=True)
##test_datagen = ImageDataGenerator(rescale=1.0/255.0)
### prepare iterators
##data.append(train_datagen.flow(imagePaths,
##	class_mode='binary', batch_size=64, target_size=(128, 128)))
##labels.append(test_datagen.flow_from_directory(imagePaths,
##	class_mode='binary', batch_size=64, target_size=(128, 128)))
#
#
## loop over the input images
#for (i, imagePath) in enumerate(imagePaths):
#	# load the image and extract the class label (assuming that our
#	# path as the format: /path/to/dataset/{class}.{image_num}.jpg
#	image = cv2.imread(imagePath)

#	label = imagePath.split(os.path.sep)[-1].split(".")[0]
#	# construct a feature vector raw pixel intensities, then update
#	# the data matrix and labels list
#	features = image_to_feature_vector(image)
#	data.append(features)
#	labels.append(label)
#	# show an update every 1,000 images
#	if i > 0 and i % 1000 == 0 or i==25000:
#		print("[INFO] processed {}/{}".format(i, len(imagePaths)))
#


## encode the labels, converting them from strings to integers
le = LabelEncoder()
labels = le.fit_transform(labels)
## scale the input image pixels to the range [0, 1], then transform
## the labels into vectors in the range [0, num_classes] -- this
## generates a vector for each label where the index of the label
## is set to `1` and all other entries to `0`
#data = np.array(data) / 255.0
labels = np_utils.to_categorical(labels, 2)
#print(labels.shape)
#print(type(labels))
#print(data.shape)
## save the reshaped photos
#np.save('dogs_vs_cats_photos.npy', data)
#np.save('dogs_vs_cats_labels.npy', labels)

# load and confirm the shape
data = np.load('dogs_vs_cats_photos.npy')
labels = np.load('dogs_vs_cats_labels.npy')


# partition the data into training and testing splits, using 75%
# of the data for training and the remaining 25% for testing
print("[INFO] constructing training/testing split...")
(trainData, testData, trainLabels, testLabels) = train_test_split(data, labels, test_size=0.10, random_state=42)


num_filters_1=32
num_filters_2=64
num_filters_3=128
filter_size=3
pool_size=2
model=Sequential([
    Conv2D(num_filters_1,filter_size,input_shape=(128,128,3),kernel_initializer='he_uniform',strides=1,padding='same'),
    Activation("relu"),
    MaxPooling2D(pool_size, strides=(2, 2)),
	Dropout(0.2),
    
    Conv2D(num_filters_2,filter_size,strides=1,kernel_initializer='he_uniform',padding='same'),
	Activation("relu"),
    MaxPooling2D(pool_size),
    Dropout(0.25),

	Conv2D(num_filters_3, filter_size, activation='relu', kernel_initializer='he_uniform', padding='same'),
	MaxPooling2D(pool_size),
    Flatten(),
	Dropout(.2),

	Dense(128,activation='relu',kernel_initializer='he_uniform'),
	Dropout(.5),

    Dense(2,activation='softmax')
])
# train the model using ADAM
print("[INFO] compiling model...")

adam=Adam(learning_rate=0.001)
early_stopping = EarlyStopping(monitor='val_loss', patience=5)

model.compile(loss='binary_crossentropy', optimizer=adam,metrics=['accuracy'])

history = model.fit(train_datagen.flow(trainData,trainLabels,batch_size=60),
		validation_data=[testData, testLabels], 
		 epochs=50,callbacks= [early_stopping], verbose=2)
#print(history.history)
# show the accuracy on the testing set
print("[INFO] evaluating on testing set...")
(val_loss, val_accuracy) = model.evaluate(testData, testLabels,batch_size=128, verbose=1)
print("[INFO] loss={:.4f}, accuracy: {:.4f}%".format(val_loss,val_accuracy * 100))



plt.subplot(211)
plt.title("loss")
plt.plot(history.history['loss'],color='blue',label='train')
plt.plot(history.history['val_loss'],color='orange',label='test')
plt.subplot(212)
plt.title("Accuracy")
plt.plot(history.history['accuracy'],color='blue',label='train')
plt.plot(history.history['val_accuracy'],color='orange',label='test')
plt.savefig('results_plot.png')
plt.close()
plt.show()


# dump the network architecture and weights to file
print("[INFO] dumping architecture and weights to file...")
model.save(args["model"])



