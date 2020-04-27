#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:30:24 2020

@author: larsno
"""
import pandas as pd
import math
flowers =pd.read_csv("iris.csv")


def split (dataset, col, value):
# Split a dataset based on an value of an attribute in column 'col'
# The output is two DataFrames, consisting of the row from the initial dataframe
    lower = pd.DataFrame()
    higher = pd.DataFrame()
    for index, row in dataset.iterrows():
        if row[col] < value:
            lower=lower.append(row,ignore_index=True)
        else:
           higher=higher.append(row,ignore_index=True) 
    return lower, higher  
        
def find_instances(dataset, col):
# A function that return a lists of all possible instances in a column
    inst = list()
    for index,row in dataset.iterrows():
        if row[col] not in inst:
            inst.append(row[col])
    return inst

def count_instances(series,text):
# A function that counts the number of appearances of a string in a series
    count =0
    for i in range (len(series)):
        if series[i] == text:
            count+=1
    return count

def frequency (dataset, col, texts):
# Function that counts the appearance of each element from texts in col of dataset and returns
# the probability of its appearance
    prob = [0 for _ in range(len(texts))]
    for i in range (len(texts)):
        prob[i]=count_instances(dataset[col], texts[i])/len(dataset[col])
    return prob
    

def entropy(list):
    #The input to the function is a list of values, and the output is the entropy of that
    # list using base 2 for the logarithm
    entr=0
    for n in range (len(list)):
        if list[n] == 0:
            entr+=0
        else:
            entr+=list[n]*math.log(list[n],2)
    return -entr

# Lets put our methods to use. For instance, what is the entropy of our inital dataset?
# Since our entropy function expects a list of probabilities, we  need to figure out the
# probability that a flower is of a certain type, which we can do by first figuring out 
# which types of flowers there are in the dataset
    
types = find_instances(flowers,'Species')

# Then we can go ahead and count the number of appearances of each flower type and
# create a list of probabilities of each type of flower
#probabilities = [0,0,0]
#for i in range (len(types)):  
#    print (types[i], count_instances(flowers['Species'], types[i]))
#    probabilities[i] = count_instances(flowers['Species'], types[i])/len(flowers['Species'])

probabilities = frequency(flowers,'Species',types)

# So what is the entropy of the dataset?
print (entropy(probabilities))

# Lets now try to split the dataset along some column using some random value
lower,higher = split(flowers, 'Sepal.Length', 5.4)

# What is the entropy of the two new datasets?
below = entropy(frequency(lower,'Species',types))
above = entropy(frequency(higher,'Species',types))
print(below)
print(above)
# But since we now have two datasets, we need to determine the total information gain
# We do this by summing the new entropy values, multiplied by the weigth of 
# the two datasets in terms of their proportion of the original dataset
lower_weight = len(lower)/len(flowers)
higher_weight = len(higher)/len(flowers)
gain = entropy(probabilities)-lower_weight*below-higher_weight*above
print(gain)

    


        