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
    def movement(self):
        """
            Defines Player movement pattern
        """
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

class Enemy(Character):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.enemyImage = pygame.image.load('images/enemy.png')
        self.move = 5
    def display(self):
        screen.blit(self.enemyImage,(self.x,self.y))
    def movement(self):
        """
        Defines enemies movement pattern
        """
        self. x+= self.move
        if self.x >= 750:
            self.x_change -= self.move
            self.y += 10
        if self.x <= 0:
            self.x_change += self.move
            self.y += 10

class Bullet(Character):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.bulletImage = pygame.image.load('images/bullet.png')
        self.move = 0.5
        self.bullet_state = 'ready'
    def fire(self,x,y):
        """
            displays the bullet on the screen
        """
        self.bullet_state = 'fire'
        screen.blit(self.bulletImage,(self.x+16,self.y-10))
    def movement(self,x,y):
        """
            Is the actual firing of the bullet
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.y_change +=self.move
                self.y+=self.y_change
                if self.bullet_state is 'ready':
                    #sound
                    bullet_sound = mixer.Sound('sounds/laser.wav')
                    bullet_sound.play()
                    #effects
                    self.x = x
                    self.y = y
                    self.fire(x,self.y)
    def reset(self,y):
        """
            Resets bullet unto players position
        """
        if self.y<=0:
            self.y = y
            self.bullet_state = 'ready'
        if self.bullet_state is 'fire':
            self.y -= self.y_change
            self.fire(self.x,self.y)


#Creating player
fo = Player(370,480)

#Creating enemies
no_of_enemies = 5
enemies = []
for e in range(no_of_enemies):
    enemies.append(Enemy(random.randint(30,730),random.randint(50,150)))
     
# en_one = Enemy(random.randint(30,730),random.randint(50,150))

#Creating bullet
blt = Bullet(fo.x,fo.y)




gameon = True
while gameon:
    screen.fill((0,0,0))
    screen.blit(backgroundImg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                blt.movement(fo.x,fo.y)
        blt.movement(fo.x,fo.y)

#player
    fo.x +=fo.x_change
    fo.y +=fo.y_change
    fo.movement()
    if fo.x <= 0:
        fo.x = 0
    if fo.x >= 736:
        fo.x = 736
    if fo.y <= 0:
        fo.y = 0
    if fo.y >= 536:
        fo.y = 536
    
    
    

#enemy
    for e in range(no_of_enemies):
        enemies[e].display()
        enemies[e].movement()
        enemies[e].x +=enemies[e].x_change
#Game Over

#killed

#bullet movement
    blt.reset(fo.y)
    
#display
    #player
    fo.display()
    #life

    #scores



    pygame.display.update()

