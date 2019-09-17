# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:37:12 2019

@author: gynjkm
"""
import random
import math

class Agent():
    
        
    def __init__ (self, environment, agents):
         self.x = random.randint(0,299)
         self.y = random.randint(0,299)
         self.environment = environment
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
        
    def eat(self): # can you make it eat what is left?
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
                print("Shared " + str(distance) + " " + str(average_store))
               
        