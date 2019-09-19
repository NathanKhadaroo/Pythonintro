# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:12:33 2019

@author: gynjkm
"""

#importing packages and telling python to use TkAgg

import matplotlib

matplotlib.use('TkAgg')

from bs4 import BeautifulSoup
import tkinter
import requests
import matplotlib.pyplot 
import matplotlib.animation
import math
import agentframework
import csv
import random


#requesting web data

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')

content = r.text

soup = BeautifulSoup(content, 'html.parser')





td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

#testing to see if beautifullsoup has got the right data
print(td_ys)

the_ys = []

the_ys.append(td_ys)

print(td_xs)

the_xs = []

the_xs.append(td_xs)

#print(content)  #testing to see if content had been pulled 

#defining our arguments

num_of_agents = 10

#

num_of_iterations = 100

neighbourhood = 20

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
  
fig = matplotlib.pyplot.figure(figsize=(12, 12))
    
def update(frame_number):
    
    fig.clear()   
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.xlim(0, agents[0].environment_width)
    matplotlib.pyplot.ylim(0, agents[0].environment_height)

    random.shuffle(agents)

    for agent in agents:
        agent.move()
        agent.eat()
        agent.share_with_neighbours(neighbourhood)
        
   
    
    for agent in agents:
        matplotlib.pyplot.scatter(agent.x,agent.y)

    
    
for j in range(num_of_iterations):
    random.shuffle(agents)
    
    for i in range (num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
    
#Showing our agents on a plot

matplotlib.pyplot.ylim(0, 299)
matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.imshow(environment)

for i in range (num_of_agents):

    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
    canvas.show()

menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)





tkinter.mainloop()
 

