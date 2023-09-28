import pygame
from pygame.locals import *

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)

# This class represents the bar at the bottom that the player controls
class Wall(pygame.sprite.Sprite):
 # Constructor function
 def __init__(self,height,width,x,y):
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
 def __init__(self,x,y):
     # Call the parent's constructor
     pygame.sprite.Sprite.__init__(self)

     # Set speed vector
     self.change_x=0
     self.change_y=0
  
     # Set height, width
     self.image = pygame.Surface([15, 15])
     self.image.fill((white))

     # Make our top-left corner the passed-in location.
     self.rect = self.image.get_rect()
     self.rect.topleft = [x,y]

 # Change the speed of the player
 def changespeed(self,x,y):
     self.change_x+=x
     self.change_y+=y
  
 # Find a new position for the player
 def update(self,walls):
     # Get the old position, in case we need to go back to it
     old_x=self.rect.topleft[0]
     old_y=self.rect.topleft[1]
  
     # Update position according to our speed (vector)
     new_x=old_x+self.change_x
     new_y=old_y+self.change_y
  
     # Put the player in the new spot
     self.rect.topleft = (new_x,new_y)

     # Did this update cause us to hit a wall?
     collide = pygame.sprite.spritecollide(self, walls, False)
     if collide:
         # Whoops, hit a wall. Go back to the old position
         self.rect.topleft=(old_x,old_y)
      
# This is the main function where our program begins
def main():
 score = 0
 # Call this function so the Pygame library can initialize itself
 pygame.init()

 # Create an 800x600 sized screen
 screen = pygame.display.set_mode([800, 600])
 # Set the title of the window
 pygame.display.set_caption('Test')
 # Enable this to make the mouse dissappear when over our window
 #pygame.mouse.set_visible(0)
 # This is a font we use to draw text on the screen (size 36)
 font = pygame.font.Font(None, 36)

 # Create a surface we can draw on
 background = pygame.Surface(screen.get_size())
 # Used for converting color maps and such
 background = background.convert()
 # Fill the screen with a black background
 background.fill(black)

 # Create the player paddle object
 player = Player( 50,50 )
 movingsprites = pygame.sprite.RenderPlain((player))

 # Make the walls. (height, width, x_pos, y_pos)
 wall_list=[]
 wall_list.append(Wall(600,10,0,0))
 wall_list.append(Wall(10,790,10,0))
 wall_list.append(Wall(10,790,10,590))
 wall_list.append(Wall(590,600,790,0))

 walls=pygame.sprite.RenderPlain(wall_list)

 clock = pygame.time.Clock()

 while 1:
     clock.tick(40)
  
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             return

         if event.type == KEYDOWN:
             if event.key == K_LEFT:
                 player.changespeed(-3,0)
             if event.key == K_RIGHT:
                 player.changespeed(3,0)
             if event.key == K_UP:
                 player.changespeed(0,-3)
             if event.key == K_DOWN:
                 player.changespeed(0,3)
              
         if event.type == KEYUP:
             if event.key == K_LEFT:
                 player.changespeed(3,0)
             if event.key == K_RIGHT:
                 player.changespeed(-3,0)
             if event.key == K_UP:
                 player.changespeed(0,3)
             if event.key == K_DOWN:
                 player.changespeed(0,-3)
              
     player.update(walls)
  
     pygame.draw.rect(screen,black,(0,0,800,600))
     movingsprites.draw(screen)
     walls.draw(screen)
     pygame.display.flip()
          
#this calls the 'main' function when this script is executed
main()