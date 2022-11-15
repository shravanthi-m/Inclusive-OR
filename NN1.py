#Perceptron: consists of 2 neurons in inputs column and 1 neuron in output column
#Neural network returns outputs according to inclusive or that is:
#if X is true and Y is true then X or Y is true
#if X is true and Y is false then X or Y is true
#if X is false and Y is true then X or Y is true
#if X is false and Y is false then X or Y is false

import numpy, random, os
lr = 1 #learning rate
bias = 1 #value of bias
weights = [random.random(), random.random(), random.random()] 
#weights gen. in list (3 weigths for 2 neurons and bias)
#weights will be modifies (generated randomly)

def Perceptron(input1, input2, output):
    outputP = input1*weights[0] + input2*weights[1] + bias*weights[2]
    if outputP > 0:
        outputP = 1
        #activation function (heaviside)
    else:
        outputP = 0
    error = output - outputP
    weights[0] += error * input1 * lr
    weights[1] += error * input2 * lr
    weights[2] += error * bias * lr
    
#above function defines work of the output neuron
#error is calculated and used to modify weights of every connection to output


#loop that makes neural network repeat situation several times
#part of learning phase
for i in range(50):
    Perceptron(1,1,1) #True or true
    Perceptron(1,0,1) #True or false
    Perceptron(0,1,1) #False or true
    Perceptron(0,0,0) #False or false


x = int(input("Enter first value: "))
y = int(input("Enter second value: "))
outputP = x*weights[0] + y*weights[1] + bias*weights[2]
if outputP > 0: #activation function
    outputP = 1
else:
    outputP = 0
print(x, "or", y, "is: ",outputP)

outputP = 1/(1+numpy.exp(-outputP)) #sigmoid function