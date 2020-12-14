""" Main file of asteroids."""
import pygame
from random import *
import sys
import time
from pygame.locals import *
from Ship import Ship
from Asteroid import Asteroid

class AsteroidsGame:
    """Contains all the variables and methods for running the main game loop."""
    def __init__(self):
        self.FPS = 60
        self.WINDOW_RES = (640, 480)
        self.BG_COLOR = (0, 0, 0) # RGB for black

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

    def game_loop(self):
        """Main game loop."""
        # fixed sprites
        self.player_ship = Ship(*self.WINDOW_RES)
        self.player_ship.update()

        # Initial asteroids
        self.asteroids = pygame.sprite.Group()

        for i in range(0, 10):
            x_offset = randint(50, 300)
            y_offset = randint(50, 200)
            x_offset = choice([x_offset, -x_offset])
            y_offset = choice([y_offset, -y_offset])

            asteroid = Asteroid(self.player_ship.x_pos + x_offset, self.player_ship.y_pos + y_offset, 10)
            self.asteroids.add(asteroid)

        # main loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Update sprites
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