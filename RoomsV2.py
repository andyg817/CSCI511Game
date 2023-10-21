import random
import pygame
from pygame.locals import *

black = (0, 0, 0)
white = (255, 255, 255)
grey = (120, 120, 120)

# Constants from main.py - Andrew
W, H = 800, 600
pSize = 50
pSpeed = 2
pHealth = 100
pAttack = 10
pDefense = 5
pHColor = (0, 255, 0)  # Green
mSize = 50
mSpeed = 5
mHealth = 50
mHColor = (255, 0, 0)  # Red


# Load all images - main.py - Andrew
pImg = pygame.image.load("player.png")
pImg = pygame.transform.scale(pImg, (pSize, pSize))
mImg = pygame.image.load("skeleton.png")
mImg = pygame.transform.scale(mImg, (mSize, mSize))
bImg = pygame.image.load("floor.png")
bImg = pygame.transform.scale(bImg, (W, H))
wImg = pygame.image.load("wall.png")
wImg = pygame.transform.scale(wImg, (W, H))

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

# Define an empty list to hold room information--------------------------------------------------------------------
room_list = []

# Function to generate random room information
def generate_room(room):
    
    wall_list = []

    #1
    if room == 0:
        wall_list.append(Wall(600, 20, 0, 0))
        wall_list.append(Wall(20, 790, 20, 0))

        #right wall with door
        wall_list.append(Wall(590, 20, 780, 360))
        wall_list.append(Wall(240, 20, 780, 20))

        #bottom wall with door
        wall_list.append(Wall(20, 340, 20, 580))
        wall_list.append(Wall(20, 360, 460, 580))

    #2
    elif room < 9:
        wall_list.append(Wall(20, 790, 0, 0))

        #left wall with door
        wall_list.append(Wall(590, 20, 0, 360))
        wall_list.append(Wall(240, 20, 0, 20))

        #right wall with door
        wall_list.append(Wall(590, 20, 780, 360))
        wall_list.append(Wall(240, 20, 780, 20))

        #bottom wall with door
        wall_list.append(Wall(20, 340, 20, 580))
        wall_list.append(Wall(20, 360, 460, 580))
    #3
    elif room == 9:
        wall_list.append(Wall(20, 790, 20, 0))
        wall_list.append(Wall(600, 20, 780, 0))
        
        #bottom wall with door
        wall_list.append(Wall(20, 340, 20, 580))
        wall_list.append(Wall(20, 360, 460, 580))

        #left wall with door
        wall_list.append(Wall(590, 20, 0, 360))
        wall_list.append(Wall(240, 20, 0, 20))
    #4
    elif room % 10 == 0 and room < 40:
        wall_list.append(Wall(600, 20, 0, 0))

        #right wall with door
        wall_list.append(Wall(590, 20, 780, 360))
        wall_list.append(Wall(240, 20, 780, 20))

        #bottom wall with door
        wall_list.append(Wall(20, 340, 20, 580))
        wall_list.append(Wall(20, 360, 460, 580))

        #top wall with door
        wall_list.append(Wall(20, 340, 20, 0))
        wall_list.append(Wall(20, 360, 460, 0))

    #5
    elif room == 40:
        wall_list.append(Wall(600, 20, 0, 0))
        wall_list.append(Wall(20, 790, 0, 580))

        #right wall with door
        wall_list.append(Wall(590, 20, 780, 360))
        wall_list.append(Wall(240, 20, 780, 20))

        #top wall with door
        wall_list.append(Wall(20, 340, 20, 0))
        wall_list.append(Wall(20, 360, 460, 0))

    #6
    elif room > 40 and room < 49:
        wall_list.append(Wall(20, 790, 20, 580))

        #right wall with door
        wall_list.append(Wall(590, 20, 780, 360))
        wall_list.append(Wall(240, 20, 780, 20))

        #top wall with door
        wall_list.append(Wall(20, 340, 20, 0))
        wall_list.append(Wall(20, 360, 460, 0))

        #left wall with door
        wall_list.append(Wall(590, 20, 0, 360))
        wall_list.append(Wall(240, 20, 0, 20))
    #7
    elif room == 49:
        wall_list.append(Wall(20, 790, 20, 580))
        wall_list.append(Wall(600, 20, 780, 0))

        #top wall with door
        wall_list.append(Wall(20, 340, 20, 0))
        wall_list.append(Wall(20, 360, 460, 0))

        #left wall with door
        wall_list.append(Wall(590, 20, 0, 360))
        wall_list.append(Wall(240, 20, 0, 20))

    #8
    elif room % 10 == 9:
        wall_list.append(Wall(600, 20, 780, 0))

        #bottom wall with door
        wall_list.append(Wall(20, 340, 20, 580))
        wall_list.append(Wall(20, 360, 460, 580))

        #top wall with door
        wall_list.append(Wall(20, 340, 20, 0))
        wall_list.append(Wall(20, 360, 460, 0))

        #left wall with door
        wall_list.append(Wall(590, 20, 0, 360))
        wall_list.append(Wall(240, 20, 0, 20))
    #9 
    else:
        #right wall with door
        wall_list.append(Wall(590, 20, 780, 360))
        wall_list.append(Wall(240, 20, 780, 20))

        #left wall with door
        wall_list.append(Wall(590, 20, 0, 360))
        wall_list.append(Wall(240, 20, 0, 20))

        #bottom wall with door
        wall_list.append(Wall(20, 340, 20, 580))
        wall_list.append(Wall(20, 360, 460, 580))

        #top wall with door
        wall_list.append(Wall(20, 340, 20, 0))
        wall_list.append(Wall(20, 360, 460, 0))

    return wall_list

# Create some initial rooms
#for _ in range(5):
    #room = generate_random_room()
    #room_list.append(room)

# This class represents the bar at the bottom that the player controls
class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, height, width, x, y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Make a grey wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill((grey))

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):
    room_changed = False
    # Constructor function
    def __init__(self, x, y, w, h, vel, scale_factor=3):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = vel

        self.scale_factor = scale_factor
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

        # Set height, width
        self.image = pygame.Surface([50, 50])

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

        # Current room index
        self.current_room = 0  # Start in the first room

    # Change the speed of the player
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    # Find a new position for the player
    def update(self, walls):
        # Get the old position, in case we need to go back to it
        old_x = self.rect.topleft[0]
        old_y = self.rect.topleft[1]

        # Update position according to our speed (vector)
        new_x = old_x + self.change_x
        new_y = old_y + self.change_y

        # Put the player in the new spot
        self.rect.topleft = (new_x, new_y)

        # Did this update cause us to hit a wall?
        collide = pygame.sprite.spritecollide(self, walls, False)
        if collide:
            # Whoops, hit a wall. Go back to the old position
            self.rect.topleft = (old_x, old_y)

        #reset position if outside of screen-------------------------------------------------------------------------------------
        if new_x > 800:
            self.rect.topleft = (20, new_y)
            self.current_room = self.current_room + 1
            Player.room_changed = True
        elif new_y > 600:
            self.rect.topleft = (new_x, 20)
            self.current_room = self.current_room + 10
            Player.room_changed = True
        elif new_x < 0:
            self.rect.topleft = (790, new_y)
            self.current_room = self.current_room - 1
            Player.room_changed = True
        elif new_y < 0:
            self.rect.topleft = (new_x, 590)
            self.current_room = self.current_room - 10
            Player.room_changed = True

player_x, player_y = 350, 250

# Create the player paddle object
player = Player(player_x, player_y, 32, 32, 5, scale_factor=3)
movingsprites = pygame.sprite.RenderPlain((player))

# This is the main function where our program begins
def main():
    score = 0
    # Constants from main.py - Andrew
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

    # Call this function so the Pygame library can initialize itself
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
    # Set the title of the window
    pygame.display.set_caption('Dungeon Crawler')
    # Enable this to make the mouse disappear when over our window
    # pygame.mouse.set_visible(0)
    # This is a font we use to draw text on the screen (size 36)
    font = pygame.font.Font(None, 36)

    # Create a surface we can draw on
    background = pygame.Surface(screen.get_size())
    # Used for converting color maps and such
    background = background.convert()
    # Fill the screen with a black background
    background.fill(black)

    walls = pygame.sprite.RenderPlain(generate_room(player.current_room))

    clock = pygame.time.Clock()

    #Added monster x, and y from main.py
    monster_x = random.randint(0, W - mSize)
    monster_y = random.randint(0, H - mSize)

    running = True
    while running:
        clock.tick(40)

        #getting the current player x and y
        player_x = player.rect.topleft[0]
        player_y = player.rect.topleft[1]


        #Monster Movement
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


        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            #Player Movement
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    player.changespeed(-3, 0)
                if event.key == K_RIGHT:
                    player.changespeed(3, 0)
                if event.key == K_UP:
                    player.changespeed(0, -3)
                if event.key == K_DOWN:
                    player.changespeed(0, 3)


            if event.type == KEYUP:
                if event.key == K_LEFT:
                    player.changespeed(3, 0)
                if event.key == K_RIGHT:
                    player.changespeed(-3, 0)
                if event.key == K_UP:
                    player.changespeed(0, 3)
                if event.key == K_DOWN:
                    player.changespeed(0, -3)

            
        
        player.update(walls)
        walls = pygame.sprite.RenderPlain(generate_room(player.current_room))
        # Clear the screen and draw objects
        #screen.fill(black)

        

        #Check for collision
        playerRect = pygame.Rect(player.rect.topleft[0], player.rect.topleft[1], pSize, pSize)
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

        #commented out which would draw the square representing the Player class instance
        #movingsprites.draw(screen)
        walls.draw(screen)
        pygame.display.flip()

        if(Player.room_changed == True):
            monster_x = random.randint(0, W - mSize)
            monster_y = random.randint(0, H - mSize)

        Player.room_changed = False    
        #Draw everything
        screen.blit(bImg, (0, 0))
        screen.blit(pImg, (player.rect.topleft[0], player.rect.topleft[1]))
        screen.blit(mImg, (monster_x, monster_y))
        drawHealthBar(screen, player.rect.topleft[0], player.rect.topleft[1], pHealth, 100, pHColor)
        drawHealthBar(screen, monster_x, monster_y, mHealth, 50, mHColor)

# This calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()