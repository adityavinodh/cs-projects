# main.py
"""
Module for Project 5 Robot Task Allocation

To to see the animation, in the Spyder Python Console, type
    %matplotlib qt
to send the graphics to the qt graphical user interface.  You only need to do
this once in a session (unless you restart the kernel).
"""

from robot import Robot
from item import Item
import numpy as np
import matplotlib.pyplot as plt


def run_robots(data_filename):
    """
    Create an allocation of robots to pickup items given a data file in the
    necessary format.
    :param data_filename:
    """
    with open('room1.txt', 'r') as fid:
        # Process the first line of the file
        line = fid.readline()  
        sim_info = line.strip().split(',')
        sim_time = int(sim_info[0])
        horiz_dim = float(sim_info[1])
        vert_dim = float(sim_info[2])
        room_size = np.array([horiz_dim, vert_dim])
        
        robots = []  # list of robots
        items = []   # list of items
        
        for line in fid:

            if line[0] == 'R':
                tokens = line.strip().split(', ')
                splitr = tokens[3].split(',')
                left = int(splitr[0][1:])
                right = int(splitr[1][:-1])
                r = Robot(int(tokens[1]), int(tokens[2]), [left,right], int(sim_time))
                robots.append(r)
            
                
            if line[0] == 'I':
                tokens = line.strip().split(", ")
                spliti = tokens[5].split(',')
                left = int(spliti[0][1:])
                right = int(spliti[1][:-1])
                i = Item(int(tokens[1]), tokens[2], float(tokens[3]), int(tokens[4]), int(tokens[6]),[left,right])
                items.append(i)
                
        return robots, items, sim_time,room_size, line, sim_info, horiz_dim, vert_dim
    

    # OPTIONAL TODO: check for collisions
    #   Uncomment the check_collisions call below if you have implemented
    #   this OPTIONAL function
    #
    # collisions = check_collisions(allocated_robots)
    


def simple_allocation(robots, items):
    """
    Given a list of items and a list of robots, allocate item pickups to the robots.
        
    Parameters
    ----------
    robots : list
        non-empty list of unique `Robot` references
    items : list
        non-empty list of unique `Item` references

    Algorithm: for each `Item` in `items`, look for the first `Robot` in 
        `robots` that is capable of picking it up to pick it up.

    Returns
    -------
    lisR : list
        list of the `Robot`s that picked up `Item`s
    lisI : list
        list of remaining `Item`s that didn't get picked up
    """
    # TODO TASK 2: implement this function

    lisR = []
    lisI = []
    for i in items:
        picked = False
        
        for r in robots:
            if r.pick(i) == True:
                lisR.append(r)
                picked = True

                
        if picked == False:
            lisI.append(i)


    return (lisR,lisI)

def animate(robots, items, sim_time, room_size):
    """
    Animate the robots and items in space for `sim_time` timesteps.  At each
    time step, call the `draw` method for each `Item` and for each `Robot`. 
    
    Assume that the bottom left corner is at (0,0) for room_size

    Parameters
    ----------
    robots : list
        list of `Robot` references
    items : list
        list of `Item` references
    sim_time : int
        number of timesteps
    roomsize : list
        length 2 list that represents the dimensions of the room
    """
    plt.close('all')
    plt.pause(1)
              
    for t in range(1,sim_time+1):
        
        plt.clf()  # clear figure
        plt.axis('equal')
        plt.axis('off')
        plt.axis([0, room_size[0] + 1, 0, room_size[1] + 1])
        plt.autoscale(False)
        plt.title(f"Time = {t}")
        
        for r in robots:
            if len(r._locations)>=t>=1:
                r.draw(t)
            else:
                r.draw(len(r._locations))
        
        for i in items:
            i.draw(t)
            
        plt.pause(0.75)
        

def output_results(robots):
    """
    Prints the results of task allocation. Show the stats and tasks for each 
    `Robot` in `robots`:
        - Print the number of `Item`s picked and the total timesteps taken
        - Print out each `Item` picked and the time period taken to navigate 
          to the object and pick it.
    See the print format in the project description.
    
    Parameter robots: (list) Each element is a `Robot` in the simulation.

    """
    
    for r in robots:
        list_i = r.get_items_picked()
        max_time = 0
        for i in list_i:
            if i.duration+len(r.steps_to_arrival(i.loc)) > max_time:
                max_time = i.duration+len(r.steps_to_arrival(i.loc))
                last_i = i
        picked_no = len(r.get_items_picked())
        print(f'Robot {r._id_} picked {picked_no} items in {last_i.duration+len(r.steps_to_arrival(last_i.loc))} timesteps')
        
        for i in (r._items_picked):
            if i in simple_allocation(robots, r.get_items_picked())[1]:
                print()
            else:
                print(f' {i.name} (ID {i.id_}): Assigned at time {len(r.steps_to_arrival(i.loc))}, picked up at time {i.duration+len(r.steps_to_arrival(i.loc))}')



def check_collisions(allocated_robots):
    """
    Check for and report on collisions.
    
    OPTIONAL TO DO: write the specifications for this function

    Parameter allocated_robots: (list) Each element is a `Robot` that has been
        allocated at least one task

    """
    # OPTIONAL TO DO: implement this function
    pass






#if__name__ == '__main__':
    
   # robots, items, sim_time,room_size = run_robots("room1.txt")[0],run_robots("room1.txt")[1],run_robots("room1.txt")[2],run_robots("room1.txt")[3]
    
    #allocated_robots, items_remaining = simple_allocation(robots, items)
    
    #animate(robots, items, sim_time, room_size)

    #output_results(robots)
