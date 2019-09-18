# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:41:53 2019

@author: gynjkm
"""

from subprocess import run


a = [2, 5, 10, 20, 50, 100, 200, 500]

#a = [10, 100, 1000, 10000, 100000]

for i in range(len(a)):
    #print(a[i])
    s = 'python Communicating.py {0} 20 30'.format(a[i])
    print (s)
    run(s)
