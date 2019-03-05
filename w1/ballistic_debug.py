import numpy
import matplotlib.pyplot as plt

num_steps = 30
h = .1

v = numpy.zeros([num_steps, 2])

# initial forward Euler attempt involved velocity estimates of the form
for step in range(num_steps):
    t = h * step
    v[step][0] = t
    v[step][1] = 20*numpy.sin(numpy.radians(20)) - 9.8*(t)

# the correct velocity estimate was
v_2 = numpy.zeros([num_steps + 1, 2])

# set initial values
v_2[0][0] = 0
v_2[0][1] = 20*numpy.sin(numpy.radians(20))

for step in range(num_steps):
    v_2[step + 1][0] = h*step
    v_2[step + 1][1] = v_2[step][1] - 9.8*h

plt.plot(v[:, 0], v[:, 1])
plt.plot(v_2[:, 0], v_2[:, 1])
axes = plt.gca()
axes.set_xlabel('Time')
axes.set_ylabel('Velocity in m/s')
plt.show()


