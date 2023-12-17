# game_of_life.py
"""
CS1112 Project 4 Game of Life

Refer to the Project 4 description for details and other helpful information.

To to see the animation, in the Spyder Python Console, type
    %matplotlib qt
to send the graphics to the qt graphical user interface.  You only need to do
this once in a session (unless you restart the kernel).

"""
import numpy as np
import matplotlib.pyplot as plt
import random


def create_world(nr, nc, data_mode):
    """
    Returns an nr-by-nc array of ints representing the game of life world
    
    Parameters
    ----------
    nr : the number of rows in the world.  An int > 5.
    
    nc : the number of columns in the world.  An int > 5.
    
    data_mode : (string) can be one of two kinds:
        
    - The string "random".  Then the initial state is to be randomly generated.
      The element at [i,j] is 1 with probability 1/(abs(i-j)+2); otherwise 0.
        
    - The string name of a plain text file storing the initial state.  If the
      world read from the file is bigger than nr-by-nc, use only the rows and
      columns of data that fit on the nr-by-nc array to be returned
    """
    pass  # TO-DO: implement this function 
    if data_mode == "random":
        #Initializing a new array of the same size with zeros
        first_world = np.zeros(int(nr*nc)).reshape(nr,nc) 
        for i in range(nr):
            for j in range(nc): 
                #Randomly assigning elements as 1s or 0s with the probability given
                first_world[i,j] = np.random.choice([0,1], p=(1/(abs(i-j)+2),1-(1/(abs(i-j)+2))))
    
    else: 
        first_world = np.loadtxt(data_mode, 'int', '#')
        #Cases where the array shape in the textfile is larger than specified nr,nc
        if first_world.shape[0] > nr or first_world.shape[1]>nc:
            first_world = first_world[0:nr,0:nc]
        
    return first_world
        

def one_generation_later(w, add_rule):
    """
    Returns a new array representing the world matrix w after ONE generation
    according to the rules of the game of life

    Parameters
    ----------
    w : the world matrix, a 2-d array.
    
    add_rule: (bool) If True, apply extra-life-rule; 
              otherwise do not apply extra-life-rule.
    """
    pass  # TO-DO: implement this function 
    if add_rule == True:
        #Assigning a variable with a 0.4 probability of revival IF the extra-life rule is specified 
        revive = (0.6,0.4)
    else:
        #If not specified, assigning the probability of revival as 0
        revive = (1,0)
        
    #Initializing a new variable to count the number of live neighbors
    live_count = sum_neighbors(w)
    for i in range(nr):
        for j in range(nc):
            
            #All cases where a cell is alive (denoted by 1)
            if w[i,j] == 1:
                #Cases where a cell has either lesser than 2 or greater than 3 live neighbors
                if live_count[i,j] < 2 or live_count[i,j] > 3:
                    w[i,j] = 0
                #Cases where a cell has either 2 or 3 live neighbors 
                else:
                    w[i,j] = 1
            #All cases where a cell is dead (denoted by 0)         
            else: 
                #Cases where a cell has 3 live neighbors (reproduce)
                if live_count[i,j] == 3:
                    w[i,j] = 1
                #New-life rule where a cell has greater than or equal to 4 live neighbors
                elif live_count[i,j]>=4:
                    w[i,j] = np.random.choice([0,1],p=revive)
                else:
                    #Cases where the cell remains dead
                    w[i,j] = 0
    return w

def simulate(n, nr, nc, data_mode, add_rule, blink):
    """
    Returns the world matrix after simulating n generations of the game of life
    
    Parameters
    ----------
    n : the number of generations (steps), a non-negative int
    
    nr : the number of rows in the world.  An int > 5.
    
    nc : the number of columns in the world.  An int > 5.
    
    data_mode : (string) can be one of two things:
        
     - The string "random". Then the initial state is to be randomly generated.
     The element at [i,j] is 1 with probability 1/(abs(i-j)+2); otherwise 0.
        
     - The string name of a plain text file storing the initial state.  If the
        world read from the file is bigger than nr-by-nc, use only the rows and
        columns of data that fit on the nr-by-nc array to returned
    
    add_rule: (bool) If True, apply extra-life-rule; 
              otherwise do not apply extra-life-rule.
              
    blink : a positive float.  blink > 1 means no animation
            blink <= 1 is the blink rate of the animation, i.e., the pause time
            in seconds between generations 
    """
    pass  # TO-DO: implement this function 
    world1 = create_world (nr,nc,data_mode)
    world_current = world1
    plt.close() # Close any currently opened figure window
    fig, ax = plt.subplots() # Get the figure reference (fig) and axes reference (ax) for a subplot
    ax.matshow(world_current) # Show the values in matrix w using default colors on the axes
    # Use your world matrix, which may not be called w
    ax.set_title(f'New World') # You need to write an f-string to replace the blank (see diagram)
    plt.pause(blink) # blink is a parameter in function simulate
    
    #Game simulation for when blink is greater than 1
    if blink>1:
        for sim in range(n):
            world_new = one_generation_later(world_current, add_rule)
            world_current = world_new
            ax.matshow(world_current)
            ax.set_title(f'Simulation {sim}')
            
   #Game simulation for when blink is less than or equal to 1         
    else:
        for sim in range(n):
            world_new = one_generation_later(world_current, add_rule)
            world_current = world_new
            ax.clear() # Clear axes
            ax.matshow(world_current)
            ax.set_title(f'Simulation {sim+1}')
            plt.pause(blink)                
                                        
                    

#### TO-DO: Specify and implement at least one helper function here

#Function to count the number of live neighbors each cell has:
def sum_neighbors(w):
    """
    Counts the number of live neighbors each cell in a given world has

    Parameters
    ----------
    w: current world (in the form of an array)
    
    Returns
    
    live_count: number of live neighbors for each cell (array)
    
    """
    
    live_count = np.zeros((nr*nc)).reshape(nr,nc)
    for i in range (nr):
        for j in range (nc):
            #Setting limits for the range around which neighbors can be counted
            iMin = max(0,i-1)
            iMax = min (nr,i+1+1)
            jMin = max(0, j-1)
            jMax = min(nc, j+1+1)
            
            #Creating a subset array of the immediate neighbors for each cell
            neighb = w[iMin:iMax, jMin:jMax]
            #Counting the number of rows, columns to loop through
            numrows_neighb = neighb.shape[0]
            numcols_neighb = neighb.shape[1]
            sum_incl = 0
            #Counting the number of live neighbors in this neighbor array around a cell
            for k in range(numrows_neighb):
                for l in range(numcols_neighb):
                    sum_incl = sum_incl + neighb[k,l]
            #The total count includes the cell in the center so this must be subtracted        
            sum_neighb = sum_incl - w[i,j]
            live_count[i,j] = sum_neighb
    return live_count
            
        
#### Script code
if __name__ == "__main__":
    # This is a convenient place to write code to test your functions 
    # individually as you develop your program!!

    # TO-DO: Add more code here and execute the script for testing
    
    nr= 5
    nc= 8
    simulate(20, nr, nc, "seeds_p48.txt", True, 0.2)

    
    