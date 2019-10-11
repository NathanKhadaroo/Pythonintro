# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:37:12 2019

@author: gynjkm
"""
import random
import math

class Agent():
    
        
    def __init__ (self, environment, agents):
         
         self.environment = environment
         self.environment_height = len(environment)
         self.environment_width = len(environment)
         self.x = random.randint(0, self.environment_width-1)
         self.y = random.randint(0, self.environment_height-1)         
         self.store = 0 
         self.agents = agents
        
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
        
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
              #  print("Shared with agent " + str(distance) + " units away, now they both have" + str(average_store))
               
class Zombiesheep():
    def __init__(self, environment, zombsheep, agents, spawn_coordinates = None):
        self.environment = environment
        self.environment_height = len(environment)
        self.environment_width = len(environment)
        self.agents = agents
        
        # setting location of new zombie
        if spawn_coordinates is None:
            self.x = random.randint(0, self.environment_width-1)
            self.y = random.randint(0, self.environment_height-1)
        else:
            self.x = spawn_coordinates[1]
            self.y = spawn_coordinates[0]

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
    
    def bite(self, neighbourhood, agents, zombsheep):
        list_agent = []
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                list_agent.append(agent)
        return list_agent
    
    
        