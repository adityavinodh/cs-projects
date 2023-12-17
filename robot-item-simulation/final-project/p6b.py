#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 22:01:39 2023

@author: adityavinodh
"""

import random
import math


def select_r ( lis , k ):
    """
    Returns ( int or float ) the kth smallest value in list lis , selected by
    using a RANDOM splitter , using RECURSION .
    Parameters
    lis : a non - empty list or array of numbers
    k : an int in [0.. n -1] where n is the length of lis
    """
    i = random.randint(0,len(lis)-1)
    little_vals = []
    big_vals = []
    splitter = lis[i]
    
    for v in range(len(lis)):
        if lis[v] < splitter:
            little_vals.append(lis[v])
        elif lis[v]>splitter:
            big_vals.append(lis[v])
        else:
            if v != k:
                big_vals.append(lis[v])
                
    if k<len(little_vals):
        val = select_r(little_vals, k)
    elif k == len(little_vals):
        val= lis[i]
    else:
        
        val = select_r(big_vals, k-len(little_vals)-1)
        
    return val
def my_median ( lis ):
    """
    Returns ( int or float ) the median of list lis
    Parameter lis : a non - empty list or array of numbers
    Makes effective use of select_r .
    Does not use predefined functions median or sort .
    """
    
    if len(lis) % 2 == 1:
        m = int(len(lis)/2)
        median = select_r(lis,m)
    if len(lis)%2 == 0:
        m = int(len(lis)/2)
        median_high = select_r(lis,m+1)    
        median_low = select_r(lis, m)
        median = (median_high+median_low)/2

    return median

def select_m ( lis , k ):
    """
    Returns ( int of float ) the kth smallest value in list lis , selected by
    using a MIDDLE splitter , using RECURSION . If lis has an even length ,
    define middle as int ( len ( lis )/2).
    Parameters
    lis : a non - empty list or array of numbers
    k : an int in [0.. n -1] where n is the length of lis
    """
    
    splitter_id = int(len(lis)/2)
    splitter = lis[splitter_id]
    little_vals = []
    big_vals = []
    
    for v in range(len(lis)):
        if lis[v] < splitter:
            little_vals.append(lis[v])
        elif lis[v]>splitter:
            big_vals.append(lis[v])
        else:
            if v != k:
                big_vals.append(lis[v])
                
    if k<len(little_vals):
        val = select_m(little_vals, k)
    elif k == len(little_vals):
        val= lis[splitter_id]
    else:
        
        val = select_m(big_vals, k-len(little_vals)-1)
        
    return val


def my_median2 ( lis ):
    """
    Returns ( int or float ) the median of list lis
    Parameter lis : a non - empty list or array of numbers
    Makes effective use of select_r .
    Does not use predefined functions median or sort .
    """
    
    if len(lis) % 2 == 1:
        m = int(len(lis)/2)
        median = select_m(lis,m+1)
    if len(lis)%2 == 0:
        m = int(len(lis)/2)
        median_high = select_m(lis,m+1)
        median_low = select_m(lis, (m))
        median = (median_high+median_low)/2

    return median
    
        

            
        
        
            

        