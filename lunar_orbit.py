import numpy
import matplotlib.pyplot as plt

moon_distance = 384e6 # m

# TODO some type of off-by-one error

def orbit():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])
    
    for step in range(num_steps):
        x[step + 1][0] = 384e6*numpy.cos((2 * numpy.pi) / num_steps * step)
        x[step + 1][1] = 384e6*numpy.sin((2 * numpy.pi) / num_steps * step)
    
    return x

orbit_coords = orbit()
orbit_x = orbit_coords[:, 0]
orbit_y = orbit_coords[:, 1]

plt.plot(orbit_x, orbit_y)
plt.xlabel('x')
plt.ylabel('y')

plt.title("Moon Orbit")

plt.show()