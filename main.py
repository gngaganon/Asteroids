import pygame

from constants import *

from player import Player

def main():
    # Initializing pygame
    pygame.init()
    # Creating pygame GUI Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Creating pygame Clock object
    clock = pygame.time.Clock()
    # Instantiating a Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
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
        # Player rotation (a and d keys)
        player.update(dt)
        # Rendering player
        player.draw(screen)
        # Screen flip
        pygame.display.flip()
        # Frame rate is set to 60 frames per second when .tick(60) is called
        # dt variable stores delta time
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
