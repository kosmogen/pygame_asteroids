import pygame
import math
from pygame.locals import *

class Asteroid(pygame.sprite.Sprite):
    """Represents an initially static rock in space."""
    def __init__(self, x_pos, y_pos, radius):
        """Constructor for Asteroid class
        Arguments:
            x_pos: the center x point to create an asteroid from
            y_pos: the cetner y point to create an asteroid from
        """
        super().__init__() 

        self.image = pygame.Surface([radius*2, radius*2])
        self.image.fill((0, 0, 0))
        pygame.draw.circle(self.image, (0, 255, 0), (radius,radius), radius)
        pygame.draw.circle(self.image, (0, 0, 0), (radius,radius), radius-4)

        self.image.set_colorkey((0, 0, 0))
        self.mask = pygame.mask.from_surface(self.image)

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.rect = self.image.get_rect()
        self.rect.centerx = self.x_pos
        self.rect.centery = self.y_pos

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pass