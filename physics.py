import numpy as np
from bodies import Body
from constants import SUN_MASS, G

def apply_gravity(body1, body2):
    displacement = body2.position - body1.position
    distance = np.linalg.norm(displacement)
    direction = displacement / distance

    force = G * body1.mass * body2.mass / distance**2 * direction

    if not body1.mass == SUN_MASS:
        acc1 = force/body1.mass
        body1.velocity += acc1
        body1.position += body1.velocity

    if not body2.mass == SUN_MASS:
        acc2 = -force/body2.mass
        body2.velocity += acc2
        body2.position += body2.velocity
