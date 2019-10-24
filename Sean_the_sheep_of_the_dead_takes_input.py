# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:12:33 2019

@author: gynjkm
"""

#imports required packages

import sys
import matplotlib.pyplot as plt
import matplotlib.animation
import agentframework_zombies
import csv
import random

#defines our arguments and creating the lists of sheep and zombiesheep

num_of_agents = int(sys.argv[1])

num_of_iterations = int(sys.argv[2])

neighbourhood = int(sys.argv[3])

num_of_zombsheep = int(sys.argv[4])

num_of_landmines = int(sys.argv[5])

blast_radius = int(sys.argv[6])

agents = []   

zombsheep = []

holylandmines = []

#creates the environment from the csv file
environment = []

with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)

#Tests whether the environment has read in properly
"""
plt.imshow(environment)
plt.show()
"""

#Assign starting points to all our agents in their environment

for i in range (num_of_agents):
    agents.append(agentframework_zombies.Agent(environment, agents))

for i in range (num_of_zombsheep):
    zombsheep.append(agentframework_zombies.Zombiesheep(environment, zombsheep, agents))
    
for i in range (num_of_landmines):
    holylandmines.append(agentframework_zombies.Holy_landmine_of_Antioch(environment, zombsheep))
    

  
fig = plt.figure(figsize=(12, 12))
 
 
'''
#Testing to see if our agents have acces to the locations of other agents
print("Our first sheep is at", agents[0].x, agents[0].y, ", some other sheep he knows are at:")

for i in range(10):
    print(agents[0].agents[i].x, agents[0].agents[i].y)
'''  

'''
This makes the model run until the zombies have wiped out all ofthe sheep or 
the desired number of iterations has been reached.  
'''
def update(frame_number):
    
    fig.clear()   
    plt.imshow(environment)
    plt.xlim(0, agents[0].environment_width)
    plt.ylim(0, agents[0].environment_height)
    plt.xlim(0, zombsheep[0].environment_width)
    plt.ylim(0, zombsheep[0].environment_height)
    if len(holylandmines) == 0:
        pass
    else:
        plt.xlim(0, holylandmines[0].environment_width)
        plt.ylim(0, holylandmines[0].environment_height)

#shuffles the order in which agents in a list move to avoid "first mover" advantages
    random.shuffle(agents)
    random.shuffle(zombsheep)
    random.shuffle(holylandmines)

    for agent in agents:
        agent.move()
        agent.eat()
        agent.share_with_neighbours(neighbourhood)
    
    for zombiesheep in zombsheep:
        zombiesheep.move()
#creates a list of all sheep within "biting range"
        target_agents = zombiesheep.bite(neighbourhood, agents, zombsheep)

        
        for target in target_agents:
#adds a new zombie in place of the target's location
            zombsheep.append(agentframework_zombies.Zombiesheep(environment, zombsheep, agents, [target.y, target.x]))
#kills the target
            agents.remove(target)
#this is done in this order to avoid losing the coordinates of the target

    if len(holylandmines) == 0:
        pass
    else:
        for Holy_landmine_of_Antioch in holylandmines:
                ded_zombies = Holy_landmine_of_Antioch.detonate(blast_radius, zombsheep)
                if len(ded_zombies)> 0:
                        for ded_zombie in ded_zombies:
                            zombsheep.remove(ded_zombie)
                        holylandmines.remove(Holy_landmine_of_Antioch)
#plots our sheep in white and our zombies in red and our landmines in gold
    for agent in agents:
        plt.scatter(agent.x, agent.y, c="snow")
    
    for zombiesheep in zombsheep:
        plt.scatter(zombiesheep.x, zombiesheep.y, c="red")
        
    if len(holylandmines) == 0:
        pass
    else:
        for Holy_landmine_of_Antioch in holylandmines:
            plt.scatter(Holy_landmine_of_Antioch.x, Holy_landmine_of_Antioch.y, c="gold")
   
    print(frame_number)
   
#Prints an update on how the sheep vs zombie battle is going
   
    print("There are", str(len(agents)), "sheep, ", str(len(zombsheep)), "zombie sheep, and", str(len(holylandmines)), "landmines remaining.") 

#prints a victory message for the zombies if they manage to convert all the sheep
    if len(agents) == 0:
        print("Braiiiiins! Zombies win!")
        
#prints a victory message for the sheep if they manage to survive until dawn or all zombies die
    if int(frame_number) == int(num_of_iterations)-1:
        print("Baaaahhhh! Sheep win!")
    if len(zombsheep) == 0:
        print("Baaaahhhh! Sheep win!")

#Showing our agents in animation 

plt.ylim(0, 299)
plt.xlim(0, 299)
plt.imshow(environment)

#for i in range (num_of_agents):

   # plt.scatter(agents[i].x,agents[i].y)


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)

plt.show()

   