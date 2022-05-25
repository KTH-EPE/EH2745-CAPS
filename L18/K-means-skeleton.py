#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wednesday 2022-05-25

@author: antontv
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

# Select only the input columns from the dataframe and convert it to a Numpy
# array to speed up calculations
inputs = flowers[['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width']].to_numpy()

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

#### Everything below this point is what needs to be filled in #################


#To perform the k-nearest-neighbor, we need to calculate equlidian distance, which should 
#be done using the function below. (incomplete)
def eq_distance(x1, x2):
    #complete function
        
    return distance

#Calculates mean of number of datapoints (incomplete)
def calc_mean(data, types):

    return new_means

#Calculates difference between previous and new mean values, to see if algorithm
#should stop (incomplete)
def calc_diff(x1, x2):
    diff = np.zeros(len(x1))

    return diff

#Calculate cost (incomplete)
def calc_cost(data, means, types):

    return cost

def kmeansclustering(inputs, init_guess = 3):
    n_of_data = inputs.shape[0]
    k = 1 #Number of centroids (initializes at one, increases as algorithm runs) until cost difference is small
    J_min = None #Minimum cost
    J_r = [] #saved costs
    means_r = []
    
    means_thresh = 1e-4
    while(True):
        print("k {}".format(k))
        loop = 0
        #loop by picking random starting element equal to init_guess number of times
        while loop < init_guess:
            init_mean = np.zeros((k, inputs.shape[1]))
            print("loop {}".format(loop))
            i = 0
            
            for i in range(k):
                init_mean[i,:] = inputs[np.random.randint(inputs.shape[0]),:]
            

            dist_from_mean = np.zeros(k)
            means_diff = np.ones(k)
            
            #Continue while new means are different from old ones. Main
            #part of the algorithm.
            curr_means = init_mean
            while np.sum(means_diff) > means_thresh:
                belong_to = np.zeros(n_of_data)
        
                #find new means using eq_distance & calc_mean functions
                
                #Assign new means, calculate difference
                prev_means = curr_means
                curr_means = next_means
                means_diff = calc_diff(prev_means, curr_means)
            
            #Calculate cost of the current means
            J = 0
            #... continue implementation here
            
            #If cost is less than previous attempt, replace the previous result
            #from your previous guess
            if J_min == None:
                J_min = J
                means = curr_means
            elif J < J_min:
                J_min = J
                means = curr_means
                
            loop +=1
            
        #Check if the exit condition is fulfilled.
        if k == 1:
            prev_J = J_min
            J_r.append(J_min)
            means_r.append(means)
            print(J_min)
        elif k > 1:
            diff_J = abs(prev_J - J_min)
            J_r.append(J_min)
            means_r.append(means)
            print(J_min)
            if diff_J < 10:
                break
            else:
                prev_J = J_min
        k += 1
    
    #Returns number of means, the cost function for the best value & the mean values in vector means
    return k, J_r, means_r

#k here equals number of centroids
k, J_r, means_r= kmeansclustering(inputs)





