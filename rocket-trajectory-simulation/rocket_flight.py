#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 06:08:36 2023

@author: adityavinodh
"""
import math 
import matplotlib.pyplot as plt
import numpy as np

def approx_flight(mR, q, b, u): 
    """
Return the tracjectory (time and altitude) of a rocket
Parameters
mR: (float or int) mass of rocket without fuel, in slugs q: (float or int) burn rate of fuel, in slugs/s
b: (float or int) burn time, seconds
2
u: (float or int) exhaust velocity, ft/s
Returns as a tuple
t: a list or array of numbers of at least 200 time values in seconds,
from 0 to tf, where tf is the flight time (from takeoff to landing) 
h: a list or array of altitude values in feet, corresponding to the list
(or array) of time values. """

    #Given constants
    g = 32.2

    #Initializing variables
    h_b = 0
    v_b = 0
    h_t = []
    time = np.arange(0,251)
    
    #Calculating mass of rocket with fuel
    mo = mR+q*b

    #Looping through all values of time 't'
    for t in time:
            
        #Calculating height, velocity during burn time (h denoted by h_b)
        if t<b: 
            v_b = u*(math.log(mo/(mo-q*t)))-g*t
            h_b =(u/q)*(mo-q*t)*math.log(mo-q*t)+u*(math.log(mo)+1)*t-(g*t**2)/2 - (math.log(mo)*u*mo)/q
            #Appending the height values to a list
            h_t.append(h_b)
            
        #Calculating height, velocity after burn time
        else:
            if (h_b + v_b * (t-b)-(g*(t-b)**2)/2)>=0:
                #Appending the height values to a list
                h_t.append((h_b + v_b * (t-b)-(g*(t-b)**2)/2))
                
            #Appending height values of NaN once the rocket falls to ground level
            else:
                 h_t.append(np.NaN)
                
    return (time, h_t) #Returning time, height values as a tuple  of 2 lists

           
# Given m_r, q, b, u

#Plotting the sensitivity analysis for 'u' values of 6000, 7000, 8000, and 8500
u = 6000
plt.figure(1)
(time1, h_t1)= approx_flight(100, 1, 80, 6000) 
legend_text = f'u = {u} ft/s' 
plt.plot(time1, h_t1, label=legend_text)

u = 7000
(time2, h_t2)= approx_flight(100, 1, 80, 7000) 
legend_text = f'u = {u} ft/s' 
plt.plot(time2, h_t2, label=legend_text)

u = 8000
(time3, h_t3)= approx_flight(100, 1, 80, 8000) 
legend_text = f'u = {u} ft/s' 
plt.plot(time3, h_t3, label=legend_text)
plt.legend()

u = 8500
(time4, h_t4)= approx_flight(100, 1, 80, 8500) 
legend_text = f'u = {u} ft/s' 
plt.plot(time4, h_t4, label=legend_text)
plt.legend()
plt.xlabel ('Time (seconds)')
plt.ylabel ('Height (feet)')
plt.title ('Sensitivity Analysis for Different Exhaust Velocities')

            
#Plotting the sensitivity analysis for burn times of 60, 70, 80, 90, and 100 s
plt.figure(2)
mR = 100
q = 1
u = 8000
for b in range(60,110,10):
    (time, h_t)= approx_flight(mR, q, b, u) 
    legend_text = f'b = {b} ft/s' 
    plt.plot(time, h_t, label=legend_text)
    plt.legend()
    plt.grid()
    plt.xlabel ('Time (seconds)')
    plt.ylabel ('Height (feet)')
    plt.title ('Sensitivity Analysis for Different Burn Times')

            

      
        
        