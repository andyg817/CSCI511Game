import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
W, H = 800, 600
pSize = 50
pSpeed = 2
pHealth = 100
pAttack = 10
pDefense = 5
pHColor = (0, 255, 0)  # Green
mSize = 50
mSpeed = 1
mHealth = 50
mHColor = (255, 0, 0)  # Red

# Create the game window
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Dungeon Crawler")

# Load all images
pImg = pygame.image.load("player.png")
pImg = pygame.transform.scale(pImg, (pSize, pSize))
mImg = pygame.image.load("monster.png")
mImg = pygame.transform.scale(mImg, (mSize, mSize))
bImg = pygame.image.load("floor.png")
bImg = pygame.transform.scale(bImg, (W, H))

#Initial positions
player_x = W // 2 - pSize // 2
player_y = H - pSize - 10
monster_x = random.randint(0, W - mSize)
monster_y = random.randint(0, H - mSize)

def attack(pAttack):
    damage = pAttack
    return damage

def block(pDefense, incDamage):
    pDamage = max(0, incDamage - pDefense)
    return pDamage

def drawHealthBar(surface, x, y, currHealth, maxHealth, color):
    bar_width = int((currHealth / maxHealth) * pSize)
    playerHealthRect = pygame.Rect(x, y, bar_width, 8)
    pygame.draw.rect(surface, color, playerHealthRect)
    monsterHealthRect = pygame.Rect(x, y, bar_width, 8)
    pygame.draw.rect(surface, color, monsterHealthRect)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= pSpeed
    if keys[pygame.K_d] and player_x < W * pSize:
        player_x += pSpeed
    if keys[pygame.K_w] and player_y > 0:
        player_y -= pSpeed
    if keys[pygame.K_s] and player_y < H * pSize:
        player_y += pSpeed

    #Monster
    if monster_x < player_x:
        monster_x += mSpeed
    elif monster_x > player_x:
        monster_x -= mSpeed
    else:
        monster_x = monster_x
    if monster_y < player_y:
        monster_y += mSpeed
    elif monster_y > player_y:
        monster_y -= mSpeed
    else:
        monster_y = monster_y

    #Draw everything
    screen.blit(bImg, (0, 0))
    screen.blit(pImg, (player_x, player_y))
    screen.blit(mImg, (monster_x, monster_y))
    drawHealthBar(screen, player_x, player_y, pHealth, 100, pHColor)
    drawHealthBar(screen, monster_x, monster_y, mHealth, 50, mHColor)

    #Check for collision
    playerRect = pygame.Rect(player_x, player_y, pSize, pSize)
    monsterRect = pygame.Rect(monster_x, monster_y, mSize, mSize)

    if playerRect.colliderect(monsterRect):
        if not keys[pygame.K_h]:
            pHealth -= .5
        if keys[pygame.K_g]:
            mHealth -= 1
        if pHealth <= 0:
            print("Game Over - Player defeated!")
            running = False
        elif mHealth <= 0:
            print("Victory! You defeated the monster!")
            running = False
    pygame.display.update()

# Quit the game
pygame.quit()
