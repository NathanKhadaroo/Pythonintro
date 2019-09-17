# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:12:33 2019

@author: gynjkm
"""

#importing packages and creating list

import random
import math
import operator
import matplotlib.pyplot

agents = []

#Assinging starting point y, x of the first agent as agents[0][0],[0][1]

agents.append([random.randint(0,49), random.randint(0,49)])

#Building an algorithm to randomise the value of y0 one step

if random.random() < 0.5:
    agents[0][0] = agents[0][0] + 1
else:
    agents[0][0] = agents[0][0] - 1
    
#Building an algorithm to randomise the value of x0 one step

if random.random() < 0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1
    
#And a few more steps...

if random.random() < 0.5:
    agents[0][0] = agents[0][0] + 1
else:
    agents[0][0] = agents[0][0] - 1

if random.random() < 0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1

if random.random() < 0.5:
    agents[0][0] = agents[0][0] + 1
else:
    agents[0][0] = agents[0][0] - 1

if random.random() < 0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1
    
if random.random() < 0.5:
    agents[0][0] = agents[0][0] + 1
else:
    agents[0][0] = agents[0][0] - 1

if random.random() < 0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1

#Assinging starting point y, x of the second agent as agents[1][0],[1][1]

agents.append([random.randint(0,49),random.randint(0,49)])


if random.random() < 0.5:
    agents[1][0] = agents[1][0] + 1
else:
    agents[1][0] = agents[1][0] - 1

if random.random() < 0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1] - 1
    
if random.random() < 0.5:
    agents[1][0] = agents[1][0] + 1
else:
    agents[1][0] = agents[1][0] - 1

if random.random() < 0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1] - 1

if random.random() < 0.5:
    agents[1][0] = agents[1][0] + 1
else:
    agents[1][0] = agents[1][0] - 1

if random.random() < 0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1] - 1
    
if random.random() < 0.5:
    agents[1][0] = agents[1][0] + 1
else:
    agents[1][0] = agents[1][0] - 1

if random.random() < 0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1] - 1

#Working out the distance between x0,y0 and x1,y1

distance = math.sqrt( ((agents[1][1] - agents[0][1])**2) + ((agents[1][0]-agents[0][0])**2))

print ("The distance between our two points is", distance, "units")

print ("The coordinates of our agents (y, x) are", agents)

#Calculating the most easterly (eastmost?) and northerly agents

print ("The most northerly agent is at", max(agents))

print("The most easterly agent is at", max(agents, key=operator.itemgetter(1)))

#Showing our agents on a plot and colouring the most easterly point red

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
east_point= tuple(max(agents, key=operator.itemgetter(1)))
matplotlib.pyplot.scatter(east_point[1], east_point[0], color = 'red')
matplotlib.pyplot.show()

