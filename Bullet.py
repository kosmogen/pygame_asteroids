import pygame
import math
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):
    """Represents a bullet fired by the player's ship."""
    def __init__(self, start_x, start_y, start_angle, x_vel, y_vel, screen_width, screen_height):
        super().__init__()
        self.x_pos = start_x
        self.y_pos = start_y
        self.x_velocity = x_vel + 8 * math.cos(math.radians(start_angle))
        self.y_velocity = y_vel - 8 * math.sin(math.radians(start_angle))
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.image = pygame.surface.Surface((12, 4))
        pygame.draw.rect(self.image, (0, 255, 0), pygame.Rect(0, 0, 12, 4))
        self.display_image = pygame.transform.rotate(self.image, start_angle)
        self.mask = pygame.mask.from_surface(self.display_image)
        self.rect = self.image.get_rect()
        self.rect.centerx = start_x
        self.rect.centery = start_y

    def draw(self, surface):
        surface.blit(self.display_image, self.rect)

    def update(self):
        # Update sprite position
        self.x_pos = self.x_pos + self.x_velocity
        self.y_pos = self.y_pos + self.y_velocity

        self.rect.centerx = self.x_pos
        self.rect.centery = self.y_pos

        # Make sure the ship wraps around when it reaches the edge of the screen
        if self.x_velocity > 0 and self.x_pos > self.screen_width:
            self.kill()

        if self.x_velocity < 0 and self.x_pos + 25 < 0:
            self.kill()

        if self.y_velocity > 0 and self.y_pos > self.screen_height:
            self.kill()

        if self.y_velocity < 0 and self.y_pos + 25 < 0:
            self.kill()