import random
import pygame
from pygame.locals import *

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Define an empty list to hold room information--------------------------------------------------------------------
room_list = []

# Function to generate random room information
def generate_room(room):
    
    wall_list = []

    #1
    if room == 0:
        wall_list.append(Wall(600, 10, 0, 0))
        wall_list.append(Wall(10, 790, 10, 0))

        #right wall with door
        wall_list.append(Wall(590, 10, 790, 340))
        wall_list.append(Wall(260, 10, 790, 10))

        #bottom wall with door
        wall_list.append(Wall(10, 360, 10, 590))
        wall_list.append(Wall(10, 360, 440, 590))

    #2
    elif room < 9:
        wall_list.append(Wall(10, 790, 0, 0))

        #left wall with door
        wall_list.append(Wall(590, 10, 0, 340))
        wall_list.append(Wall(260, 10, 0, 10))

        #right wall with door
        wall_list.append(Wall(590, 10, 790, 340))
        wall_list.append(Wall(260, 10, 790, 10))

        #bottom wall with door
        wall_list.append(Wall(10, 360, 10, 590))
        wall_list.append(Wall(10, 360, 440, 590))
    #3
    elif room == 9:
        wall_list.append(Wall(10, 790, 10, 0))
        wall_list.append(Wall(600, 10, 790, 0))
        
        #bottom wall with door
        wall_list.append(Wall(10, 360, 10, 590))
        wall_list.append(Wall(10, 360, 440, 590))

        #left wall with door
        wall_list.append(Wall(590, 10, 0, 340))
        wall_list.append(Wall(260, 10, 0, 10))
    #4
    elif room % 10 == 0 and room < 40:
        wall_list.append(Wall(600, 10, 0, 0))

        #right wall with door
        wall_list.append(Wall(590, 10, 790, 340))
        wall_list.append(Wall(260, 10, 790, 10))

        #bottom wall with door
        wall_list.append(Wall(10, 360, 10, 590))
        wall_list.append(Wall(10, 360, 440, 590))

        #top wall with door
        wall_list.append(Wall(10, 360, 10, 0))
        wall_list.append(Wall(10, 360, 440, 0))

    #5
    elif room == 40:
        wall_list.append(Wall(600, 10, 0, 0))
        wall_list.append(Wall(10, 790, 0, 590))

        #right wall with door
        wall_list.append(Wall(590, 10, 790, 340))
        wall_list.append(Wall(260, 10, 790, 10))

        #top wall with door
        wall_list.append(Wall(10, 360, 10, 0))
        wall_list.append(Wall(10, 360, 440, 0))

    #6
    elif room > 40 and room < 49:
        wall_list.append(Wall(10, 790, 10, 590))

        #right wall with door
        wall_list.append(Wall(590, 10, 790, 340))
        wall_list.append(Wall(260, 10, 790, 10))

        #top wall with door
        wall_list.append(Wall(10, 360, 10, 0))
        wall_list.append(Wall(10, 360, 440, 0))

        #left wall with door
        wall_list.append(Wall(590, 10, 0, 340))
        wall_list.append(Wall(260, 10, 0, 10))
    #7
    elif room == 49:
        wall_list.append(Wall(10, 790, 10, 590))
        wall_list.append(Wall(600, 10, 790, 0))

        #top wall with door
        wall_list.append(Wall(10, 360, 10, 0))
        wall_list.append(Wall(10, 360, 440, 0))

        #left wall with door
        wall_list.append(Wall(590, 10, 0, 340))
        wall_list.append(Wall(260, 10, 0, 10))

    #8
    elif room % 10 == 9:
        wall_list.append(Wall(600, 10, 790, 0))

        #bottom wall with door
        wall_list.append(Wall(10, 360, 10, 590))
        wall_list.append(Wall(10, 360, 440, 590))

        #top wall with door
        wall_list.append(Wall(10, 360, 10, 0))
        wall_list.append(Wall(10, 360, 440, 0))

        #left wall with door
        wall_list.append(Wall(590, 10, 0, 340))
        wall_list.append(Wall(260, 10, 0, 10))
    #9 
    else:
        #right wall with door
        wall_list.append(Wall(590, 600, 790, 340))
        wall_list.append(Wall(260, 10, 790, 10))

        #left wall with door
        wall_list.append(Wall(590, 10, 0, 340))
        wall_list.append(Wall(260, 10, 0, 10))

        #bottom wall with door
        wall_list.append(Wall(10, 360, 10, 590))
        wall_list.append(Wall(10, 360, 440, 590))

        #top wall with door
        wall_list.append(Wall(10, 360, 10, 0))
        wall_list.append(Wall(10, 360, 440, 0))

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

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill((blue))

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):
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
        self.image = pygame.Surface([15, 15])
        self.image.fill((white))

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
            self.rect.topleft = (10, new_y)
            self.current_room = self.current_room + 1
        elif new_y > 600:
            self.rect.topleft = (new_x, 10)
            self.current_room = self.current_room + 10
        elif new_x < 0:
            self.rect.topleft = (790, new_y)
            self.current_room = self.current_room - 1
        elif new_y < 0:
            self.rect.topleft = (new_x, 590)
            self.current_room = self.current_room - 10

player_x, player_y = 350, 250
# Create the player paddle object
player = Player(player_x, player_y, 32, 32, 5, scale_factor=3)
movingsprites = pygame.sprite.RenderPlain((player))

# This is the main function where our program begins
def main():
    score = 0
    # Call this function so the Pygame library can initialize itself
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
    # Set the title of the window
    pygame.display.set_caption('Test')
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

    while 1:
        clock.tick(40)

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

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
        screen.fill(black)
        movingsprites.draw(screen)
        walls.draw(screen)
        pygame.display.flip()

# This calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()