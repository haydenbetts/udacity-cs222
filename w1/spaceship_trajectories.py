# PROBLEM 3
#
# Modify the below functions acceleration and 
# ship_trajectory to plot the trajectory of a 
# spacecraft with the given initial position 
# and velocity. Use the Forward Euler Method 
# to accomplish this.

from matplotlib.pyplot import plt

h = 1.0 # s
earth_mass = 5.97e24 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

h = 1.0 # s
earth_mass = 5.97e24 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

def acceleration(spaceship_position):
    # get unit vector pointing from ship to earth
    ship_to_earth_vec = spaceship_position * -1
    ship_to_earth_length = numpy.linalg.norm(ship_to_earth_vec)
    ship_to_earth_unit = (ship_to_earth_vec) / ship_to_earth_length

    # Scale ship_to_moon_unit, ship_to_earth_unit by the acceleration due to gravity expression
    # I omit ship mass bc it drops out of the equation, unecessary to find acceleration
    acc_gravity_earth_ship = (gravitational_constant * (earth_mass / (ship_to_earth_length**2))) * ship_to_earth_unit
    
    return acc_gravity_earth_ship
    
def ship_trajectory():
    num_steps = 13000
    x = numpy.zeros([num_steps + 1, 2]) # m
    v = numpy.zeros([num_steps + 1, 2]) # m / s

    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3

	###Your code here. This code should call the above 
    for step in range(num_steps):
        v[step + 1][0] = v[step][0] + acceleration(x[step])[0] * h
        v[step + 1][1] = v[step][1] + acceleration(x[step])[1] * h
        x[step + 1][0] = x[step][0] + v[step][0] * h
        x[step + 1][1] = x[step][1] + v[step][1] * h
	
    return x, v

x, v = ship_trajectory()

@show_plot
def plot_me():
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.scatter(0, 0)
    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
plot_me()
    


