# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:37:12 2019

@author: gynjkm
"""
import random
import math

class Agent():
    
#Creates out sheep and gives them acces to the information they need for their behaiviour        

    def __init__ (self, environment, agents):
         
         self.environment = environment
         self.environment_height = len(environment)
         self.environment_width = len(environment)
         self.x = random.randint(0, self.environment_width-1)
         self.y = random.randint(0, self.environment_height-1)         
         self.store = 0 
         self.agents = agents

#allows our agents to move randomly two steps    
         
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300

#these functions calculate the (euclidian) distance beween agents,
#allows agents to eat their environment if they are "hungry", and share
#food with their nearby neigbors 
            
    def distance_between(self,a):
                
        return math.sqrt( ((self.x - a.x)**2) + ((self.y-a.y)**2))   
        
    def eat(self):
          if self.environment[self.y][self.x] > 10:
              self.environment[self.y][self.x] -= 10
              self.store += 10
        
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                average_store = (self.store + agent.store)/2
                self.store = average_store
                agent.store = average_store
        #print("Shared with agent " + str(distance) + " units away, now they both have" + str(average_store))

#Creates our zombies and gives them acces to the information they need                   
class Zombiesheep():

    def __init__(self, environment, zombsheep, agents, spawn_coordinates = None):
        self.environment = environment
        self.environment_height = len(environment)
        self.environment_width = len(environment)
        self.agents = agents
        
        #Sets the spawning location for our zombies, randomly for 'original zombies
        #and for newly converted zombies at the location where they were bitten
        
        if spawn_coordinates is None:
            self.x = random.randint(0, self.environment_width-1)
            self.y = random.randint(0, self.environment_height-1)
        else:
            self.x = spawn_coordinates[1]
            self.y = spawn_coordinates[0]
            
#move and distance between work the same as for our sheep (agents) 
#but faster (these are fast Zombieland style zombies, not slow Dawn 
# of the dead type zombies)
            
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 5) % 300
        else:
            self.y = (self.y - 5) % 300

        if random.random() < 0.5:
            self.x = (self.x + 5) % 300
        else:
            self.x = (self.x - 5) % 300
    
    def distance_between(self,a):
                
        return math.sqrt( ((self.x - a.x)**2) + ((self.y-a.y)**2)) 

#checks if a sheep is in the zombie's neighborhood, if there is it appends it a list
#and returns that list
        
    def bite(self, neighbourhood, agents, zombsheep):
        list_agent = []
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                list_agent.append(agent)
        return list_agent
    
#Adds anti zombie traps which detonate when zombies approach,
#showering the area with holy water, killing zombies but leaving sheep unaffected
class Holy_landmine():
    
    def __init__(self, environment, zombsheep):
        self.environment = environment
        self.environment_height = len(environment)
        self.environment_width = len(environment)
        self.x = random.randint(0, self.environment_width-1)
        self.y = random.randint(0, self.environment_height-1)
        self.zombsheep = zombsheep
        
    def distance_between(self,a):
                
        return math.sqrt( ((self.x - a.x)**2) + ((self.y-a.y)**2)) 
        
    def detonate(self, blast_radius, zombsheep):
        dead_zombies = []
        for zombiesheep in self.zombsheep:
            distance = self.distance_between(zombiesheep)
            if distance <= blast_radius:
                dead_zombies.append(zombiesheep)
        return dead_zombies
                
        
                
        