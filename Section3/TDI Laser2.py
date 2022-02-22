# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 22:37:39 2021

@author: Egecan
"""

import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations
from itertools import combinations

l=[]
l = list(set(permutations(np.arange(1,5))))
# l = list(set(permutations([1,1,3,4])))
def calculateV(mylist):
    length=len(mylist)
    V=0
    for (index,element) in enumerate(mylist):
        for j in range(index+1):
            if index-j==0:
                V+=1
                break
            if mylist[index]>mylist[index-j-1]:
                V+=1
                continue
            else:
                V+=1
                break
    return (V)


V_list=[]
for mylist in l:

    V_list.append(calculateV(mylist))

V_array=np.asfarray(V_list)
sumV=0
for mylist in l:

    sumV+=(calculateV(mylist))
V_array=np.sort(V_array)
print(sumV/len(l))
print(np.mean(V_array))
print(np.std(V_array))

