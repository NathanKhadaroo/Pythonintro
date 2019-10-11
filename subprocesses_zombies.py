# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:41:53 2019

@author: gynjkm
"""

import subprocess



a = [2, 5, 10, 20]


for i in range(len(a)):
    #print(a[i])
    s = 'python Sean_the_sheep_of_the_dead.py.py 100 100 15 {0}'.format(a[i])
    #print (s)
    sub = subprocess.run(s)
    print('returncode:', sub.returncode)
    print(str(sub.stdout))