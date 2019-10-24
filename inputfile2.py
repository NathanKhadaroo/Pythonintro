# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:41:15 2019

@author: msra2nk3
"""
def safe_input(question):
   
    x = input(question)
    while not (x.isdigit()) and not (x == 0):
            print("This must be a positive integer!")
            x = input(question)
    
    return x

    
a = safe_input("How many sheep should there be?" )

b = safe_input("For how many iterations should the model run?")

c = safe_input("How large should the neighborhoods be?")

d = safe_input("How many Zombie sheep should there be?")

e = safe_input("How many landmines should there be?")

f = safe_input("How large should the landmines blast radius be?")

arguments =  "%s %s %s %s %s %s" % (a, b, c, d, e, f)

#print (arguments)

runfile("Sean_the_sheep_of_the_dead_takes_input.py", args = arguments)
