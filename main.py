import random
import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)

SCREENWIDTH = 800
SCREENHEIGHT = 600

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.display.set_caption("Cookie Clicker")
icon = pygame.image.load('Cookie.png')
pygame.display.set_icon(icon)