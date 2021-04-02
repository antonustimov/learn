import pygame
import random

# screen
WIDTH = 360
HEIGHT = 480
FPS = 30

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

# game cycle
running = True
while running:
# holding right cycle speed
    clock.tick(FPS)
    # input of process or event
    for event in pygame.event.get():
        # chek for closing window
        if event.type == pygame.QUIT:
            running = False


# update

# render
screen.fill(BLACK)
# after render we flip screen and draw
pygame.display.flip()


pygame.quit()