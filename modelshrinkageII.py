# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:12:33 2019

@author: gynjkm
"""

#importing packages and creating list

import random
import matplotlib.pyplot
import math
import time

agents = []

num_of_agents = 100

num_of_iterations = 100

#Creating a loop to assign starting points to all our agents

for i in range (num_of_agents):
    agents.append([random.randint(0,49), random.randint(0,49)])
    
#Creating a loop to randomise the  coordinateds of all our agents two steps
#Stopping our agents falling off the edge by making our space a donught
for j in range(num_of_iterations):
    
    for i in range (num_of_agents):
        
        if random.random() < 0.5:
        
            agents[i][0] = (agents[i][0] + 1) % 50
    
        else:
            agents[i][0] = (agents[i][0] - 1) % 50         
            
    
    for i in range (num_of_agents):
            
        if random.random() < 0.5:
        
            agents[i][1] = (agents[i][1] + 1) % 50
    
        else:
            agents[i][1] = (agents[i][1] - 1) % 50
            
#Working out the distance between two agents
def distance_between(agents_row_a, agents_row_b):
                
            return math.sqrt( ((agents_row_a[1] - agents_row_b[1])**2) + ((agents_row_a[0]-agents_row_b[0])**2))
            

#Showing our agents on a plot

matplotlib.pyplot.ylim(0, 49)
matplotlib.pyplot.xlim(0, 49)

for i in range (num_of_agents):

    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

matplotlib.pyplot.show()

#Working out the distances between all agents and timing it

start = time.perf_counter()

for j in range(num_of_agents):
    for i in range(num_of_agents):
    
        distance = distance_between(agents[i], agents[j])
        print(distance)

end = time.perf_counter()

print("time = " + str(end - start))