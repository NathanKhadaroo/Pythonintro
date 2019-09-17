# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:12:33 2019

@author: gynjkm
"""

#importing packages and creating list

import matplotlib.pyplot
import math
import agentframework
import csv

#Reading in data 


environment = []

with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)

 #Testing to see if the environment has read in properly
"""
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
"""


#Working out the distance between two agents

def distance_between(agents_row_a, agents_row_b):
                
            return math.sqrt( ((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y-agents_row_b.y)**2))
        
agents = []

num_of_agents = 10

num_of_iterations = 300


        
#Assign starting points to all our agents in their environment

for i in range (num_of_agents):
    agents.append(agentframework.Agent(environment))
    
#Creating a loop to randomise the  coordinateds of all our agents two steps
#Stopping our agents falling off the edge by making our space a donught
#Making our agents eat
for j in range(num_of_iterations):
    
    for i in range (num_of_agents):
        agents[i].move()
        agents[i].eat()
        

#Showing our agents on a plot

matplotlib.pyplot.ylim(0, 299)
matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.imshow(environment)

for i in range (num_of_agents):

    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

matplotlib.pyplot.show()

#Working out the distances between all agents

for j in range(num_of_agents):
    for i in range(num_of_agents):
    
        distance = distance_between(agents[i], agents[j])
     
