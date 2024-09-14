#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 05:44:42 2023

@author: adityavinodh
"""

from random import uniform
import matplotlib.pyplot as plt 

n= 10000
r = 1
r2 = 2.5
# Set up figure window
plt.figure()            # creates a new figure window
ax= plt.gca()           # gets current axes
ax.set_aspect('equal')  # unit lengths on x- and y-axis are equal (equal scaling)
plt.axis((-r2, r2, -r2, r2))  # x-axis limits -r to r; y-axis limits -r to r.                                       # y-axis limits -s_half to s_half
                          # dart board is centered over the origin
                          
# Simulate dart throwing
y_hits= 0
r_hits=0
b_hits=0   # no. of darts in circle so far
for k in range(n):
    # Throw kth dart
    x= uniform(-r2, r2)
    y= uniform(-r2, r2)
    
    # Is dart in the circle?
    if ((x**2 + y**2) - 1)**3 <= (x**2*y**3):
        y_hits= y_hits + 1
        plt.plot(x, y, 'y.')
    elif ((x**2 + y**2) - 3)**3 <= (x**2*y**3):
        plt.plot(x, y, 'r.')
        r_hits=r_hits+1
    else:
        plt.plot(x, y, 'c.')
        b_hits=b_hits+1
        
#Calculating the area of the inner heart
heart_area_inner = (6.55*y_hits/r_hits)
#Calculating the area of the outer heart
heart_area_diff =  abs(heart_area_inner-6.55)

#Printing the difference in areas as the plot's title
plt.title(f'The difference in areas between the 2 hearts is {heart_area_diff:.4f}')
