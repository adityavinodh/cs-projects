#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 21:55:44 2023

@author: adityavinodh
"""
import math 

#Soliciting user inputs with validation 
h_final = float(input('Enter a positive goal height in feet: '))
while h_final<0:
    h_final = float(input('Enter a positive goal height in feet: '))
    
b = float(input('Enter a positive burn time in seconds: '))
while b<0:
    b = float(input('Enter a positive burn time in seconds: '))

#Given constants
u = 8000
g = 32.2
mR = 100
q = 1

#Initializing variables
t = 0.1
h_b = 0

#Calculating mass of rocket with fuel
mo = mR+q*b

#Calculating peak height to check if goal height is achievable 
h_b = (u/q)*(mo-q*b)*math.log(mo-q*b)+u*(math.log(mo)+1)*b-(g*b**2)/2 - (math.log(mo)*u*mo)/q
v_b = u*(math.log(mo/(mo-q*b)))-g*b
v_t = 0
h_p = h_b+((v_b)**2)/(2*g)

#Additional equations
t_p = b + v_b/g
t_f = t_p + (2*h_p/g)**0.5


#Condition that checks if goal height is achievable
if h_p>=h_final:
    
    #Calculating height, velocity during burn time (h denoted by h_b)
    while h_b<h_final and t<b:
            v_b = u*(math.log(mo/(mo-q*t)))-g*t
            h_b =(u/q)*(mo-q*t)*math.log(mo-q*t)+u*(math.log(mo)+1)*t-((g*t**2)/2) - (math.log(mo)*u*mo)/q
            t = t+0.1
    h_t = h_b
    
    #Calculating height, velocity once fuel is used up (h_t gets h_b)
    while h_t<h_final and t>=b:
            v_t = v_b - g*(t-b)
            h_t = h_b + v_b * (t-b)-(g*(t-b)**2)/2
            t = t+0.1
            
#Output message if the goal height is not achievable
else:
    print('Goal height is not achievable')
        
#Re-assigning the final height reached and time taken using prior variables
h_reached = h_t
t_taken = t

print (f'The time taken to reach a goal height of {h_final} with a burn time of {b} is {t_taken:.1f}')





        
        


