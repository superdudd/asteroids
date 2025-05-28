# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updateable, )
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    Shot.containers = (updateable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.collisions(player):
                sys.exit("Game over!")
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collisions(shot):
                    asteroid.kill()
                    shot.kill()
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen, "white", 2)
        
        pygame.display.flip()

        
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()