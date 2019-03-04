# QUIZ
#
# Modify the acceleration function so that it returns 
# the acceleration vector of the spacecraft.
#
# A sample of how to use the numpy.linalg.norm function
# is given. This computes the length of the vector, and 
# it should be the only outside function you need to 
# use in your answer.

import numpy
import matplotlib

earth_mass = 5.97e24 # kg
moon_mass = 7.35e22 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

# The origin, or (0,0), is at the center of the earth 
# in this example, so it doesn't make any sense to 
# set either the moon_position or spaceship_position
# equal to (0,0). Depending on your solution, doing this
# may throw an error!  Please note that moon_position and 
# spaceship_position are both numpy arrays, and the 
# returned value should also be a numpy array.

def acceleration(moon_position, spaceship_position):

    # get unit vector pointing from ship to earth
    ship_to_earth_vec = spaceship_position * -1
    ship_to_earth_length = numpy.linalg.norm(ship_to_earth_vec)
    ship_to_earth_unit = (ship_to_earth_vec) / ship_to_earth_length

    # get unit vector pointing from ship to moon
    ship_to_moon_vec =  moon_position - spaceship_position
    ship_to_moon_length = numpy.linalg.norm(ship_to_moon_vec)
    ship_to_moon_unit = ship_to_moon_vec / ship_to_moon_length

    # Scale ship_to_moon_unit, ship_to_earth_unit by the acceleration due to gravity expression
    # I omit ship mass bc it drops out of the equation, unecessary to find acceleration
    acc_gravity_earth_ship = (gravitational_constant * (earth_mass / (ship_to_earth_length**2))) * ship_to_earth_unit
    acc_gravity_moon_ship = (gravitational_constant * (moon_mass / (ship_to_moon_length**2))) * ship_to_moon_unit
    
    # add components of acc due to gravity acting on the ship
    acc_gravity_net = acc_gravity_earth_ship + acc_gravity_moon_ship
    
    return acc_gravity_net