#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:00:16 2020

@author: larsno
"""

import numpy as np

def sigmoid(x):
    return 1./(1.+np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x)*(1-sigmoid(x))

class NeuralNetwork:
    # skeleton code for a ANN with one hidden layer, and N nodes in the hidden layer (layer1).
    def __init__(self, x, y, N):
        # x is a column vector of inputs to the ANN
        self.input      = x
        self.test_x      = x
        # weights1 are the weights on links from inputs to hidden layer nodes, start with random weights
        self.weights1   = np.random.rand(self.input.shape[1],N)
        #self.weights1 = np.array([[0.05, 0.05, 0.05, 0.05, 0.05, 0.05],
        #                    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05],
        #                    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05],
        #                    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05]])
        # y is the output                
        self.y          = y
        #  Set the output to 0 to start with 
        self.output     = np.zeros(y.shape)
        # weights2 are the weights on links from the hidden nodes to the output layer
        self.weights2   = np.random.rand(N,self.output.shape[1]) 
        
    def feedforward(self):
        # The feedforward function first calculates the values in the hidden layer (layer1)
        # using the inputs and the weights on the links from input to hidden layer nodes
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        # And then the values in the output layer using weights on the links to the output
        self.output = sigmoid(np.dot(self.layer1, self.weights2))
        
    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2