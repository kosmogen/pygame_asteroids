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
        self.FPS = 30
        self.WINDOW_RES = (640, 480)
        self.BG_COLOR = (0, 0, 0) # RGB for black
        self.MIN_SPAWN_DIST = 50 # Minimum distance from ship for asteroids to spawn (in pixels)
        self.CURRENT_STATE = 'start_game'

        pygame.init()
        self.FramePerSec = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode(self.WINDOW_RES)
        pygame.display.set_caption('Asteroids')
        self.TITLE_FONT = pygame.font.SysFont('FreeMono', 20, bold=True)

    def random_offset_from_ship(self):
        x_offset = randint(self.MIN_SPAWN_DIST, self.WINDOW_RES[0]/2 - self.MIN_SPAWN_DIST)
        y_offset = randint(self.MIN_SPAWN_DIST, self.WINDOW_RES[1]/2 - self.MIN_SPAWN_DIST)
        x_offset = choice([x_offset, -x_offset]) + self.player_ship.x_pos
        y_offset = choice([y_offset, -y_offset]) + self.player_ship.y_pos

        return (x_offset, y_offset)

    def tick(self) -> bool:
        """Processes one round of updates and drawing for existing sprites.

        Returns:
            True if a collision occurs between the player ship and any asteroids, otherwise False.
        """
        # Handle quit event so players aren't trapped forever
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update sprites
        self.player_ship.update()
        for bullet in self.bullets:
            bullet.update()
        for asteroid in self.asteroids:
            asteroid.update()
        for emitter in self.asteroid_emitters:
            emitter.update()

        # Draw sprites
        self.DISPLAYSURF.fill(self.BG_COLOR)
        self.player_ship.draw(self.DISPLAYSURF)
        for asteroid in self.asteroids:
            asteroid.draw(self.DISPLAYSURF)
        for bullet in self.bullets:
            bullet.draw(self.DISPLAYSURF)

        pygame.display.update()
        self.FramePerSec.tick(self.FPS)

        # Detect collisions between bullets and asteroids and remove colliding sprites
        pygame.sprite.groupcollide(self.bullets, self.asteroids, True, True, pygame.sprite.collide_mask)

        # Detect collision between player and any asteroids
        if pygame.sprite.spritecollideany(self.player_ship, self.asteroids, pygame.sprite.collide_mask):
            return True
        
        return False

    #region Game States
    def start_game(self) -> str:
        """Resets the game field and draws the initial game back at level 1."""
        # Initial empty group for bullets
        self.bullets = pygame.sprite.Group()

        # Player ship
        self.player_ship = Ship(*self.WINDOW_RES, self.bullets)
        self.player_ship.update()

        # Initial asteroids
        self.asteroids = pygame.sprite.Group()
        self.asteroid_emitters = []

        for _ in range(0, 8):
            aster_x, aster_y = self.random_offset_from_ship()

            asteroid = Asteroid(aster_x, aster_y)
            self.asteroids.add(asteroid)

        # Initial asteroid emitter
        emitter = AsteroidEmitter(*self.WINDOW_RES, self.asteroids, self.random_offset_from_ship)
        self.asteroid_emitters.append(emitter)

        return 'level_1'

    def level_1(self) -> str:
        """Animates the first difficulty level of the game."""

        hit_asteroid = False

        while not hit_asteroid:
            hit_asteroid = self.tick()

        return 'death_screen'

    def death_screen(self) -> str:
        """Renders the death screen when a player collides with an asteroid."""
        self.DISPLAYSURF.fill((0, 255, 0))
        pygame.display.update()
        text = self.TITLE_FONT.render('Game Over', True, (0, 0, 0))
        textRect = text.get_rect().center = (0, 0)
        self.DISPLAYSURF.blit(text, textRect)

        return 'wait'

    def wait(self) -> str:
        """Do nothing state."""
        return 'wait'
    #endregion

    def game_loop(self):
        """Main game loop."""
        while True:
            current_func = getattr(self, str(self.CURRENT_STATE))
            self.CURRENT_STATE = current_func()
            

if __name__ == '__main__':
    game = AsteroidsGame()
    game.game_loop()