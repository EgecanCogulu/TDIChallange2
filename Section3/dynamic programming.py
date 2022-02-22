# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 03:49:13 2021

@author: Egecan
"""

import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations
from itertools import combinations
from math import factorial

def V(n,memo={}):
    if n==2:
        return 5
    else:
        if n in memo:
            return memo[n]
        else:
            result=factorial(n-1)V(n-1,memo)
            memo[n]=result
            return(result)
