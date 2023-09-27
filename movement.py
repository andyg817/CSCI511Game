import pygame
import sys

pygame.init()

# display screen res
display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# define Player
class Player:
    def __init__(self, x, y, w, h, vel):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = vel

    def move(self, keys):
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.vel
        if keys[pygame.K_d] and self.x < 800 - self.w:
            self.x += self.vel
        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.vel
        if keys[pygame.K_s] and self.y < 600 - self.h:
            self.y += self.vel

    def main(self, display):
        pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.w, self.h))

# change vel to change Player speed
player = Player(400, 300, 32, 32, 10)

while True:
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    player.move(keys)

    player.main(display)

# frame rate
    clock.tick(60)
    pygame.display.update()
