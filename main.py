
import pygame
import sys
import time
from pygame.locals import *

pygame.init()

MOVE_SPEED = 20

clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))

bg = pygame.image.load(("space.jpg"))
spaceship = pygame.image.load("spaceship.png")

spaceship_x = screen.get_width() / 2 + 10
spaceship_y = screen.get_height() - spaceship.get_size()[1]
def check_boundaries():
    global spaceship_x
    if spaceship_x < 0:
        spaceship_x = 0
    if spaceship_x > screen.get_width() - spaceship.get_size()[0]:
        spaceship_x = screen.get_width() - spaceship.get_size()[0]


pygame.display.set_caption("Galaga")


while True:  
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT  :
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                spaceship_x -= MOVE_SPEED
            elif event.key == K_RIGHT:
                spaceship_x += MOVE_SPEED
    check_boundaries()
    screen.blit(bg,(0,0))
    screen.blit(spaceship,(spaceship_x, spaceship_y))
    pygame.display.update()
