import time
import math
import pygame

from Bullet import Bullet

class BaseGun:
    def __init__(self, screen_width, screen_height, bullets: pygame.sprite.Group, cooldown_time_in_sec = 0.5):
        """Represents a basic scatter gun with a rate of fire limiter."""
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bullets = bullets
        self.last_fire_time = time.time()
        self.cooldown_time_in_sec = cooldown_time_in_sec
    
    def fire(self, start_x, start_y, start_angle, x_vel, y_vel):
        """Fires three bullets in a small angle spread."""
        if time.time() - self.last_fire_time > self.cooldown_time_in_sec:
            for spread in range(-1, 2):
                bullet = Bullet(start_x, start_y, start_angle + spread*4, x_vel, y_vel, self.screen_width, self.screen_height)
                self.bullets.add(bullet)
            self.last_fire_time = time.time()
