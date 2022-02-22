# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 01:16:48 2021

@author: Egecan
"""


import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations
from itertools import combinations




def calculateV(mylist):
    length=len(mylist)
    V=0
    for (index,element) in enumerate(mylist):
        if index==0:
            V+=1
            # print(index,V,"Index is 0")
            continue
        if element>max(mylist[:index]):
            V+=index+1
            # print(index,V,"Element largest.")
            continue
        else:
            V+=1
            # print(index,V,"Else.")
    return (V)


# l = list(set(permutations(np.arange(1,11))))
# l = list(set(permutations([1,1,3,4])))
# length=len(l)
# vsum=0
# for config in l:
#     vsum+=calculateV(config)
    
# print(vsum/length)