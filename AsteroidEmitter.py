import pygame
import time
from pygame.locals import *
from Asteroid import Asteroid

class AsteroidEmitter():
    """Emites an asteroid on a predefined interval."""
    def __init__(self, screen_width, screen_height, asteroids, random_xy_func, emit_time_in_sec = 1):
        """Constructor for AsteroidEmitter class
        Arguments:
            screen_width: the width of the surface to blit to in pixels
            screen_height: the height of the surface to blit to in pixels
            asteroids: the particles group to add the emitted particle to
            emit_time_in_sec: the interval (in seconds) to emit a new particle on. optional.
        """
        self.last_emit_time = time.time()
        self.emit_time_in_sec = emit_time_in_sec
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.asteroids = asteroids
        self.random_xy_func = random_xy_func

    def _emit(self):
        aster_x, aster_y = self.random_xy_func()
        particle = Asteroid(aster_x, aster_y)
        self.asteroids.add(particle)

    def update(self):
        if time.time() - self.last_emit_time > self.emit_time_in_sec and len(self.asteroids) < 10:
            self._emit()
            self.last_emit_time = time.time()