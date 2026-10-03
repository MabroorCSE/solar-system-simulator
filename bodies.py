import numpy as np

class Body:
    def __init__(self, mass, size, colour, pos_x, pos_y, vel_x, vel_y):
        self.mass = mass
        self.size = size
        self.colour = colour
        self.position = np.array([pos_x, pos_y], dtype=float)
        self.velocity = np.array([vel_x, vel_y], dtype=float)


