from keras.models import Sequential 
from keras.layers import Convolution2D, GlobalAveragePooling2D, Dense, Dropout, Conv2D, MaxPooling2D, Flatten, Lambda

def lenet(input_shape, comp=False, summary=False):
	model = Sequential()

	model.add(Conv2D(32, kernel_size=(3, 3), activation='relu',input_shape=input_shape))
	model.add(Conv2D(64, (3, 3), activation='relu'))
	
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.25))
	
	model.add(Flatten())
	
	model.add(Dense(128, activation='relu'))
	model.add(Dropout(0.5))

	model.add(Dense(265, activation='relu'))
	model.add(Dropout(0.5))
	
	model.add(Dense(1, activation='logistic'))
	
	if summary:
		model.summary()
	if comp:
		model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])

	return model