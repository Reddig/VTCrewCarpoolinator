import sys, pygame
from typing import List, Tuple
from visualizer_utils import convert_coordinates



def pygame_plot(coords):
    pygame.init()

    size = width, height = 1200, 800
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    surface = pygame.display.get_surface()

    # will need to be inverted in y direction (height - y)
    #coords = [(800,200), (600,600), (400,400), (200,200), (100,100)]

    screen.fill(black)
    for c in coords:
        print(c)
        pygame.draw.circle(surface, (255,255,255), c, 10)

    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
