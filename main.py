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
    Body(10, 10, (255, 255, 255), 650, 500, 3.2, 0), #Planet1
    Body(50, 15, (0, 255, 255), 240, 300, 0, -1.1), #Planet 2
    Body(100, 8, (255, 0, 0), 800, 650, -2.5, -0.5), #Planet 3
    Body(50, 12, (20, 200, 45), 240, 450, 0.5, -1.5) #Planet 3
]

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

    apply_gravity(Bodies)


    pygame.display.flip()
    clock.tick(60)  # 60 fps cap

