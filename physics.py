import numpy as np

import bodies
from bodies import Body
from constants import SUN_MASS, G, epsilon

def apply_gravity(Bodies):

    accList = [0] * len(Bodies)

    for i in range (0, len(Bodies)):
        for j in range (1, len(Bodies)):
            if i != j:
                displacement = Bodies[j].position - Bodies[i].position
                dist_squared = displacement.dot(displacement)
                softened = dist_squared + epsilon**2
                accList[j] -= G * Bodies[i].mass * displacement / softened**1.5

    for k in range(len(Bodies)):
        Bodies[k].velocity += accList[k]
        Bodies[k].position += Bodies[k].velocity
