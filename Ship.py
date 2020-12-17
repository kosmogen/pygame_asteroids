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

        self.image = pygame.surface.Surface((8, 12))
        pygame.draw.rect(self.image, (0, 255, 0), pygame.Rect(0, 0, 8, 12))
        pygame.image = pygame.transform.rotate(self.image, start_angle)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = start_x
        self.rect.centery = start_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

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

class Ship(pygame.sprite.Sprite):
    """Represents the player's ship in asteroids."""
    def __init__(self, screen_width, screen_height, bullets_group: pygame.sprite.Group):
        """Constructor for Model class.
        Arguments:
            screen_width: the width of the surface to blit to in pixels
            screen_height: the height of the surface to blit to in pixels
        """
        super().__init__()

        self.bullets_group = bullets_group
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
            self.y_velocity = self.y_velocity - 0.33 * math.sin(math.radians(self.angle))
            self.x_velocity = self.x_velocity + 0.33 * math.cos(math.radians(self.angle))
            pass
        if pressed_keys[K_DOWN]:
            self.y_velocity = self.y_velocity + 0.33 * math.sin(math.radians(self.angle))
            self.x_velocity = self.x_velocity - 0.33 * math.cos(math.radians(self.angle))
            pass
        if pressed_keys[K_LEFT]:
            self.angle = self.angle + 4
            self.display_image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.display_image.get_rect()
        if pressed_keys[K_RIGHT]:
            self.angle = self.angle - 4
            self.display_image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.display_image.get_rect()
        if pressed_keys[K_SPACE]:
            bullet = Bullet(self.x_pos, self.y_pos, self.angle, self.x_velocity, self.y_velocity, 
                            self.screen_width, self.screen_height)
            self.bullets_group.add(bullet)

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
