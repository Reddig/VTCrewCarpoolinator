from pygametest import pygame_plot
from visualizer_utils import convert_coordinates


coverted = convert_coordinates(coords_hardcoded, 1200, 800, -80.38, 37.1, 0.08, 0.2)

pygame_plot(coverted)