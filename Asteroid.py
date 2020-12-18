import pygame
import math
from pygame.locals import *
from random import randint, choice

class Asteroid(pygame.sprite.Sprite):
    """Represents an initially static rock in space."""
    def __init__(self, x_pos, y_pos, game_surface: pygame.Surface, radius=10):
        """Constructor for Asteroid class
        Arguments:
            x_pos: the center x point to create an asteroid from
            y_pos: the cetner y point to create an asteroid from
            radius: the radius of the asteroid in pixels (Optional, defaults to 10)
        """
        super().__init__() 
        self.game_surface = game_surface
        self.radius = radius
        self.image = pygame.Surface([radius*2, radius*2])
        self.image.fill((0, 0, 0))
        pygame.draw.circle(self.image, (0, 255, 0), (radius,radius), radius)
        pygame.draw.circle(self.image, (0, 0, 0), (radius,radius), radius-4)

        self.image.set_colorkey((0, 0, 0))
        self.mask = pygame.mask.from_surface(self.image)

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_velocity = 0
        self.y_velocity = 0

        self.rect = self.image.get_rect()
        self.rect.centerx = self.x_pos
        self.rect.centery = self.y_pos

    def draw(self):
        self.game_surface.blit(self.image, self.rect)

    def update(self):
        # Update sprite position
        self.x_pos = self.x_pos + self.x_velocity
        self.y_pos = self.y_pos + self.y_velocity

        # Make sure the asteroid wraps around when it reaches the edge of the screen
        if self.x_velocity > 0 and self.x_pos > self.game_surface.get_width():
            self.x_pos = self.x_pos - self.game_surface.get_width()

        if self.x_velocity < 0 and self.x_pos + self.radius < 0:
            self.x_pos = self.x_pos + self.game_surface.get_width()

        if self.y_velocity > 0 and self.y_pos > self.game_surface.get_height():
            self.y_pos = self.y_pos - self.game_surface.get_height()

        if self.y_velocity < 0 and self.y_pos + self.radius < 0:
            self.y_pos = self.y_pos + self.game_surface.get_height()

        self.rect.centerx = self.x_pos
        self.rect.centery = self.y_pos

    def random_nudge(self):
        x_bump = randint(0, 3)
        x_bump = choice([x_bump, -x_bump])

        y_bump = randint(0, 3)
        y_bump = choice([y_bump, -y_bump])

        self.x_velocity = self.x_velocity + x_bump
        self.y_velocity = self.y_velocity + y_bump