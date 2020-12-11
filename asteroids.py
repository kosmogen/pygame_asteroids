""" Main file of asteroids."""
import pygame
import sys
import time
from pygame.locals import *
from Ship import Ship
from Asteroid import Asteroid

def death_screen(surface):
    surface.fill((0, 255, 0))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    FPS = 60
    WINDOW_RES = (640, 480)
    BG_COLOR = (0, 0, 0) # RGB for black
    RED = (255, 0, 0)

    pygame.init()
    FramePerSec = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode(WINDOW_RES)

    # fixed sprites
    player_ship = Ship(*WINDOW_RES)
    player_ship.update()

    # Test asteroid
    asteroids = pygame.sprite.Group()
    test_asteroid = Asteroid(100, 100, 20)

    asteroids.add(test_asteroid)

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update sprites
        player_ship.update()
        for asteroid in asteroids:
            asteroid.update()

        # Draw sprites
        DISPLAYSURF.fill(BG_COLOR)
        player_ship.draw(DISPLAYSURF)
        for asteroid in asteroids:
            asteroid.draw(DISPLAYSURF)

        # Detect collision between player and any asteroids
        if pygame.sprite.spritecollideany(player_ship, asteroids):
            death_screen(DISPLAYSURF)

        pygame.display.update()
        FramePerSec.tick(FPS)