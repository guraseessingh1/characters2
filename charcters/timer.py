import pygame
from time import *
from pygame.locals import *

pygame.init()
WIDTH = 400
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
start = pygame.image.load("images/red_button.jpg")
start = pygame.transform.scale(start,(WIDTH,HEIGHT))

while True:
    screen.fill((255,255,255))
    screen.blit(start,(0,0))
    font = pygame.font.SysFont("Times New Roman", 40)
    pygame.display.update()



