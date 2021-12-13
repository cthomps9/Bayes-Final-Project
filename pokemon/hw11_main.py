

def height_func(x, y):
	"""
	x^2 + xy − 2y^2
	"""
	h = (x ** 2) + x*y - 2*(y ** 2)

	return h


step_size = 0.1
num_steps = 21


x_points, y_points, z_points = [], [], []
for xi in range(num_steps):
	x = -1 + xi * step_size

	for yi in range(num_steps):
		y = -1 + yi * step_size

		z = height_func(x, y)

		x_points.append(x)
		y_points.append(y)
		z_points.append(z)


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='Greens');
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')


plt.show()