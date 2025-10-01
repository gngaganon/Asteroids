import pygame

from constants import *

def main():
    # Initializing pygame
    pygame.init()
    # Creating pygame GUI Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Creating pygame Clock object
    clock = pygame.time.Clock()
    # dt: "delta time"
    dt = 0
    while True:
        # Ensures GUI window buttons work: minimize, maximize, close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        # Frame rate is set to 60 frames per second when .tick(60) is called
        # dt variable stores delta time
        dt = clock.tick(60)/1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
