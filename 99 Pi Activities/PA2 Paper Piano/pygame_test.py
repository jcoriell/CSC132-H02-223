
import pygame
import sys
from pygame.locals import QUIT

WIDTH = 500
HEIGHT = 500

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
