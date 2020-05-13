#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 08:49:04 2020

@author: larsno
"""
import numpy as np
import pandas as pd
        
#Start main program by reading the now famous datafile with flowers into a pandas datafram
flowers = pd.read_csv('iris.csv')
np.random.seed(2)

# Next is to add three columns to the dataframe that represent the class of flower
# First, define three empty lists
type1 = []
type2 = []
type3 = []

# Iterate through the flowers dataframe and set the appropriate type value to 1 
for flower_type in flowers['Species']:
    if flower_type == 'setosa':
        type1.append(1),  type2.append(0), type3.append(0)
    if flower_type == 'versicolor':
        type1.append(0), type2.append(1), type3.append(0)     
    if flower_type == 'virginica':
        type1.append(0), type2.append(0), type3.append(1)


# Add the type columns to the flowers dataframe. We now have a numeric value (1 or 0)
# To represent the type of flower.
flowers['type1'] = type1
flowers['type2'] = type2
flowers['type3'] = type3

# Separating the DataFrame into a Learning set and a Test set

LS = pd.DataFrame()
TS = pd.DataFrame()
LS_Setosa = flowers[:40]
TS_Setosa = flowers[40:50]
LS_Versicolor = flowers[50:90]
TS_Versicolor = flowers[90:100]
LS_Virginica = flowers[100:140]
TS_Virginica = flowers[140:150]
LS = LS.append(LS_Setosa, ignore_index=True)
LS = LS.append(LS_Versicolor, ignore_index=True)
LS = LS.append(LS_Virginica, ignore_index=True)
TS = TS.append(TS_Setosa, ignore_index=True)
TS = TS.append(TS_Versicolor, ignore_index=True)
TS = TS.append(TS_Virginica, ignore_index=True)

# Select only the input columns from the dataframe and convert it to a Numpy
# array to speed up calculations
inputs = LS[['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width']].to_numpy()

#print(inputs)

# In order to normalize the data, we find the max and min values for each of
# the  columns in the inputs
max = np.amax(inputs, axis=0)
min = np.amin(inputs, axis=0)


# Using numpy array magic, we go through the inputs array and regularize all values
inputs = (inputs-min)/(max-min)

#print(inputs)

# The outputs data is the type columns from the flowers dataframe
outputs = LS[['type1','type2','type3']].to_numpy()

# Finally, we can build a Neural Network using the input and output
# The number of input nodes is the number of columns in the 'inputs' array, the number of output
# nodes is the number of columns in the 'outputs' array. Finally, we can freely chose the number
# nodes in the hidden layer
ANN = NeuralNetwork (inputs, outputs,6)

# Next step is to train the ANN, by feeding forward data from the input array
# and then tuning the weights to try match the 'output' array to the outputs 
# using the backpropagation algorithm

for i in range (10000):
    NeuralNetwork.feedforward(ANN)
    NeuralNetwork.backprop(ANN)
print (ANN.output)









