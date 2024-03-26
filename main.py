
import pygame
import time

pygame.init()
SPACESHIP_SPEED = 100
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('galaga in pygame')
spaceship_y = 20
spaceship_X = 20

keys = pygame.key.get_pressed()
    
if keys[pygame.K_LEFT] and >0: 
    x -= speed
if keys[pygame.K_RIGHT] and <500: 
    x += speed 
if keys[pygame.K_UP] and >0: 
    y -= speed    
if keys[pygame.K_DOWN] and <500:   
    y += speed 

pygame.quit()