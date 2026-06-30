from .accelerationfunc import find_alpha1, find_alpha2

def rk4(theta1, theta2, omega1, omega2, stringLength, dt):
    """
    approximates using the Runge Kutta 4 algorithm

Attributes:
    (Note: all inputs are numbers -> floats or integers)

    theta1(float): angle between string1 and the vertical
    theta2(float): angle between string2 and the vertical
    omega1(float): change in theta1
    omega2(float): change in theta2
    stringLength(float or int): length of the string
    
Returns:
    new_theta1, new_theta2, new_omega1, new_omega2: 4 updated values after the timestep
    """
    # Each 'k' is a (velocity, acceleration) pair sampled at different points, for both balls

    #speed and acceleration at the start
    k1_v1 = omega1
    k1_v2 = omega2
    k1_a1 = find_alpha1(theta1, theta2, omega1, omega2, stringLength)
    k1_a2 = find_alpha2(theta1, theta2, omega1, omega2, stringLength)

    #acceleration at midpoint, approximate 1
    k2_v1 = omega1 + 0.5*dt*k1_a1
    k2_v2 = omega2 + 0.5*dt*k1_a2
    k2_a1 = find_alpha1(theta1 + 0.5*dt*k1_v1, theta2 + 0.5*dt*k1_v2, k2_v1, k2_v2, stringLength)
    k2_a2 = find_alpha2(theta1 + 0.5*dt*k1_v1, theta2 + 0.5*dt*k1_v2, k2_v1, k2_v2, stringLength)

    #acceleration at midpoint, approximate 2
    k3_v1 = omega1 + 0.5*dt*k2_a1
    k3_v2 = omega2 + 0.5*dt*k2_a2
    k3_a1 = find_alpha1(theta1 + 0.5*dt*k2_v1, theta2 + 0.5*dt*k2_v2, k3_v1, k3_v2, stringLength)
    k3_a2 = find_alpha2(theta1 + 0.5*dt*k2_v1, theta2 + 0.5*dt*k2_v2, k3_v1, k3_v2, stringLength)

    #acceleration at endpoint
    k4_v1 = omega1 + dt*k3_a1
    k4_v2 = omega2 + dt*k3_a2
    k4_a1 = find_alpha1(theta1 + dt*k3_v1, theta2 + dt*k3_v2, k4_v1, k4_v2, stringLength)
    k4_a2 = find_alpha2(theta1 + dt*k3_v1, theta2 + dt*k3_v2, k4_v1, k4_v2, stringLength)

    # Weighted average update
    new_theta1 = theta1 + (dt / 6) * (k1_v1 + 2*k2_v1 + 2*k3_v1 + k4_v1)
    new_theta2 = theta2 + (dt / 6) * (k1_v2 + 2*k2_v2 + 2*k3_v2 + k4_v2)
    new_omega1 = omega1 + (dt / 6) * (k1_a1 + 2*k2_a1 + 2*k3_a1 + k4_a1)
    new_omega2 = omega2 + (dt / 6) * (k1_a2 + 2*k2_a2 + 2*k3_a2 + k4_a2)

    return new_theta1, new_theta2, new_omega1, new_omega2