import pygame
import sys

pygame.init()

# Display screen resolution
display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


# Define Player
class Player:
    def __init__(self, x, y, w, h, vel, scale_factor=3):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = vel
        self.scale_factor = scale_factor

        # Load the sprite sheet
        self.sprite_sheet = pygame.image.load("32MCsprite.png")
        self.sprite_width = 32  # Set sprite width
        self.sprite_height = 32  # Set sprite height
        self.sprite_positions = [(0, 0), (32, 0), (64, 0)]
        self.current_sprite = 0

        # Animation timer
        self.animation_timer = 0
        self.animation_speed = 10  # Adjust this value to control animation speed

        # Add a visibility flag
        self.visible = True

        # Track the state of the 'h' key
        self.h_key_pressed = False

        # Track the state of the 'j' key
        self.j_key_pressed = False

        # Grid settings
        self.grid_spacing = 32  # Adjust this value to control the spacing between grid lines
        self.grid_color = (200, 200, 200)  # Brighter color for the grid lines
        self.show_grid = True  # Flag to toggle grid visibility

    def move(self, keys):
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.vel
        if keys[pygame.K_d] and self.x < 800 - self.w * self.scale_factor:
            self.x += self.vel
        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.vel
        if keys[pygame.K_s] and self.y < 600 - self.h * self.scale_factor:
            self.y += self.vel

    def animate(self, keys):
        # Increment the animation timer
        self.animation_timer += 1

        # Change sprite every animation_speed frames
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0

            if any(keys):  # Check if any movement key is pressed
                self.current_sprite += 1
                if self.current_sprite >= len(self.sprite_positions):
                    self.current_sprite = 0
            else:
                # Reset to the first sprite when idle
                self.current_sprite = 0

    def toggle_visibility(self):
        # Toggle the visibility flag when 'h' key is pressed (not held)
        if not self.h_key_pressed:
            self.visible = not self.visible
            self.h_key_pressed = True

    def toggle_grid(self):
        # Toggle the grid visibility when 'j' key is pressed (not held)
        if not self.j_key_pressed:
            self.show_grid = not self.show_grid
            self.j_key_pressed = True

    def main(self, display):
        if self.visible:
            # Get the current sprite's position
            sprite_x, sprite_y = self.sprite_positions[self.current_sprite]

            # Calculate the scaled size
            scaled_width = self.sprite_width * self.scale_factor
            scaled_height = self.sprite_height * self.scale_factor

            # Draw the scaled sprite over the player character directly on the display
            display.blit(pygame.transform.scale(
                self.sprite_sheet.subsurface((sprite_x, sprite_y, self.sprite_width, self.sprite_height)),
                (scaled_width, scaled_height)), (self.x, self.y))


# Adjust the screen resolution and player's starting position
screen_width, screen_height = 800, 600
player_x, player_y = screen_width // 2, screen_height // 2

# Change vel to change Player speed
player = Player(player_x, player_y, 32, 32, 5, scale_factor=3)

while True:
    display.fill((0, 128, 0))  # Set the background color to green

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    player.move(keys)

    if keys[pygame.K_h]:  # Press 'h' key to toggle the visibility of the red square
        player.toggle_visibility()
    else:
        player.h_key_pressed = False

    if keys[pygame.K_j]:  # Press 'j' key to toggle grid visibility
        player.toggle_grid()
    else:
        player.j_key_pressed = False

    player.animate(keys)
    player.main(display)

    if player.show_grid:
        # Draw grid lines
        for x in range(0, screen_width, player.grid_spacing):
            pygame.draw.line(display, player.grid_color, (x, 0), (x, screen_height))
        for y in range(0, screen_height, player.grid_spacing):
            pygame.draw.line(display, player.grid_color, (0, y), (screen_width, y))

    # Frame rate
    clock.tick(60)
    pygame.display.update()
