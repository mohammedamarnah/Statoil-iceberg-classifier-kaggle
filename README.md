# Statoil/C-CORE Iceberg Classifier Challenge
## Ship or iceberg, can you decide from space?

This is my first participation in kaggle contest. This solution implements a convolutional neural network that handles two inputs; One is the angle that the image was taken from, the other one is an image with two channels: HH (transmit/recieve horizontally), and HV(transmit horizontally and recieve vertically).

A very important step before training is the data augmentation. Data augmentation was done with the help of the keras ImageDataGenerator function. The data augmentation consisted of horizontal flipping, vertical flipping, zooming and rotation.

After that, a "Min-Max Stacking" step was implemented to even decrease the loss of the model. This should get a score of ~ 0.1478. Further improvements are being developed.
