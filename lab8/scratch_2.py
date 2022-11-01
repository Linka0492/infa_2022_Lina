import pygame
from pygame.draw import *

pygame.init()
color = (255, 255, 204)
FPS = 30

screen = pygame.display.set_mode((400, 400))
screen.fill(color)
circle(screen, (255, 255, 0), (200, 175), 150)
circle(screen, (0, 0, 0), (200, 175), 150, 5)


circle(screen, (102, 255, 204), (150, 150), 25)
circle(screen, (102, 255, 204), (250, 150), 25)
circle(screen, (0, 0, 0), (150, 150), 15)
circle(screen, (0, 0, 0), (250, 150), 15)
rect(screen, (0, 0, 0), (150, 225, 50, 8))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()