import pygame
import sys
import time
from pygame.locals import *
import random
pygame.init()
pygame.mixer.init()


# all the files
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
bg = pygame.image.load(("space.jpg"))
spaceship = pygame.image.load("galaga_ship.png")
enemy_sprite = pygame.image.load("enemy_sprite.png")
bullet_sprite = pygame.image.load("bullet.png")



#all the variables
spaceship_width = spaceship.get_width()
spaceship_height = spaceship.get_height()
enemy_width = enemy_sprite.get_width()
enemy_height = enemy_sprite.get_height()
LEFT_BORDER = 0
RIGHT_BORDER = screen.get_width() - enemy_width
MOVE_SPEED = 5
MAX_ENEMIES = 3
ENEMY_SPEED = 2
BULLET_SPEED = 10
MAX_BULLETS = 1
spaceship_x = screen.get_width() // 2 + 10
spaceship_y = screen.get_height() - spaceship.get_size()[1]
spaceship_hitbox = pygame.Rect(spaceship_x, spaceship_y, spaceship.get_width(), spaceship.get_height())
enemies = []
bullets = []
points = 0

#fonts and sounds
font = pygame.font.SysFont(None, 24)
hit_sound = pygame.mixer.Sound("enemy_death.mp3")
hit_sound.set_volume(1)
pygame.mixer.music.load('filibuster.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
shoot_sound = pygame.mixer.Sound('pewpew.mp3')
game_over_sound = pygame.mixer.Sound('game_over.wav')

#find the highest enemy and return its y
def findTopPlayerY():
    global enemies
    min_y=screen.get_height()

    for enemy in enemies:
        if enemy[1]<min_y:
            min_y=enemy[1]
    return min_y

#check if the player is on the screen if not return him to the left or right border
def check_boundaries():
    global spaceship_x
    global spaceship_hitbox
    if spaceship_x < 0:
        spaceship_x = 0
        spaceship_hitbox = pygame.Rect(spaceship_x, spaceship_y, spaceship.get_width(), spaceship.get_height())
    if spaceship_x > screen.get_width() - spaceship.get_size()[0]:
        spaceship_x = screen.get_width() - spaceship.get_size()[0] 
        spaceship_hitbox = pygame.Rect(spaceship_x, spaceship_y, spaceship.get_width(), spaceship.get_height())

#randomly adds enemies in a random x spot at the top of the screen
def generateEnemies():
    global enemies
    if (findTopPlayerY()> spaceship.get_size()[1]) and (len(enemies)<MAX_ENEMIES):
            x = random.randint(LEFT_BORDER,RIGHT_BORDER)
            enemies.append([x,0])

#makes a bullet when the player shoots
def generate_bullet():
    keys = pygame.key.get_pressed()
    global spaceship_y
    global spaceship_x
    global bullets
    if event.type == pygame.KEYDOWN:
        if event.key == K_UP:
            if len(bullets) < MAX_BULLETS:
                bullets.append([spaceship_x + spaceship_width - 53,spaceship_y - 30])
                shoot_sound.play()



#prints the bullets on the screen
def show_bullets():
    global screen
    for bullet in bullets:
        screen.blit(bullet_sprite, (bullet[0],bullet[1]))
#moves the bullets
def move_bullets():
    global bullets
    for bullet in bullets:
        bullet[1] -= BULLET_SPEED
            

#shows the enemies on the screen
def showEnemies():
    global screen
    for enemy in enemies:
        screen.blit(enemy_sprite, (enemy[0],enemy[1]))

#moves the enemies
def moveEnemies():
    global enemies
    for enemy in enemies:
        enemy[1] += ENEMY_SPEED



#checks of the enemies are below the floor if so remove then
def removeEnemies():
    global points
    global enemies
    for enemy in enemies:
        if enemy[1] > screen.get_size()[1]:
            enemies.remove(enemy)
            points += 100
    return points

# return the value in the highscore file
def load_highscore():
    try:
        with open("highscore.txt", "r") as scorefile:
            highscore = scorefile.read().strip()
            if highscore.isdigit():
                return int(highscore)
    except FileNotFoundError:
        pass
    return 0

#saves the points as the new hightscore
def save_highscore(new_score):
    with open("highscore.txt", "w") as scorefile:
        scorefile.write(str(new_score))
  

#makes a hitbox of the player and the enemies and checks if they collide
def collision_detect():
    global enemies
    spaceship_hitbox = pygame.Rect(spaceship_x, spaceship_y, spaceship.get_width(), spaceship.get_height())
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)
        if spaceship_hitbox.colliderect(enemy_rect):
            game_over_sound.play()
            pygame.mixer.music.stop()
            time.sleep(1)
            if load_highscore() < points:
                save_highscore(points)
            sys.exit()

#makes a hitbox of the bullets and enemies and checks if they collide
def bullet_collision_detect():
    global enemies
    global bullets
    global points
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)
        for bullet in bullets:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_sprite.get_width(), bullet_sprite.get_height())
            if enemy_rect.colliderect(bullet_rect):
                if enemy in enemies:
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    points += 200
                    hit_sound.play()
            if bullet[1] < 0:
                bullets.remove(bullet)



pygame.display.set_caption("Galaga")

#main gameloop  
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
    text = font.render('points: '+ str(points), True, (255, 255, 255))
    screen.blit(bg,(0,0))
    screen.blit(text, (0, 0))
    moveEnemies()
    generateEnemies()
    generate_bullet()
    show_bullets()
    move_bullets()
    bullet_collision_detect()
    showEnemies()
    check_boundaries()
    collision_detect()
    removeEnemies()
    screen.blit(spaceship,(spaceship_x, spaceship_y))
    pygame.display.update()
