import numpy as np

class Body:
    def __init__(self, mass, size, colour, pos_x, pos_y, vel_x, vel_y):
        self.mass = mass
        self.size = size
        self.colour = colour
        self.position = np.array([pos_x, pos_y], dtype=float)
        self.velocity = np.array([vel_x, vel_y], dtype=float)


def create_bodies(sun_mass):
    return [
        Body(sun_mass, 30, (255, 255, 0), 640, 360, 0, 0), #Sun
        Body(10, 10, (255, 255, 255), 650, 500, 3.2, 0), #Planet1
        Body(50, 15, (0, 255, 255), 240, 300, 0, -1.1), #Planet 2
        Body(100, 8, (255, 0, 0), 800, 650, -2.5, -0.5), #Planet 3
        Body(50, 12, (20, 200, 45), 240, 450, 0.5, -1.5) #Planet 3
    ]
