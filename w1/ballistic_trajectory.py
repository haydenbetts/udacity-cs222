# PROBLEM 2
#
# Modify the trajectory function below to 
# plot the trajectory of several particles. 
# Each trajectory starts at the point (0,0) 
# given initial speed in the direction 
# specified by the angle. Use the Forward 
# Euler Method to accomplish this.
# Currently, we plot tracetories produced by both

import numpy
import matplotlib.pyplot as plt

h = 0.1 # s
g = 9.81 # m / s2
acceleration = numpy.array([0., -g])
initial_speed = 20. # m / s

def trajectory():
    angles = numpy.linspace(20., 70., 6)

    num_steps = 30
    x = numpy.zeros([num_steps + 1, 2])
    v = numpy.zeros([num_steps + 1, 2])

    for angle in angles:
        # set the intial values
        rad = numpy.radians(angle)
        x[0][0] = 0
        x[0][1] = 0
        v[0][0] = initial_speed*numpy.cos(rad)
        v[0][1] = initial_speed*numpy.sin(rad)

        for step in range(num_steps):
            v[step + 1][0] = v[step][0] + acceleration[0] * h
            v[step + 1][1] = v[step][1] + acceleration[1] * h
            x[step + 1][0] = x[step][0] + v[step][0] * h
            x[step + 1][1] = x[step][1] + v[step][1] * h

        plt.plot(x[:, 0], x[:, 1])
    """
    plt.axis('equal')
    axes = plt.gca()
    axes.set_xlabel('Horizontal position in m')
    axes.set_ylabel('Vertical position in m')
    plt.show()
    """
    return x, v

#trajectory()

def trajectory_attempt_1():
    angles = numpy.linspace(20., 70., 6)

    num_steps = 30
    x = numpy.zeros([num_steps + 1, 2])
    v = numpy.zeros([num_steps + 1, 2])
    
    for angle in angles:

        rad = numpy.radians(angle)
        x[0][0] = 0
        x[0][1] = 0
        v[0][0] = initial_speed * numpy.cos(rad)
        v[0][1] = initial_speed * numpy.sin(rad)
            
        for step in range(num_steps):
            t = (step + 1) * h # .1, .2, .3 ... 3
            v_x_est = initial_speed*numpy.cos(rad) + acceleration[0] * t
            v_y_est = initial_speed*numpy.sin(rad) + acceleration[1] * t # 9.8 * .1, 9.8 * .2, .....
            x_est = v_x_est * t
            y_est = v_y_est * t
    
            v[step + 1][0] = v_x_est
            v[step + 1][1] = v_y_est
            x[step + 1][0] = x_est
            x[step + 1][1] = y_est

        plt.plot(x[:, 0], x[:, 1])
    plt.axis('equal')
    axes = plt.gca()
    axes.set_xlabel('Horizontal position in m')
    axes.set_ylabel('Vertical position in m')
    plt.show()
    return x, v     

trajectory()
trajectory_attempt_1()