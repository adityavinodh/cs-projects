# testscript.py
"""
Demonstration and tests for Project 5 classes
"""

from interval import Interval
from item import Item
from robot import Robot


## Test class Interval
in1= Interval(3,9)  # Instantiate an Interval with endpoints 3 and 9
print(in1)
print(in1.left)     # Should be 3. The attributes are "public," so it is possible
                    #  to access the attribute left directly.
in2= Interval()     # Instantiate an Interval with default end points
print(in2)
o= in1.overlap(Interval(5,15))
                    # o references an Interval with endpoints 5 and 9.
print(o)
print(f"{o.get_width()=}")  # Should be 4, the width of the Interval 
                            #   referenced by o


## Test class Item

#Testing valid_pickup
i1= Item(1,'basket', 2, 0, 3, [3,4])
#Should return true since maximum payload and arm_requirement can accommodate item i1 
print(f"{i1.valid_pickup(4,2)=}") 

#Should return false since payload is only 1 and weight of the object is 2
print(f"{i1.valid_pickup(1,0)=}")

i2= Item(1,'basket', 0, 0, 3, [3,4])
#Both should return true as this payload and arm_rquirement allow pick up of item i2 
print(f"{i2.valid_pickup(0,0)=}")
print(f"{i2.valid_pickup(1,0)=}")



#Testing update_pickup_status
j1 = Item(1,'basket', 2, 0, 3,[3,4])
j1.update_pickup_status(5)
print(f"{j1.picked_window.right=}")
print(f"{j1.picked_window.left=}")

j2 = Item(1,'basket', 2, 0, 0,[3,4])
j2.update_pickup_status(0)
print(f"{j2.picked_window.right=}")
print(f"{j2.picked_window.left=}")

j3 = Item(1,'basket', 2, 0, 4,[3,4])
j3.update_pickup_status(0)
print(f"{j3.picked_window.right=}")
print(f"{j3.picked_window.left=}")
print(f"{j3.weight=}")
print(f"{j3.arm_requirement=}")

#Testing draw method for item j1
j1.draw(7)


## Testing class Robot

#Initializing a Robot object:
Robot = Robot(5,5,(0,0),10)

#Testing attributes under the Robot class to see if the initialization method has worked
print(f"{Robot.total_time=}")
print(f"{Robot.starting_location=}")


#Testing the get_id method
print(f"{Robot.get_id()=}")

#Creating a new object i4
i4= Item(1,'ball', 2, 0, 3, loc = [3,4])



#Testing that get_items_picked is a copy 
print(f"{Robot.get_items_picked()=}")
test_picked = Robot.get_items_picked()
print(test_picked)

#Picking up item i4
print(f"{Robot.pick(i4, do_pick = True)=}")
updated_picked = Robot.get_items_picked()
print(updated_picked)
#Testing whether test_picked changes as new item is picked
print(test_picked)
#The empty test_picked list is unchanged - showing that it is indeed a copy

#Testing get_locations method after the Robot has picked up item i4
print(f"{Robot.get_locations()=}")

#Testing where_am_i to see if Robot's current location and time is correctly returned
print(f"{Robot.where_am_i()=}")

#Testing steps to item from current position
print(f"{Robot.steps_to_arrival([5,5])=}")

#Picking up new item at [5,5] - which is 3 steps and requires 4 further time steps to pick up
#Should return false
i5= Item(2,'pencil', 2, 0, 4, loc = [5,5])
print(f"{Robot.pick(i5, do_pick=True)=}")

#Changing pickup duration to 1
#Should still return False as it takes 3 steps to reach item - greater than total time of 10 minutes
i5= Item(2,'pencil', 2, 0, 1, loc = [5,5])
print(f"{Robot.pick(i5, do_pick=True)=}") 

#Now changing coordinates of item to only being 1 step away
#Should return True
i5= Item(2,'pencil', 2, 0, 1, loc = [3,5])
print(f"{Robot.pick(i5, do_pick=True)=}")

#Finally changing coordinates of item to being 2 steps away 
#Should return False as time would be past 10 time steps
i5= Item(2,'pen', 2, 0, 1, loc = [4,5])
print(f"{Robot.pick(i5, do_pick=True)=}")

#Finding recent location of robot after 2 pickups
#Should return (3,5) and 9 since only item 'pencil'  was able to be picked up
print(f"{Robot.where_am_i()=}")

Robot.draw(8)









