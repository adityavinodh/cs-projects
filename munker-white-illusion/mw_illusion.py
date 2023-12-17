# mw_illusion.py
"""
Module for drawing and displaying the Munker-White Illusion
"""
import shapes
import matplotlib.pyplot as plt


def draw_illusion(n, w, cg, cs, f, a, b):
    """
    Display the Munker-White Illusion in the current figure window
    
    Parameters:
      n:  (int) number of grid rectangles, i.e., the long rectangles that span 
          the width of the diagram.  An int greater than 1.
      w:  (float or int) width of grid rectangles
      cg: (string) color of grid rectangles.  A predefined color name such as 
          'k', 'b', ..., etc.
      cs: (string) color of the two stacks of narrow rectangles. A predefined 
          color name such as 'k', 'b', ..., etc. 
      f:  (float) a fraction greater than 0 and less than 0.5.  The horizontal 
          width of the narrow rectangles is f*w. 
      a:  (float) the x-coordinate of the lower left corner of the diagram
      b:  (float) the y-coordinate of the lower left corner of the diagram

    The height of each rectangle is one. There are n-1 narrow rectangles in 
    each stack, and the two stacks are horizontally centered in the diagram, 
    with the same amount of space left of the left stack, between the stacks, 
    and right of the right stack.
    Check parameter f:  if f>=.5, set f to .3
    
    Returns None
    """
    
    #Setting the f value if not given.
    if f >=0.5:
        f = 0.3
        
        #Drawing the grid rectangles 
        for i in range(0,n):
            shapes.draw_rect(a,b+2*i, w, 1, cg )
        
        #Drawing the 2 sets of narrow rectangles    
        for i in range (0,n-1,2):         
            shapes.draw_rect(a+(w/9),(b+1+2*i),(f*w),1, cs) 
            shapes.draw_rect((a+2*w/9)+f*w,b+2*i,(f*w),1, cs)
        
    else:
        f = f
        
        #Drawing the grid rectangles 
        for i in range(0,n):
            shapes.draw_rect(a,b+2*i, w, 1, cg )
            
        #Drawing the 2 sets of narrow rectangles       
        for i in range (0,n-1,2):         
            shapes.draw_rect(a+w/9,b+1+2*i,(f*w),1, cs)
            shapes.draw_rect((a+2*w/9)+f*w,b+2*i,(f*w),1, cs)
            
     

#----
# Demonstration: draw three different Munker-White Illusions where the left 
# two are strong and the right one is weak.  All three diagrams are drawn on 
# one set of axes.  (Do not use subplots.)
#----
plt.close()
plt.figure(figsize=[9,3])  # Change figure size (default is [6.4, 4.8])
plt.axis('equal')

# TO-DO: complete the code below to draw the three illusions

# Example 1 Strong illusion
a=0; b=0  # coordinates of lower left corner of first illusion to draw

draw_illusion(8,15,'g','r',0.5,-20,0) #Setting the grid, narrow rectangle colors to green and red

# Example 2 Strong illusion

draw_illusion(8,15,'b','c',0.5,0,0) #Setting the grid, narrow rectangle colors to blue and cyan 

# Example 3 Weak illusion

draw_illusion(8,15,'orange','b',0.5,20,0) #Setting the grid, narrow rectangle colors to orange and blue
