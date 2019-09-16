# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:12:33 2019

@author: gynjkm
"""
"""
Model:
# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.
    
"""
#importing packages

import random
import math

#Assinging variables x0 and y0

y0 = random.randint(0,99)
x0 = random.randint(0,99)

print("y0 is", y0)
print("x0 is", x0)

#Building an algorithm to randomise the value of y0 one step

if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
print("After our first step y0 is now", y0)

#Building an algorithm to randomise the value of x0 one step

if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
    
print("After our first step x0 is now", x0)

#And a few more steps...

if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1

if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1

if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1

if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
    
if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1

if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1

print("Three steps later x0 is", x0)
print("Three steps later y0 is", y0)


#Introducing x1 and y1

y1 = random.randint(0,99)
x1 = random.randint(0,99)

print("y1 is", y1)
print("x1 is", x1)


if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1

if random.random() < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
    
print("After our first step x1 is now", x1)
print("After our first step y1 is now", y1)

if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1

if random.random() < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1

if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1

if random.random() < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
    
if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1

if random.random() < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1

print("Three steps later x1 is", x1)
print("Three steps later y1 is", y1)

#Working out the distance between x0,y0 and x1,y1

distance = math.sqrt( ((x1 - x0)**2) + ((y1-y0)**2))

print ("The distance between our two points is", distance, "units")