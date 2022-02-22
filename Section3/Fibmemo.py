# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 03:12:31 2021

@author: Egecan
"""
def Fib(n):
    if n==0 or n==1:
        return(1)
    else:
        return(Fib(n-1)+Fib(n-2))


def memoFib(n,memo = {} ):
    if n==0 or n==1:
        return(1)
    else:
        if n in memo:
            return memo[n]
        else:
            result=memoFib(n-1,memo)+memoFib(n-2,memo)
            memo[n]=result
            return(result)

        