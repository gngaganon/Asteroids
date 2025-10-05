import pygame

from constants import *

from player import Player

from asteroid import Asteroid

from asteroidfield import AsteroidField

def main():
    # Initializing pygame
    pygame.init()
    # Creating pygame GUI Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Creating pygame Clock object
    clock = pygame.time.Clock()
    # Creating containers
    # updatable: objects that can be updated
    # drawable: objects that can be drawn
    # asteroids contain...asteroids
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    # Setting Player class in updatable and drawable
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    # Instantiating a Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Instantiating an AsteroidField object
    asteroid_field = AsteroidField()
    # dt: "delta time"
    dt = 0

    # Game Loop
    while True:
        # Ensures GUI window buttons work: minimize, maximize, close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Dark background
        screen.fill("black")
        # Player movement
        updatable.update(dt)
        # Rendering drawable objects
        for drawing in drawable:
            drawing.draw(screen)
        # Screen flip
        pygame.display.flip()
        # Frame rate is set to 60 frames per second when .tick(60) is called
        # dt variable stores delta time
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
