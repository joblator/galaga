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
spaceship_width = spaceship.get_width
spaceship_height = spaceship.get_height
enemy_width = enemy_sprite.get_width
enemy_height = enemy_sprite.get_height
MOVE_SPEED = 5
MAX_ENEMIES = 3
ENEMY_SPEED = 3


spaceship_x = screen.get_width() // 2 + 10
spaceship_y = screen.get_height() - spaceship.get_size()[1]
spaceship_hitbox = pygame.Rect(spaceship_x, spaceship_y, spaceship.get_width(), spaceship.get_height())
enemies = []



def check_boundaries():
    global spaceship_x
    global spaceship_hitbox
    if spaceship_x < 0:
        spaceship_x = 0
        spaceship_hitbox = pygame.Rect(spaceship_x, spaceship_y, spaceship.get_width(), spaceship.get_height())
    if spaceship_x > screen.get_width() - spaceship.get_size()[0]:
        spaceship_x = screen.get_width() - spaceship.get_size()[0] 
        spaceship_hitbox = pygame.Rect(spaceship_x, spaceship_y, spaceship.get_width(), spaceship.get_height())


def generateEnemies():
    global enemies
    global enemy_width
    global enemy_height
    
    if len(enemies) < MAX_ENEMIES:
        x = random.randint(0, screen.get_size()[0] - enemy_sprite.get_size()[0])
        y = 0
        enemy_width = enemy_sprite.get_width()  # Get enemy width
        enemy_height = enemy_sprite.get_height()  # Get enemy height
        enemy_rect = pygame.Rect(x, y, enemy_width, enemy_height)
        enemies.append([x, y])

        



def showEnemies():
    print(enemies)
    global screen
    for enemy in enemies:
        screen.blit(enemy_sprite, (enemy[0],enemy[1]))


def moveEnemies():
    global enemies
    index = 0 
    for enemy in enemies:
        enemy[1] += ENEMY_SPEED
        index += 1




def removeEnemies():
    global enemies
    index = 0
    for enemy in enemies:
        if enemy[1] > screen.get_size()[1]:
            enemies.remove(enemy)
            index += 1

def collision_detect():
    global spaceship_hitbox
    global enemies
    spaceship_rect = pygame.Rect(spaceship_hitbox)
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)
        if spaceship_rect.colliderect(enemy_rect):
            print("Collision detected!")








pygame.display.set_caption("Galaga")


while True:  
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == K_LEFT:
            spaceship_x -= MOVE_SPEED
            spaceship_hitbox = pygame.Rect(spaceship_x, spaceship_y, spaceship.get_width(), spaceship.get_height())
        elif event.key == K_RIGHT:
            spaceship_x += MOVE_SPEED
            spaceship_hitbox = pygame.Rect(spaceship_x, spaceship_y, spaceship.get_width(), spaceship.get_height())
    screen.blit(bg,(0,0))
    moveEnemies()
    generateEnemies()
    showEnemies()
    check_boundaries()
    collision_detect()
    removeEnemies()
    print(enemies)
    screen.blit(spaceship,(spaceship_x, spaceship_y))
    pygame.display.update()
