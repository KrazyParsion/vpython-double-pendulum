#used to surpress warnings because a vpython dependency from previous python versions is changed/deleted
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

#imports used
from vpython import *
from functions import find_alpha1, find_alpha2, find_theta, rk4
from math import *

#colours
scene.background = vector(.123,.213,.255)*3 #background color
darkGray = hat(vec(99,102,106)) #custom color

#setup/default variables
l = 10 #length of strings
#initial speed of the balls
v1 = 10
v2 = 10

#vectors for position and velocity of both balls
b1Position = hat(vec(0,-1,0))*l #vector for string1
b2Position = hat(vec(0,-1,0))*l #vector for string2
v_ball1 = hat(vec(1,0,0))*v1
v_ball2 = hat(vec(1,0,0))*v2

#time related settings
timestep_per_frame = 10
dt = 1/60/timestep_per_frame
t = 0

#unit vectors in x and y coordinates
yHat = vec(0,1,0)
xHat = vec(1,0,0)
# theta1 = diff_angle()


#objects for making the double pendulum
pivot = cylinder(pos=vec(0,0,-2), axis=vec(0,0,4), radius=2, color=darkGray*0.5)
string1 = cylinder(pos=vec(0,0,0), axis=b1Position, radius=1, color=darkGray)
string2 = cylinder(pos=b1Position, axis=b2Position, radius=1, color=darkGray)
ball1 = sphere(pos=b1Position, radius=2, color=color.red)
ball2 = sphere(pos=b1Position+b2Position, radius=2, color=color.red)

#initial function settings for angles
theta1 = 0
theta2 = 0
omega1 = mag(v_ball1)/l
omega2 = mag(v_ball2)/l

#time text
scene.append_to_caption("\n")
time = wtext(text = "time = 0s", format = ".3g")
scene.append_to_caption("\n\n")

#start the animation, rewrite the variables based on the sliders
running = False
def start():
    global theta1, theta2, omega1, omega2, running, t
    theta1 = Theta1Slider.value
    theta2 = Theta2Slider.value
    omega1 = Omega1Slider.value
    omega2 = Omega2Slider.value
    running = True
    t = 0
button(left = 12, bind = start, text = "Start")

#stop the animation
def stop():
    global running
    running = False
button(left = 12, bind = stop, text = "Stop")

#change Theta1
def adjustTheta1():
    Theta1.text = str(Theta1Slider.value) + "rad"
scene.append_to_caption("\n\n")
Theta1Slider = slider(min=-pi, max=pi, step=pi/18, value=0,
                     bind=adjustTheta1)
scene.append_to_caption(" Ball1's Angle = ")
Theta1 = wtext(text = "0 rad")

#change Theta2
def adjustTheta2():
    Theta2.text = str(Theta2Slider.value) + "rad"
scene.append_to_caption("\n\n")
Theta2Slider = slider(min=-pi, max=pi, step=pi/18, value=0,
                     bind=adjustTheta2)
scene.append_to_caption(" Ball2's Angle = ")
Theta2 = wtext(text = "0 rad")

#change Omega1
def adjustOmega1():
    Omega1.text = str(Omega1Slider.value) + "rad"
scene.append_to_caption("\n\n")
Omega1Slider = slider(min=-3*pi, max=3*pi, step=pi/18, value=0,
                     bind=adjustOmega1)
scene.append_to_caption(" Ball1's Angular Speed = ")
Omega1 = wtext(text = "0 rad/s")

#change Omega2
def adjustOmega2():
    Omega2.text = str(Omega2Slider.value) + "rad"
scene.append_to_caption("\n\n")
Omega2Slider = slider(min=-pi, max=pi, step=pi/18, value=0,
                     bind=adjustOmega2)
scene.append_to_caption(" Ball2's Angular Speed = ")
Omega2 = wtext(text = "0 rad/s")

#animation loop
while True:
    #first loop to check for slider changes
    rate(60)
    while running:
        #second loop for animation
        rate(60)
        for i in range(timestep_per_frame):
            #runs many calculations per frame to increase accuracy
            theta1, theta2, omega1, omega2 = rk4(theta1, theta2, omega1, omega2, l, dt)
            t += dt
        string1.axis = vec(sin(theta1), -cos(theta1), 0)*l
        ball1.pos = string1.axis
        string2.pos = string1.axis
        string2.axis = vec(sin(theta2), -cos(theta2), 0)*l
        ball2.pos = string2.axis + string1.axis
        time.text = "{:.3g}s".format(t)
    







# def pendulum_derivatives

# def rk4_step(state, dt):
#     """
#     state: """


# while True:
#     theta1 = find_theta(b1Position)
#     theta2 = find_theta(b2Position)
#     omega1 = v1/l
#     omega2 = v2/l
#     alpha1 = find_alpha1(theta1, theta2, omega1, omega2, l)
#     alpha2 = find_alpha2(theta1, theta2, omega1, omega2, l)
#     K11 = omega1
#     K12 = omega2
#     K21 = (omega1 + alpha1*)



