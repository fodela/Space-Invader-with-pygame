import pygame
from pygame import mixer
import random
import math


pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

#background set up
backgroundImg = pygame.image.load('images/background.jpg')
backgroundSound = mixer.music.load('sounds/back')


gameon = True
while gameon:
    screen.fill((0,0,0))
    screen.blit(backgroundImg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False

    pygame.display.update()