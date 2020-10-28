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
backgroundSound = mixer.music.load('sounds/background.wav')
mixer.music.play(-1)

#Charaters set up
class Character():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0
    
    

class Player(Character):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.playerImage = pygame.image.load('images/player.png')
        self.move = 0.3
    def display(self):
        screen.blit(self.playerImage,(self.x,self.y))
    def player_move(self):
        if event.type == pygame.KEYDOWN:
            #right
            if event.key == pygame.K_RIGHT:
                self.x_change += self.move
            #left
            if event.key == pygame.K_LEFT:
                self.x_change -= self.move
            #up
            if event.key == pygame.K_UP:
                self.y_change -= self.move
            #down
            if event.key == pygame.K_DOWN:
                self.y_change += self.move
        elif event.type == pygame.KEYUP:
            self.x_change = 0
            self.y_change = 0
        


fo = Player(370,480)


gameon = True
while gameon:
    screen.fill((0,0,0))
    screen.blit(backgroundImg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False

    fo.x +=fo.x_change
    fo.y +=fo.y_change
    fo.player_move()
    fo.display()
    pygame.display.update()

