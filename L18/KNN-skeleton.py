#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wednesday 2022-05-25

@author: antontv
"""
import numpy as np
import pandas as pd

#The preprocessing of data is done as in the neural network exercise. The skeleton code is below.

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


# The outputs data is the type columns from the flowers dataframe
outputs = LS[['type1','type2','type3']].to_numpy()

#### Everything below this point is what needs to be filled in ##################

#To perform the KNN, we need to calculate equlidian distance, which should 
#be done using the function below. (incomplete)
def equilidian_distance(x1, x2):
    #complete function
        
    return distance

#Function to compare classes
def result_cmpr(set1, set2):
    true = 0; false = 0
    
    for row in range(set1.shape[0]):
        if (set1[row,:] == set2[row,:]).all():
            true += 1
        else:
            false += 1
        
    return true,false

#Complete the function to compare the test set against your chosen k (incomplete)
def result_check(inputs_TS, outputs_TS, inputs, outputs):
    
    return accuracy

def KNN(inputs, outputs, k):
    
    #Choose the number of partitions of the inputs
    div = 5
    
    accuracy = []
    
    loop = 0
    while loop < div:
        smaller = inputs[(loop)*len(inputs)//div:(loop+1)*len(inputs)//div]
        bigger = np.delete(inputs,range((loop)*len(inputs)//div,(loop+1)*len(inputs)//div),axis=0)
        output_small = outputs[(loop)*len(inputs)//div:(loop+1)*len(inputs)//div]
        output_big = np.delete(outputs,range((loop)*len(outputs)//div,(loop+1)*len(outputs)//div),axis=0)
        
        nn = np.zeros((smaller.shape[0],3))
        #Complete the for loop
        for row in range(smaller.shape[0]):
            eq_dist = equilidian_distance(smaller[row,:], bigger)
            #....
        
        #identify which class the datapoints should be
        #....
         
        #identify accuracy
        true, false = result_cmpr(x1, x2)
        accuracy.append(true / (true+false))
        loop += 1
        
            
    return sum(accuracy)/len(accuracy)                      
    
    
    
#Function to run the KNN. Outputs the accuracy of the chosen k, to give some feedback on which value to choose.
k = 4#any choosen integer
accuracy = KNN(inputs, outputs, k)
print(accuracy)


#Checking the picked value of k against the test set.
inputs_TS = TS[['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width']].to_numpy()
max = np.amax(inputs_TS, axis=0)
min = np.amin(inputs_TS, axis=0)
inputs_TS = (inputs_TS-min)/(max-min)
outputs_TS = TS[['type1','type2','type3']].to_numpy()

accuracy = result_check(inputs_TS, outputs_TS, inputs, outputs)




