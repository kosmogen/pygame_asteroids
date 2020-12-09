import pygame
from pygame.locals import *

class Ship(pygame.sprite.Sprite):
    """Represents the player's ship in asteroids."""
    def __init__(self, screen_width, screen_height):
        super().__init__() 
        self.image = pygame.Surface([50, 50])
        self.image.fill((0, 0, 0))
        pygame.draw.line(self.image, (0, 255, 0), (0, 50), (25, 0))
        pygame.draw.line(self.image, (0, 255, 0), (25, 0), (50, 50))
        pygame.draw.line(self.image, (0, 255, 0), (49, 49), (0, 49))
        self.rect = self.image.get_rect()
        self.rect.move_ip(screen_width/2, screen_height/2)
        self.y_velocity = 0
        self.x_velocity = 0
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, surface):
        surface.blit(self.image, self.rect) 

    def update_keys(self):
        pressed_keys = pygame.key.get_pressed()

        # Update velocity and atitude from keypresses
        if pressed_keys[K_UP]:
            self.y_velocity = self.y_velocity - 0.5
        if pressed_keys[K_DOWN]:
            self.y_velocity = self.y_velocity + 0.5
        if pressed_keys[K_LEFT]:
            self.x_velocity = self.x_velocity - 0.5
        if pressed_keys[K_RIGHT]:
            self.x_velocity = self.x_velocity + 0.5

    def update_sprite(self):
        # Update sprite position
        self.rect.move_ip(self.x_velocity, self.y_velocity)

        # Make sure the ship wraps around when it reaches the edge of the screen
        if self.x_velocity > 0 and self.rect.left > self.screen_width:
            self.rect.move_ip(-self.screen_width, 0)

        if self.x_velocity < 0 and self.rect.right < 0:
            self.rect.move_ip(self.screen_width, 0)

        if self.y_velocity > 0 and self.rect.bottom > self.screen_height:
            self.rect.move_ip(0, -self.screen_width)

        if self.y_velocity < 0 and self.rect.top < 0:
            self.rect.move_ip(0, self.screen_width)
