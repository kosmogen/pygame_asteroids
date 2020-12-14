import pygame
import math
from pygame.locals import *

class Ship(pygame.sprite.Sprite):
    """Represents the player's ship in asteroids."""
    def __init__(self, screen_width, screen_height):
        super().__init__()

        # self.image = pygame.Surface([50, 50])
        # self.image.fill((0, 0, 0))
        # self.image.set_colorkey((0, 0, 0))
        # pygame.draw.line(self.image, (0, 255, 0), (1, 1), (49, 25))
        # pygame.draw.line(self.image, (0, 255, 0), (49, 25), (1, 49))
        # pygame.draw.line(self.image, (0, 255, 0), (1, 1), (1, 49))

        self.image = pygame.image.load('player_ship.png')
        
        self.mask = pygame.mask.from_surface(self.image)

        self.x_pos = screen_width/2 - 25
        self.y_pos = screen_height/2 - 25
        self.y_velocity = 0
        self.x_velocity = 0
        self.angle = 90
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.display_image = pygame.transform.rotate(self.image, self.angle)

        self.rect = self.display_image.get_rect()
        self.rect.centerx = self.x_pos
        self.rect.centery = self.y_pos

    def draw(self, surface):
        surface.blit(self.display_image, self.rect)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        # Update velocity and atitude from keypresses
        if pressed_keys[K_UP]:
            self.y_velocity = self.y_velocity - 0.25 * math.sin(math.radians(self.angle))
            self.x_velocity = self.x_velocity + 0.25 * math.cos(math.radians(self.angle))
            pass
        if pressed_keys[K_DOWN]:
            self.y_velocity = self.y_velocity + 0.25 * math.sin(math.radians(self.angle))
            self.x_velocity = self.x_velocity - 0.25 * math.cos(math.radians(self.angle))
            pass
        if pressed_keys[K_LEFT]:
            self.angle = self.angle + 1
            self.display_image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.display_image.get_rect()
        if pressed_keys[K_RIGHT]:
            self.angle = self.angle - 1
            self.display_image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.display_image.get_rect()

        # Update sprite position
        self.x_pos = self.x_pos + self.x_velocity
        self.y_pos = self.y_pos + self.y_velocity

        # Make sure the ship wraps around when it reaches the edge of the screen
        if self.x_velocity > 0 and self.x_pos > self.screen_width:
            self.x_pos = self.x_pos - self.screen_width

        if self.x_velocity < 0 and self.x_pos + 25 < 0:
            self.x_pos = self.x_pos + self.screen_width

        if self.y_velocity > 0 and self.y_pos > self.screen_height:
            self.y_pos = self.y_pos - self.screen_height

        if self.y_velocity < 0 and self.y_pos + 25 < 0:
            self.y_pos = self.y_pos + self.screen_height

        self.rect.centerx = self.x_pos
        self.rect.centery = self.y_pos
