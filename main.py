import pygame
import sys
from bodies import Body
from physics import apply_gravity
from constants import SUN_MASS, G, TRAIL_NUM

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulator")

clock = pygame.time.Clock()


Bodies = [
    Body(SUN_MASS, 30, (255, 255, 0), 640, 360, 0, 0), #Sun
    Body(1, 10, (255, 255, 255), 640, 500, 3.2, 0), #Planet1
    Body(5, 15, (0, 255, 255), 240, 300, 0, -1.6), #Planet 2
]

#Stores last TRAIL_NUM positions of every body
Trails = [
    [], #Sun
    [], #Planet1
    [], #Planet2
]



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

            #if len(Trails[i]) > 1:
                

        

        pygame.draw.circle(screen, body.colour, body_position, body.size)

    print (Trails)

    for i in range (len(Bodies)):

        for j in range (i+1, len(Bodies)):
            apply_gravity(Bodies[i], Bodies[j])

    pygame.display.flip()
    clock.tick(60)  # 60 fps cap

