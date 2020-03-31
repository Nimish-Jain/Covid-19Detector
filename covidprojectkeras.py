# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:48:48 2020

@author: Nimish_Jain
"""

#importing libaries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('E:/Machine Learning/COVID19_line_list_data_cleanwop_archit.csv')
x=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.1,random_state=0)


# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense


# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 8, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))

# Adding the second hidden layer
classifier.add(Dense(units = 8, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 8, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(xtrain, ytrain, batch_size = 10, epochs = 100)




ypred=classifier.predict(xtest)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(ytest, ypred)

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
print ('Accuracy Score :',accuracy_score(ytest, ypred))
print ('Report : ')
print (classification_report(ytest, ypred)) 