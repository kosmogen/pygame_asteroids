""" Main file of asteroids."""
import pygame
from pygame.locals import *
from random import *
import sys
import time
import logging

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
        self.STATE_CHANGE_TIME = time.time()
        self.LEVEL_TIMER_IN_SEC = 10

        pygame.init()
        self.FramePerSec = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode(self.WINDOW_RES)
        pygame.display.set_caption('Asteroids')
        self.TITLE_FONT = pygame.font.SysFont('FreeMono', 20, bold=True)
        logging.basicConfig(filename='asteroids.log', level=logging.INFO)

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
            asteroid.draw()
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

        for _ in range(0, 10):
            aster_x, aster_y = self.random_offset_from_ship()

            asteroid = Asteroid(aster_x, aster_y, self.DISPLAYSURF)
            self.asteroids.add(asteroid)

        # Initial asteroid emitter
        emitter = AsteroidEmitter(self.asteroids, self.DISPLAYSURF, self.random_offset_from_ship)
        self.asteroid_emitters.append(emitter)

        return 'level_1'

    def level_1(self) -> str:
        """Animates the first difficulty level of the game."""

        hit_asteroid = False

        while not hit_asteroid and time.time() - self.STATE_CHANGE_TIME < self.LEVEL_TIMER_IN_SEC:
            hit_asteroid = self.tick()

        return 'death_screen' if hit_asteroid else 'level_2'

    def level_2(self) -> str:
        """Animates the second difficulty level of the game."""

        already_in_motion = False
        for emitter in self.asteroid_emitters:
            already_in_motion = already_in_motion or emitter.asteroids_in_motion
            emitter.asteroids_in_motion = True
        
        if not already_in_motion:
            for asteroid in self.asteroids:
                asteroid.random_nudge()

        hit_asteroid = False

        while not hit_asteroid and time.time() - self.STATE_CHANGE_TIME < self.LEVEL_TIMER_IN_SEC:
            hit_asteroid = self.tick()

        return 'death_screen' if hit_asteroid else 'level_2'

    def death_screen(self) -> str:
        """Renders the death screen when a player collides with an asteroid."""
        pygame.draw.rect(self.DISPLAYSURF, (0, 255, 0), pygame.Rect(self.WINDOW_RES[0]/2 - 110, 
                                                                    self.WINDOW_RES[1] - 40, 180, 40))
        pygame.draw.rect(self.DISPLAYSURF, (0, 0, 0), pygame.Rect(self.WINDOW_RES[0]/2 - 106, 
                                                                    self.WINDOW_RES[1] - 36, 172, 32))
        text = self.TITLE_FONT.render('Game Over', True, (0, 255, 0))
        textRect = text.get_rect().center = (self.WINDOW_RES[0]/2 - 70, self.WINDOW_RES[1] - 30)
        self.DISPLAYSURF.blit(text, textRect)
        pygame.display.update()

        return 'wait'

    def wait(self) -> str:
        """Do nothing state."""
        return 'wait'
    #endregion

    def game_loop(self):
        """Main game loop."""
        logging.info('Initial state: %s', self.CURRENT_STATE)

        while True:
            current_func = getattr(self, str(self.CURRENT_STATE))
            next_state = current_func()

            if self.CURRENT_STATE != next_state:
                logging.info('Changing from state %s to state %s', self.CURRENT_STATE, next_state)
                self.STATE_CHANGE_TIME = time.time()
                self.CURRENT_STATE = next_state
            
if __name__ == '__main__':
    game = AsteroidsGame()
    game.game_loop()