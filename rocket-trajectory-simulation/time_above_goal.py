#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 21:06:17 2023

@author: adityavinodh

"""
import math 
import matplotlib.pyplot as plt

#Soliciting user inputs with validation 
h_input = float(input('Enter a positive goal height in feet: '))

while h_input<0:
    h_input = float(input('Enter a positive goal height in feet: '))

#Calculating duration values for burn times from 1-100 (inclusive)    
for b in range(1,101):
        
        #Given constants
        u = 8000
        g = 32.2
        mR = 100
        q = 1
    
        #Initializing variables
        t = 0.1
        t_start = 0
        t_final = 0
        h_b = 0
        v_b = 0
        v_t = 0
    
        #Calculating mass of rocket with fuel
        mo = mR+q*b
    
        #Calculating peak height to check if goal height is achievable 
        h_b_check = (u/q)*(mo-q*b)*math.log(mo-q*b)+u*(math.log(mo)+1)*b-(g*b**2)/2 - (math.log(mo)*u*mo)/q
        v_b_check = u*(math.log(mo/(mo-q*b)))-g*b
        h_p = h_b_check+((v_b_check)**2)/(2*g)
        
        #Additional equations
        t_p = b + v_b/g
        t_f = t_p + (2*h_p/g)**0.5
    
        #Condition that checks if goal height is achievable
        if h_p>=h_input:
            
            #Calculating height, velocity during burn time (h denoted by h_b)
            while t<b and h_b<h_input:
                v_b = u*(math.log(mo/(mo-q*t)))-g*t
                h_b =(u/q)*(mo-q*t)*math.log(mo-q*t)+u*(math.log(mo)+1)*t-(g*t**2)/2 - (math.log(mo)*u*mo)/q
                t = t+0.1
            h_t = h_b
            
            #Accouting for the possibility that rocket has already reached goal height within burn time
            t_start = t
            
            #Calculating height, velocity before rocket reaches goal height
            if h_t<h_input:
                while t>=b and h_t<h_input:
                    v_t = v_b - g*(t-b)
                    h_t = h_b + v_b * (t-b)-(g*(t-b)**2)/2
                    t = t+0.1
                    
                t_start = t
                
                
                while t>=b and h_t>=h_input:
                    v_t = v_b - g*(t-b)
                    h_t = h_b + v_b * (t-b)-(g*(t-b)**2)/2
                    t = t+0.1
                    
                t_final = t
                
            
            #Calculating height, velocity of rocket above goal height    
            else:
                #Accounting for additional during burn time, as the rocket still has fuel remaining
                while t<b:
                    v_b = u*(math.log(mo/(mo-q*t)))-g*t
                    h_b =(u/q)*(mo-q*t)*math.log(mo-q*t)+u*(math.log(mo)+1)*t-(g*t**2)/2 - (math.log(mo)*u*mo)/q
                    t = t+0.1
                h_t = h_b
                
                #NCalculating final part of rocket's trajectory above goal height, once burn time is complete
                while h_t>=h_input:
                    v_t = v_b - g*(t-b)
                    h_t = h_b + v_b * (t-b)-(g*(t-b)**2)/2
                    t = t+0.1
                
            t_final = t
            
            #Calculating duration above goal height using start and final times
            duration = (t_final-t_start)
        #Output message if the goal height is not achievable
        else:
            duration = 0
        
        #Plotting the final graph for duration over burn time   
        plt.plot(b, duration , "r.")
        plt.xlabel('Burn time (seconds)')
        plt.ylabel('Duration (seconds)')
        plt.title(f'Duration above {h_input} feet')
plt.show()

#Answer: I found that using algorithm 2: directly exiting the while loop 
#        when the rocket's dropped back below the threshold, was a more efficient 
#        way of calculating the duration. This saved time in computing the heights and 
#        velocities of the rocket's trajectories below the input height,
#        presenting a direct method to extract the timestamp at which it 
#        entered this region and exited it.


        
        
