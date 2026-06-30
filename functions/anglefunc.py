from vpython import *

def find_theta(axis):
    """
    finds the angle to the vertical
    
Attributes:
    axis(vector): from up to down
    
Returns:
    radians: angle to the vertical
    """
    if axis.x < 0:
        angle = -diff_angle(vec(0,1,0), axis)
    else:
        angle = diff_angle(vec(0,1,0), axis)
    return angle