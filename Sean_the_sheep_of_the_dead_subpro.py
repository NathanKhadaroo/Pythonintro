# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:12:33 2019

@author: gynjkm
"""

#importing packages and creating list


import matplotlib.pyplot as plt
import matplotlib.animation
import agentframework_zombies
import csv
import random
import sys

#defining our arguments and creating the lists of sheep and zombiesheep


Sean_the_sheep_of_the_dead_subpro = sys.argv[0]

num_of_agents = int(sys.argv[1])

num_of_iterations = int(sys.argv[2])

neighbourhood = int(sys.argv[3])

num_of_zombsheep = int(sys.argv[4])

agents = []   

zombsheep = []

#creating the environment from the csv file


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
plt.imshow(environment)
plt.show()
"""

#Assign starting points to all our agents in their environment

for i in range (num_of_agents):
    agents.append(agentframework_zombies.Agent(environment, agents))

for i in range (num_of_zombsheep):
    zombsheep.append(agentframework_zombies.Zombiesheep(environment, zombsheep, agents))
    
    
#First we randomise the order of agents acting for every iteration, then we move
#them, make them eat, and share food with their neighbours   
  
fig = plt.figure(figsize=(12, 12))
 
 #Testing to see if our agents have acces to the locations of other agents
"""
print("Our first agent is at", agents[0].x, agents[0].y, ", some other agents he's heard of are at:")

for i in range(10):
    print(agents[0].agents[i].x, agents[0].agents[i].y)
"""  
def update(frame_number):
    
    fig.clear()   
    plt.imshow(environment)
    plt.xlim(0, agents[0].environment_width)
    plt.ylim(0, agents[0].environment_height)
    plt.xlim(0, zombsheep[0].environment_width)
    plt.ylim(0, zombsheep[0].environment_height)

    random.shuffle(agents)
    random.shuffle(zombsheep)

    for agent in agents:
        agent.move()
        agent.eat()
        agent.share_with_neighbours(neighbourhood)
    
    for zombiesheep in zombsheep:
        zombiesheep.move()
        target_agents = zombiesheep.bite(neighbourhood, agents, zombsheep) #creates a list of all sheep within "biting range"
        

        
        for target in target_agents:
            # adds a new zombie in place of the target's location
            zombsheep.append(agentframework_zombies.Zombiesheep(environment, zombsheep, agents, [target.y, target.x]))
            # kills the target
            agents.remove(target)
            #this is done in this order to avoid losing the coordinates of the target

#plots our sheep in white and our zombies in red
    for agent in agents:
        plt.scatter(agent.x,agent.y, c="snow")
    
    for zombiesheep in zombsheep:
        plt.scatter(zombiesheep.x,zombiesheep.y, c="red")
         
#Showing our agents in animation 

plt.ylim(0, 299)
plt.xlim(0, 299)
plt.imshow(environment)

for i in range (num_of_agents):

    plt.scatter(agents[i].x,agents[i].y)


animation = matplotlib.animation.FuncAnimation(fig, update, interval=0.1, repeat=False, frames=num_of_iterations)

plt.show()

print(len(agents))
