# robot.py
from interval import Interval
from shapes import draw_disk
import matplotlib.pyplot as plt
import copy


class Robot:
    """
    A robot has an id_, a maximum weight it can pick up, a list of periods
    when it is occupied with tasks it has been assigned, a list of locations
    at each time step, and a list of items picked. A robot moves in the
    cardinal directions only--north, east, south, west (NESW)--and moves
    one unit distance in each time step.

    Attributes
    ----------
    _id_ : int
        The robot's identifier
    _max_weight : number
        maximum weight that the robot can pick up at each pickup
    _total_time : int
        Maximum number of time steps the robot can be on (moving, picking)
    _occupied_periods : list
        Each element of the list is an `Interval` when the robot is occupied 
        with a task.  The list is initially empty.
        Example: if the robot is assigned a task from time 1 to time 3 and
        another task from time 4 to time 5, then the list should be
            [Interval(1,3), Interval(4,5)]
    _locations : list
        Each element of the list is the location of the robot at a time step.
        Initially the list has just the starting location of the robot,
        corresponding to time 1. The maximum eventual length of the list 
        is `_total_time`.  Each location is itself a list of two ints: the 
        x-coordinate followed by the y-coordinate.
        Example: if `Robot` at position (4,5) is allocated a task that 
        requires it to move east 2 units of distance, then three consecutive
        rows of `_locations` would be
            [[4,5], [5,5], [6,5]]
        indicating that `Robot` moves two units east over two time steps.
    _items_picked : list
        Each element of the list is an item that the robot has picked up.  The
        list is initially empty.
    """

    def __init__(self, id_, max_weight, starting_location, total_time):
        """
        Initializes a `Robot` object

        Parameters
        ----------
        id_ : int
            Robot's identifier.
        max_weight : number
            maximum weight that the robot is able to pick up
        starting_location : list
            a length 2 list of the initial location (x- and y-coord) of the robot
        total_time : int
            Maximum number of time steps the robot can be on, positive
        """
        # TODO: implement this method
    
        self.id_ = id_
        self.max_weight = max_weight
        self.starting_location = starting_location
        self.total_time = total_time
        self.occupied_periods = []
        self.locations = [starting_location]
        self.items_picked = []

    def get_id(self):
        """
        Returns (int) the `_id_` of the robot
        """
        # TODO: implement this method
        return self.id_
            


    def get_items_picked(self):
        """
        Returns a copy of the `_items_picked`.
        """
        # TODO: implement this method
        return copy.deepcopy(self.items_picked)
    


    def get_locations(self):
        """
        Return a copy of the `_locations`
        """
        # TODO: implement this method
        return copy.deepcopy(self.locations)
    


    def where_am_i(self):
        """
        Determine the most recent location of the `Robot` along with the time
        it corresponded to.  The most recent location is the last location in
        `_locations`.  

        Returns a tuple (lis, time) where
        -------
        lis : list
            a new list of length 2 that stores the most recent location (x-y
            coordinate)
        time : int
            time of most the recent location
        """
        # TODO: implement this method
        time = len(self.locations)
        lis = self.locations[time-1]

        return lis, time
        


    def steps_to_arrival(self, loc):
        """
        Returns a valid list of locations for each time step of a path that the 
        robot can take from its current location to reach the location `loc`. 
        The path needs not be optimal.  The first location of the list is the 
        robot's current location; the last location of the list is `loc`.
        
        This method considers the path only and does not consider whether 
        there is enough time to reach `loc`.  

        Parameters
        ----------
        loc : list
            a length 2 list storing the destination x-y coordinate
        """
        # TODO: implement this method
    
        steps = []
        x_disp = loc[0]-self.locations[-1][0]
        y_disp = loc[1]-self.locations[-1][1]
        
        for x in range(x_disp):
            steps.append((self.locations[-1][0]+x+1,self.locations[-1][1]))
        for y in range(y_disp):
            steps.append((loc[0],self.locations[-1][1]+y+1))
            
        return steps
    


    def pick(self, item, do_pick=True):
        """
        Returns True if the robot is able to pick up the item; returns False otherwise.
        
        Determines whether the robot should pick up `item`.  If so, executes 
        the pick if `do_pick` is True.
        
        The robot should pick up `item` when the following are true:
          1. the robot's physical characteristics allows it to pick up `item`,
          2. the robot can travel to `item` and fully pick it up in time, and
          3. `item` can be picked up (it is not already scheduled for pickup).
        
        If the pickup does occur,
          1. Update `item`'s picked_window
          2. Update `Robot`'s `_locations`, `occupied_periods`, and
               `_items_picked`. The `Interval` appended to `occupied_periods` 
               should include both the travel time and pickup duration.
        No attributes should be updated if the pickup does not occur.

        Parameters
        ----------
        item : Item
            The item to be picked up by the robot

        do_pick : Boolean
            Indicates if the robot should execute the pick should it be possible.
            Default is True.

        Returns
        -------
        Boolean
            Whether the pick is possible
        """
        # TODO: implement this method
        time = len(self.locations)
        if item.valid_pickup(self.max_weight,0) == True and time+len(self.steps_to_arrival(item.loc))+item.duration <= self.total_time and item.picked_window == None and do_pick == True:
                item.update_pickup_status(time+len(self.steps_to_arrival(item.loc)))
                self.locations = self.locations + self.steps_to_arrival(item.loc)
                for arrival in range(item.duration):
                    self.locations = self.locations + [item.loc]
                self.occupied_periods.append(Interval(time, time+len(self.steps_to_arrival(item.loc))+item.duration))
                self.items_picked.append(item)
                return True
        else:   
            return False
            
                
    


    def draw(self, t):
        """
        Draw a blue circle of diameter 1 to represent the robot at time `t`.
        Label the circle at the center with its `_id_`.
        
        Assumes figure window is already open.
        
        Parameter t: (int) the time. t>=1 
        """
        
        draw_disk(self.locations[t][0],self.locations[t][1],0.5,c = 'c')
        idtext_robot = str(self.id_); # u is number
        plt.text(self.locations[t][0],self.locations[t][1],idtext_robot,horizontalalignment="center")
    

