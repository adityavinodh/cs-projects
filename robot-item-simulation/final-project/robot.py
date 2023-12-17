# robot.py
import math
from interval import Interval
from shapes import draw_disk
import matplotlib.pyplot as plt
import copy
import numpy as np


class Robot:
    """
    A robot has an id_, a maximum weight it can pick up, a list of periods
    when it is occupied with tasks it has been assigned, a list of locations
    at each time step, and a list of items picked. A robot moves in the
    cardinal directions only--north, east, south, west (NESW)--and moves
    one unit distance in each time step.
    
    Class attribute
    ---------------
    color : str
        Robot's color. A regular `Robot` is blue

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
        is `_total_time`.  Each location is itself a list of two numbers: the
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

    color= 'b'  # Class attribute


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

        self._id_ = id_
        self._max_weight = max_weight
        self._locations = [starting_location]
        self._items_picked = []
        self._occupied_periods = []
        self._total_time = total_time
        

    def get_id(self):
        """
        Returns (int) the `_id_` of the robot
        """

        return self._id_
    

    def get_total_time(self):
        """
        Returns (int) the `_total_time` of the robot
        """
        return self._total_time
    

    def get_items_picked(self):
        """
        Returns a copy of the `_items_picked`.
        """

        return copy.deepcopy(self._items_picked)
    
    

    def get_locations(self):
        """
        Return a copy of the `_locations`
        """

        # return self._locations.copy()
        return copy.deepcopy(self._locations)
    

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

        return self._locations[-1].copy(), len(self._locations)
    

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

        # Current location
        initial_pos, _ = self.where_am_i()

        # Not required: same locations case
        if np.allclose(initial_pos, loc):
            return [initial_pos]

        init_x = initial_pos[0]
        init_y = initial_pos[1]

        # Change all of x, then change all of y
        steps = []
        delta_x = loc[0] - init_x
        if not np.allclose(delta_x, 0):
            sign = int(delta_x / abs(delta_x))
            for x in range(init_x, loc[0] + sign, sign):
                steps.append([x, init_y])
        else:
            x = init_x
            steps.append(initial_pos)

        delta_y = loc[1] - init_y
        if not np.allclose(delta_y, 0):
            sign = int(delta_y / abs(delta_y))
            # Have to offset initial y to prevent repeat
            for y in range(init_y + sign, loc[1] + sign, sign):
                steps.append([x, y])
        return steps


    def pick(self, item, do_pick=True, max_payload=None, num_arms=0):
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
          2. Update `Robot`'s `_locations`, `_occupied_periods`, and
               `_items_picked`. The `Interval` appended to `_occupied_periods`
               should include both the travel time and pickup duration.
        No attributes should be updated if the pickup does not occur.

        Parameters
        ----------
        item : Item
            The item to be picked up by the robot

        do_pick : Boolean
            Indicates if the robot should execute the pick should it be possible.
            Default is True.

        max_payload : number
            Maximum weight the `Robot` can pick up (positive)

        num_arms : int
            number of arms (>= 0)

        Returns
        -------
        Boolean
            Whether the pick is possible
        """

        if max_payload is None:
            max_payload = self._max_weight

        success = False

        # Time needed to travel and pick up.
        # Arrive at item, then spend item.duration time there to pick up
        steps = self.steps_to_arrival(item.loc)
        travel_time = len(steps) - 1  # steps includes starting position
        time_needed = travel_time + item.duration

        # Time remaining
        time_so_far = len(self._locations)
        time_remaining = self._total_time - time_so_far

        if (time_needed <= time_remaining and item.picked_window is None
                and item.valid_pickup(max_payload, num_arms)):
            success = True
        if do_pick and success:
            pick_start = time_so_far
            pick_end = time_so_far + time_needed
            self._occupied_periods.append(Interval(pick_start, pick_end))
            item.update_pickup_status(pick_start + travel_time)
            self._items_picked.append(item)

            # Update locations
            location_picking = [item.loc for _ in range(item.duration)]

            # Don't use steps[0] since that repeats the starting location
            self._locations = self._locations + steps[1:] + location_picking

        return success
    

    def draw(self, t):
        """
        Draw a blue circle of diameter 1 to represent the robot at time `t`.
        Label the circle at the center with its `_id_`.

        Assumes figure window is already open.

        Parameter t: (int) the time. len(self._locations)>=t>=1
        """

        r = 0.5
        center = self._locations[t - 1]
        draw_disk(center[0], center[1], r, self.color)
        plt.text(center[0], center[1], str(self._id_),
                 horizontalalignment='center')


class FastRobot(Robot):
    """
    A `FastRobot` is a `Robot`. A `FastRobot` can move at most `_speed_multiplier`
    distance in one timestep. A `FastRobot` is green ('g')
    
    Class attribute
    ---------------
    color : str
        FastRobot's color. A `FastRobot` is green
        
    Instance attributes
    -------------------
    _speed_multiplier : number
        The distance that a `FastRobot` is able to move in one time step 
    """
    
    color= 'g'  # Class attribute
    

    def __init__(self, id_, max_weight, starting_loc, total_time,
                 speed_multiplier=np.random.randint(1, 7)):
        """
        Construct a `FastRobot` with a speed multiplier.
        """
        # TODO: implement this method as specified

        super().__init__(id_, max_weight, starting_loc, total_time)
        self.speed_multiplier = speed_multiplier 
        

        
    def steps_to_arrival(self, loc):
        """
        Returns the list of locations for each time step of a path that the 
          robot takes from its current location to reach the location `loc`. 
          This robot can move `_speed_multiplier` distance in one timestep.
          This robot can only move in one direction once it starts moving,
          meaning it can only move in the straight line path from its starting 
          location to `loc`.  The first location of the list is the robot's 
          current location; the last location of the list is `loc`.

        Parameter `loc`:
            (list) a length 2 list storing the destination x-y coordinate

        Example 1: If a `FastRobot` with speed multiplier of 3 is to go from
          [0,0] to [4,0], then the list of locations is [[0,0], [3,0], [4,0]]
        Example 2: If a 'FastRobot' with speed multiplier of sqrt(2) is to go from
          [0,0] to [2,2], then the list of locations is [[0,0], [1.0,1.0], [2,2]]
        Example 3: If a 'FastRobot' with speed multiplier of 6 is to go from
          [0,0] to [3,4], then the list of locations is [[0,0], [3,4]]
        """
        # TODO: implement this method as specified
        pass
    
        initial_pos, _ = self.where_am_i()
        
        
        init_x = initial_pos[0]
        init_y = initial_pos[1]
        dx = loc[0] - init_x
        dy = loc[1] - init_y

        theta = np.arctan2(dy, dx)
        
        steps = []
        x = init_x
        y = init_y
        alpha = math.ceil(self.speed_multiplier)
        
        
        if not np.allclose(dx, 0) and not np.allclose(dy, 0):
            steps.append(initial_pos)
 
            while not (np.allclose(x,loc[0]) and np.allclose(y,loc[1])) and (alpha<=dx or alpha<=dy):
                x = int(x+alpha*np.cos(theta))
                y = int(y+alpha*np.sin(theta))
                steps.append([x, y])
                dy = dy = loc[1] - y
                dx = loc[0] - x
                
            
            if dx>0 and dy>0 and (alpha >=dx or alpha >= dy):
                steps.append([loc[0],loc[1]])
                
        if np.allclose(dx,0):
            for y in range(init_y, loc[1], alpha):
                    steps.append([init_x, y])
                    dy = loc[1] - y
                    
            if alpha >= dy:
                steps.append([loc[0],loc[1]])
                
        
        if np.allclose(dy,0):
            for x in range(init_x, loc[0], alpha):
                steps.append([x,init_y])
                dx = loc[0] - x
                
            if alpha >= dx:
                steps.append([loc[0],loc[1]])
            
            

        return steps
    
    

class LimbedRobot(Robot):
    """
    A `LimbedRobot` is a `Robot` that has arm capabilities and can lift
    heavier items. A `LimbedRobot` can only move `_slowdown_multiplier`
    distance in one timestep.
    A `LimbedRobot` is magenta ('m')
    
    Class attribute
    ---------------
    color : str
        LimbedRobot's color.  A `LimbedRobot` is magenta
        
    Instance attributes
    -------------------
    _slowdown_multiplier : float
        A `LimbedRobot` can move `_slowdown_multiplier` units in one timestep.
        Assume this is in the range (0, 1)
    _max_payload_factor : int
        A `LimbedRobot` can pick up `_max_payload_factor` times
        its `_max_weight`.  Default to a random integer between 2 and 7.
    _num_arms : int
        Number of arms the `LimbedRobot` has
    """
    
    color= 'm'  # Class attribute


    def __init__(self, id_, max_weight, starting_loc, total_time,
                  num_arms, slowdown_multiplier,max_payload_factor):
        """
        Construct a `LimbedRobot` with a `_slowdown_multiplier` and a 
          `_max_payload_factor`
        """
        # TODO: implement this method as specified
        pass
        super().__init__(id_, max_weight, starting_loc, total_time)
        self._max_payload_factor = self._max_weight
        self._slowdown_multiplier = slowdown_multiplier
        self._num_arms = num_arms
    
        

    def steps_to_arrival(self, loc):
        """
        Returns the list of locations for each time step of a path that the 
          robot takes from its current location to reach the location `loc`. 
          This robot can only move `_slowdown_multiplier` distance in one
          timestep and can only move in either the x or the y direction in one
          step.  The first location of the list is the robot's current 
          location; the last location of the list is `loc`.
 
        Parameter `loc`:
            (list) a length 2 list storing the destination x-y coordinate
       """
        # TODO: implement this method as specified
        pass
    
        # Current location
        initial_pos, _ = self.where_am_i()
        
        slowalpha = self._slowdown_multiplier

        # Not required: same locations case
        if np.allclose(initial_pos, loc):
            return [initial_pos]

        init_x = initial_pos[0]
        init_y = initial_pos[1]
        x_current = init_x
        y_current = init_y

        # Change all of x, then change all of y
        steps = [(init_x,init_y)]
        delta_x = loc[0] - init_x
        delta_y = loc[1] - init_y
        
        if not np.allclose(delta_x, 0):
            sign = int(delta_x / abs(delta_x))
            if sign == 1:
                while not np.allclose(x_current, loc[0]):
                    x_current = x_current + slowalpha*sign
                    
                    if x_current>=loc[0]:
                        steps.append([loc[0], init_y])
                        x_current = loc[0]
                    else:
                        steps.append([x_current, init_y])
                        
            if sign == -1:
                while not np.allclose(x_current, loc[0]):
                    x_current = x_current + slowalpha*sign
                    
                    if x_current <= loc[0]:
                        steps.append([loc[0], init_y])
                        x_current = loc[0]
                    else:
                        steps.append([x_current, init_y])
                
                
               
        if not np.allclose(delta_y, 0):
            sign = int(delta_y / abs(delta_y))
            if sign == 1:
               while not np.allclose(y_current, loc[1]):
                    y_current = y_current + slowalpha*sign
                    if y_current>=loc[1]:
                        y_current = loc[1]
                        steps.append([loc[0], loc[1]])
                    else:
                        steps.append([loc[0], y_current])
                
            if sign == -1:
                while not np.allclose(y_current, loc[1]):
                     y_current = y_current + slowalpha*sign
                     if y_current<=loc[1]:
                        y_current = loc[1]
                        steps.append([loc[0], loc[1]])
                     else:
                         steps.append([loc[0], y_current])
                
        
        return steps
    
    
    

    def pick(self, item, do_pick=True):
        """
        Override `Robot`'s pick method.
        The only difference is that a `LimbedRobot` has a different payload
          and a number of arms.
        """
        # TODO: implement this method as specified
        pass
        
        return Robot.pick(self, item, do_pick=True, max_payload = self._max_payload_factor, num_arms = self._num_arms)
        

                 
    
