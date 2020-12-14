""" Main file of asteroids."""
import pygame
from random import *
import sys
import time
from pygame.locals import *
from Ship import Ship
from Asteroid import Asteroid
from AsteroidEmitter import AsteroidEmitter

class AsteroidsGame:
    """Contains all the variables and methods for running the main game loop."""
    def __init__(self):
        self.FPS = 60
        self.WINDOW_RES = (640, 480)
        self.BG_COLOR = (0, 0, 0) # RGB for black
        self.MIN_SPAWN_DIST = 50 # Minimum distance from ship for asteroids to spawn (in pixels)

        pygame.init()
        self.FramePerSec = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode(self.WINDOW_RES)

    def death_screen(self):
        """Renders the death screen when a player collides with an asteroid."""
        self.DISPLAYSURF.fill((0, 255, 0))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    def random_offset_from_ship(self):
        x_offset = randint(self.MIN_SPAWN_DIST, self.WINDOW_RES[0]/2 - self.MIN_SPAWN_DIST)
        y_offset = randint(self.MIN_SPAWN_DIST, self.WINDOW_RES[1]/2 - self.MIN_SPAWN_DIST)
        x_offset = choice([x_offset, -x_offset]) + self.player_ship.x_pos
        y_offset = choice([y_offset, -y_offset]) + self.player_ship.y_pos

        return (x_offset, y_offset)

    def game_loop(self):
        """Main game loop."""
        # fixed sprites
        self.player_ship = Ship(*self.WINDOW_RES)
        self.player_ship.update()

        # Initial asteroids
        self.asteroids = pygame.sprite.Group()

        for _ in range(0, 8):
            aster_x, aster_y = self.random_offset_from_ship()

            asteroid = Asteroid(aster_x, aster_y)
            self.asteroids.add(asteroid)

        # Asteroid emitter
        emitter = AsteroidEmitter(*self.WINDOW_RES, self.asteroids, self.random_offset_from_ship)

        # main loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Update sprites
            emitter.update()
            self.player_ship.update()
            for asteroid in self.asteroids:
                asteroid.update()

            # Draw sprites
            self.DISPLAYSURF.fill(self.BG_COLOR)
            self.player_ship.draw(self.DISPLAYSURF)
            for asteroid in self.asteroids:
                asteroid.draw(self.DISPLAYSURF)

            # Detect collision between player and any asteroids
            if pygame.sprite.spritecollideany(self.player_ship, self.asteroids, pygame.sprite.collide_mask):
                self.death_screen()

            pygame.display.update()
            self.FramePerSec.tick(self.FPS)

if __name__ == '__main__':
    game = AsteroidsGame()
    game.game_loop()