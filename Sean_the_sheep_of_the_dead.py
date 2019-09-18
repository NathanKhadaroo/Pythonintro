# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:12:33 2019

@author: gynjkm
"""

#importing packages and creating list

import matplotlib.pyplot 
import matplotlib.animation
import math
import agentframework_zombies
import csv
import random


#defining our arguments

num_of_agents = 100

num_of_iterations = 100

neighbourhood = 40

num_of_zombsheep = 1

agents = []   

zombsheep = []

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
    agents.append(agentframework_zombies.Agent(environment, agents))

for i in range (num_of_zombsheep):
    zombsheep.append(agentframework_zombies.Zombiesheep(environment, zombsheep, agents))
    
    
#First we randomise the order of agents acting for every iteration, then we move
#them, make them eat, and share food with their neighbours   
  
fig = matplotlib.pyplot.figure(figsize=(12, 12))
    
def update(frame_number):
    
    fig.clear()   
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.xlim(0, agents[0].environment_width)
    matplotlib.pyplot.ylim(0, agents[0].environment_height)
    matplotlib.pyplot.xlim(0, zombsheep[0].environment_width)
    matplotlib.pyplot.ylim(0, zombsheep[0].environment_height)

    random.shuffle(agents)
    random.shuffle(zombsheep)

    for agent in agents:
        agent.move()
        agent.eat()
        agent.share_with_neighbours(neighbourhood)
    
    for zombiesheep in zombsheep:
        zombiesheep.move()
        zombiesheep.bite(neighbourhood, agents, zombsheep)
   
    
    for agent in agents:
        matplotlib.pyplot.scatter(agent.x,agent.y, c="green")
    
    for zombiesheep in zombsheep:
        matplotlib.pyplot.scatter(zombiesheep.x,zombiesheep.y, c="red")
         

    
"""    
for j in range(num_of_iterations):
    random.shuffle(agents)
    
    for i in range (num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
"""        
        
#Testing to see if our agents have acces to the locations of other agents
"""
print("Our first agent is at", agents[0].x, agents[0].y, ", some other agents he's heard of are at:")

for i in range(10):
    print(agents[0].agents[i].x, agents[0].agents[i].y)
"""
#Showing our agents on a plot

matplotlib.pyplot.ylim(0, 299)
matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.imshow(environment)

for i in range (num_of_agents):

    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)


animation = matplotlib.animation.FuncAnimation(fig, update, interval=0.1,repeat=False, frames=num_of_iterations)

matplotlib.pyplot.show()

#Working out the distances between all agents
"""
for j in range(num_of_agents):
    for i in range(num_of_agents):
    
        distance = distance_between(agents[i], agents[j])
"""     
