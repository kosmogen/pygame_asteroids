import pygame
import time
from pygame.locals import *
from Asteroid import Asteroid

class AsteroidEmitter():
    """Emites an asteroid on a predefined interval."""
    def __init__(self, asteroids, game_surface, random_xy_func, max_asteroids = 5, emit_time_in_sec = 2):
        """Constructor for AsteroidEmitter class
        Arguments:
            asteroids: the particles group to add the emitted particle to
            game_surface: the main Surface to blit asteroids to
            random_xy_func: the function to generate random x and y coordinates for the new asteroid
            max_asteroids: the largest number of asteroids to maintain at a time. Optional, defaults to 5.
            emit_time_in_sec: the interval (in seconds) to emit a new particle on. Optional, defaults to 2.
        """
        self.game_surface = game_surface
        self.last_emit_time = time.time()
        self.emit_time_in_sec = emit_time_in_sec
        self.max_asteroids = max_asteroids
        self.asteroids = asteroids
        self.random_xy_func = random_xy_func
        self.asteroids_in_motion = False

    def _emit(self):
        aster_x, aster_y = self.random_xy_func()
        asteroid = Asteroid(aster_x, aster_y, self.game_surface)
        if self.asteroids_in_motion:
            asteroid.random_nudge()
        self.asteroids.add(asteroid)
        self.last_emit_time = time.time()

    def update(self):
        if time.time() - self.last_emit_time > self.emit_time_in_sec and len(self.asteroids) < self.max_asteroids:
            self._emit()