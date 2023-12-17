#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:56:22 2023

@author: adityavinodh
"""

# testscript6.py
"""
Demonstration and tests for Project 6 
"""
from robot import Robot, FastRobot, LimbedRobot
from item import Item
from main6 import run_robots
import math

## Testing class Robot

#Initializing a Robot object:
Robot = Robot(5,5,(0,0),10)
#Initializing a FastRobot object:
fastr = FastRobot(2, 3, [0,0], 30, 3)

#Initializing a Limbed object:
limbedr = LimbedRobot(5, 4, [12,5], 30, 0.5, 3, 1)

#Testing whether FastRobot steps_to_arrival works:
fastr.steps_to_arrival([4,0])

fastr_2 = FastRobot(2, 3, [0,0],30, math.sqrt(2))
fastr_2.steps_to_arrival([2,2])

fastr_3 =  FastRobot(2, 3, [0,0], 30, 6)
fastr_3.steps_to_arrival([3,4])

    
#Testing whether run_robots works:
robots, items = run_robots("room2.txt")
robots2, items2 = run_robots("room3.txt")

#Testing whether LimbedRobot steps_to_arrival works:
limbedr1 = robots[4]
limbedr2= robots [5]
item1 = items[0]
item2 = items[1]

limbedr1.steps_to_arrival(item1.loc)
limbedr2.steps_to_arrival(item2.loc)




