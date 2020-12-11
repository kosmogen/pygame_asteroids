""" Main file of asteroids."""
import pygame
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

        # Test asteroid
        self.asteroids = pygame.sprite.Group()
        self.test_asteroid = Asteroid(100, 100, 20)

        self.asteroids.add(self.test_asteroid)

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
            if pygame.sprite.spritecollideany(self.player_ship, self.asteroids):
                self.death_screen()

            pygame.display.update()
            self.FramePerSec.tick(self.FPS)

if __name__ == '__main__':
    game = AsteroidsGame()
    game.game_loop()