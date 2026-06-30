from vpython import *
from math import *
def find_alpha1(theta1, theta2, omega1, omega2, stringLength):
    """
    finds the acceleration of ball1
    
Attributes:
    theta1(float): angle between string1 and the vertical
    theta2(float): angle between string2 and the vertical
    omega1(float): change in theta1
    omega2(float): change in theta2
    stringLength(float or int): length of the string
    
Returns:
    float: acceleration
    """
    alpha1 = (9.8*(3*sin(theta1) + sin(theta1-2*theta2)) + 2*stringLength*sin(theta1-theta2)*(omega1**2*cos(theta1-theta2)+omega2**2))/(stringLength*(cos(2*(theta2-theta1))-3))
    return alpha1

def find_alpha2(theta1, theta2, omega1, omega2, stringLength):
    """
    finds the acceleration of ball2
    
Attributes:
    theta1(float): angle between string1 and the vertical
    theta2(float): angle between string2 and the vertical
    omega1(float): change in theta1
    omega2(float): change in theta2
    stringLength(float or int): length of the string
    
Returns:
    float: acceleration
    """
    alpha2 = (2*sin(theta1-theta2)*(omega1**2*stringLength*2 + 9.8*2*cos(theta1) + omega2**2*stringLength*cos(theta1-theta2))) / (stringLength*(3 - cos(2*theta1-2*theta2)))
    return alpha2

# print(find_theta(vec(-1,0,0)))