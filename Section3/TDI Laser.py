# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 22:37:39 2021

@author: Egecan
"""

import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations
from itertools import combinations
from scipy.optimize import curve_fit

def poly2(x,a,b,c,d,e,f,g):
    return (a*x**6+b*x**5+c*x**4+d*x**3+e*x**2+f*x+g)

def poly(x,a,b,c):
    return (a*x**2+b*x+c)

l=[]
l = list(set(permutations(np.arange(1,4+1))))
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


# V_list=[]
# for mylist in l:

#     V_list.append(calculateV(mylist))

# V_array=np.asfarray(V_list)
# sumV=0
# for mylist in l:

#     sumV+=(calculateV(mylist))

# print(sumV/len(l))
# print(np.mean(V_array))
# print(np.std(V_array))

x=np.arange(1,10)
y=[]
z=[]
for i in x:

    l = list(set(permutations(np.arange(1,i+1))))
    V_list=[]
    for mylist in l:
        V_list.append(calculateV(mylist))

    V_array=np.asfarray(V_list)
    y.append(np.mean(V_array))
    z.append(np.std(V_array))

popt, pcov=curve_fit(poly,x,y)

plt.figure()
plt.plot(x,y,"ro")
x=np.arange(1,21)    
plt.plot(x,poly(x,*popt))
