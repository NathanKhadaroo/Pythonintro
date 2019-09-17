# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:12:33 2019

@author: gynjkm
"""

#importing packages and creating list

import matplotlib.pyplot
import math
import agentframework


#Working out the distance between two agents

def distance_between(agents_row_a, agents_row_b):
                
            return math.sqrt( ((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y-agents_row_b.y)**2))
        
agents = []

num_of_agents = 10

num_of_iterations = 100


        
#Creating a loop to assign starting points to all our agents

for i in range (num_of_agents):
    agents.append(agentframework.Agent())
    
#Creating a loop to randomise the  coordinateds of all our agents two steps
#Stopping our agents falling off the edge by making our space a donught
for j in range(num_of_iterations):
    
    for i in range (num_of_agents):
        agents[i].move

            

#Showing our agents on a plot

matplotlib.pyplot.ylim(0, 49)
matplotlib.pyplot.xlim(0, 49)

for i in range (num_of_agents):

    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

matplotlib.pyplot.show()

#Working out the distances between all agents

for j in range(num_of_agents):
    for i in range(num_of_agents):
    
        distance = distance_between(agents[i], agents[j])
        print(distance)
