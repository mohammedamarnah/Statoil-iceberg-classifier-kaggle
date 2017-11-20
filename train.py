import os
import models
import utils

import pandas as pd
import numpy as np 

from subprocess import check_output

###### TRAINING CONSTANTS ######
SPLIT = 0.2
BATCH_SIZE = 64
EPOCHS = 25
VAL_SAMPLES = 30000
SAMPLES_PER_EPOCH = (20000//BATCH_SIZE)*BATCH_SIZE
############################

# Check Files Availability
print(check_output(["ls", "./dataset/"]).decode("utf8"))

# Reading the dataset (Training/Testing)
trainjson = pd.read_json('./dataset/train.json')
testjson = pd.read_json('./dataset/test.json')

# Splitting the training and validation data
train_num = (trainjson.shape[0]*SPLIT)
training_data = trainjson.loc[0:train_num-1]
validation_data = trainjson.loc[train_num:]

# Freeing the memory from that big shit
trainjson = None

# # Generate training data and validation data
# train = utils.gen_batch(training_data, BATCH_SIZE)
# valid = utils.gen_batch(validation_data, BATCH_SIZE)

# model = models.lenet(input_shape=(64,64,1), comp=True, summary=True)

# history = model.fit_generator(train, samples_per_epoch=SAMPLES_PER_EPOCH,
#                             nb_epoch=EPOCHS, validation_data=valid,
#                             nb_val_samples=VAL_SAMPLES)

# json = model.to_json()
# model.save_weights('../../save/model.h5')
# with open('../../save/model.json', 'w') as f:
#     f.write(json)




