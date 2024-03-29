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
import random
import sys

#defining our arguments and allowing them to be read in via command line


#Communicating = sys.argv[0]
#print(Communicating)
print("hi")

try:
    print("Setting parameters")
    num_of_agents = int(sys.argv[1])

    num_of_iterations = int(sys.argv[2])

    neighbourhood = int(sys.argv[3])

except:
    print("Skipped setting parameters")
    pass


agents = []   
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
        

#Assign starting points to all our agents in their environment

for i in range (num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    
#First we randomise the order of agents acting for every iteration, then we move
#them, make them eat, and share food with their neighbours     
    
    
for j in range(num_of_iterations):
    random.shuffle(agents)
    
    for i in range (num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
        
#Testing to see if our agents have acces to the locations of other agents
print("Our first agent is at", agents[0].x, agents[0].y, ", some other agents he's heard of are at:")

for i in range(10):
    print(agents[0].agents[i].x, agents[0].agents[i].y)

#Showing our agents on a plot

matplotlib.pyplot.ylim(0, 299)
matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.imshow(environment)

for i in range (num_of_agents):

    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

#matplotlib.pyplot.savefig('./{0}.png'.format(num_of_agents))

matplotlib.pyplot.show()

#Working out the distances between all agents

for j in range(num_of_agents):
    for i in range(num_of_agents):
    
        distance = distance_between(agents[i], agents[j])
