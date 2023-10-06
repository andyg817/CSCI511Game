import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
MONSTER_SIZE = 50
PLAYER_SPEED = 2
MONSTER_SPEED = 1

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Crawler")

# Load all images
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (PLAYER_SIZE, PLAYER_SIZE))
monster_img = pygame.image.load("monster.png")
monster_img = pygame.transform.scale(monster_img, (MONSTER_SIZE, MONSTER_SIZE))
background_img = pygame.image.load("floor.png")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

#Initial positions
player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT - PLAYER_SIZE - 10
monster_x = random.randint(0, WIDTH - MONSTER_SIZE)
monster_y = random.randint(0, HEIGHT - MONSTER_SIZE)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_d] and player_x < WIDTH * PLAYER_SIZE:
        player_x += PLAYER_SPEED
    if keys[pygame.K_w] and player_y > 0:
        player_y -= PLAYER_SPEED
    if keys[pygame.K_s] and player_y < HEIGHT * PLAYER_SIZE:
        player_y += PLAYER_SPEED

    # Move the monster towards the player
    if monster_x < player_x:
        monster_x += MONSTER_SPEED
    elif monster_x > player_x:
        monster_x -= MONSTER_SPEED
    if monster_y < player_y:
        monster_y += MONSTER_SPEED
    elif monster_y > player_y:
        monster_y -= MONSTER_SPEED

    #Draw everything
    screen.blit(background_img, (0, 0))
    screen.blit(player_img, (player_x, player_y))
    screen.blit(monster_img, (monster_x, monster_y))

    #Check for collision
    player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
    monster_rect = pygame.Rect(monster_x, monster_y, MONSTER_SIZE, MONSTER_SIZE)

    if player_rect.colliderect(monster_rect):
        print("You were caught by the monster!")
        running = False

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
