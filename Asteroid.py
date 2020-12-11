import pygame
import math
from pygame.locals import *

class Asteroid(pygame.sprite.Sprite):
    """Represents an initially static rock in space."""
    def __init__(self, x_pos, y_pos, radius):
        super().__init__() 
        self.image = pygame.Surface([radius*2, radius*2])
        self.image.fill((0, 0, 0))

        pygame.draw.circle(self.image, (0, 255, 0), (radius,radius), radius)
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, (self.x_pos, self.y_pos))