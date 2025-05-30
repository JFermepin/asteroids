import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *

def main():

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # Game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game Over!")
                exit() 
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()