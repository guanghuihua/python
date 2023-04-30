import sys
import pygame
import random
import math

from pygame.locals import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    pygame.display.set_caption("circle demo")
    screen.fill((0, 0, 100))

    pos_x = 300
    pos_y = 200
    radius = 200
    angle = 360

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()

        angle += 1
        if angle >= 360:
            angle = 0
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = r, g, b

        X = math.cos(math.radians(angle)) * radius
        Y = math.sin(math.radians(angle)) * radius

        pos = (int(pos_x + X), int(pos_y + Y))

        pygame.draw.circle(screen, color, pos, 100, 10)

        pygame.display.update()
