import pygame
import sys
from bodies import create_bodies
from physics import apply_gravity
from constants import SUN_MASS, G, TRAIL_NUM, SUBSTEPS

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulator")

clock = pygame.time.Clock()


Bodies = create_bodies(SUN_MASS)

#Stores last TRAIL_NUM positions of every body
Trails = [ [] for _ in Bodies]



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # black background

    for i,body in enumerate(Bodies):
        body_position = (int(body.position[0]), int(body.position[1]))
        if i>0:
            Trails[i].append(body_position)
            if len(Trails[i]) > TRAIL_NUM:
                Trails[i].pop(0)
            if len(Trails[i]) > 1:
                pygame.draw.lines(screen, body.colour, False, Trails[i], 2)

        pygame.draw.circle(screen, body.colour, body_position, body.size)

    for _ in range(SUBSTEPS):
        apply_gravity(Bodies, 1 / SUBSTEPS)


    pygame.display.flip()
    clock.tick(60)  # 60 fps cap

