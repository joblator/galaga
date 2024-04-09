import pygame
import sys
import time
from pygame.locals import *
import random
pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
bg = pygame.image.load(("space.jpg"))
spaceship = pygame.image.load("galaga_ship.png")
enemy_sprite = pygame.image.load("enemy_sprite.png")

MOVE_SPEED = 5
MAX_ENEMIES = 5
ENEMY_SPEED = 3


spaceship_x = screen.get_width() / 2 + 10
spaceship_y = screen.get_height() - spaceship.get_size()[1]

enemies = []


def check_boundaries():
    global spaceship_x
    if spaceship_x < 0:
        spaceship_x = 0
    if spaceship_x > screen.get_width() - spaceship.get_size()[0]:
        spaceship_x = screen.get_width() - spaceship.get_size()[0] 


def generateEnemies():
    global enemies
    if (len(enemies) < MAX_ENEMIES):
        x = random.randint(0, screen.get_size()[0]-enemy_sprite.get_size()[0])
        enemies.append([x,0])



def showEnemies():
    print(enemies)
    global screen
    for enemy in enemies:
        screen.blit(enemy_sprite, (enemy[0],enemy[1]))


def movePlayers():
    global enemies
    for enemy in enemies:
        enemy[1] += ENEMY_SPEED



def removePlayers():
    global enemies
    for enemy in enemies:
        if enemy[1] > screen.get_size()[1]:
            enemies.remove(enemy)






pygame.display.set_caption("Galaga")


while True:  
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == K_LEFT:
            spaceship_x -= MOVE_SPEED
        elif event.key == K_RIGHT:
            spaceship_x += MOVE_SPEED
    screen.blit(bg,(0,0))
    movePlayers()
    generateEnemies()
    showEnemies()
    check_boundaries()
    removePlayers()
    screen.blit(spaceship,(spaceship_x, spaceship_y))
    pygame.display.update()
