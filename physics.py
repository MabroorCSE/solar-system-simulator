import numpy as np

import bodies
from bodies import Body
from constants import SUN_MASS, G, epsilon

# def apply_gravity(body1, body2):
#     displacement = body2.position - body1.position
#     distance = np.linalg.norm(displacement)
#     direction = displacement / distance
#
#     force = G * body1.mass * body2.mass / distance**2 * direction
#
#     if not body1.mass == SUN_MASS:
#         acc1 = force/body1.mass
#         body1.velocity += acc1
#         body1.position += body1.velocity
#
#     if not body2.mass == SUN_MASS:
#         acc2 = -force/body2.mass
#         body2.velocity += acc2
#         body2.position += body2.velocity

def apply_gravity(Bodies):

    accList = [0] * len(Bodies)

    for i in range (0, len(Bodies)):
        for j in range (1, len(Bodies)):
            if i != j:
                displacement = Bodies[j].position - Bodies[i].position
                distance = np.linalg.norm(displacement)
                #print(Bodies[i].position, Bodies[j].position, distance)
                direction = displacement / distance

                force = G * Bodies[i].mass * Bodies[j].mass / (distance**2 + epsilon**2) * direction

                acc = force/Bodies[j].mass
                accList[j] += acc

    print(accList)
    for k in range(0, len(Bodies)):
        Bodies[k].velocity -= accList[k]
        Bodies[k].position += Bodies[k].velocity

    # if not body1.mass == SUN_MASS:
    #     acc1 = force/body1.mass
    #     body1.velocity += acc1
    #     body1.position += body1.velocity
    #
    # if not body2.mass == SUN_MASS:
    #     acc2 = -force/body2.mass
    #     body2.velocity += acc2
    #     body2.position += body2.velocity
