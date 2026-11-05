import pygame

from logger import log_state, log_event

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

from player import Player

from asteroid import Asteroid

from asteroidfield import AsteroidField

from shot import Shot

import sys

x = SCREEN_WIDTH/2
y = SCREEN_HEIGHT/2

def main():
    
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,drawable,updatable)
    

    my_player = Player(x,y)
    my_asteroid = AsteroidField()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0.0
    clock= pygame.time.Clock()

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        for i in asteroids:
            if i.collides_with(my_player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for s in shots:
                if s.collides_with(i):
                    log_event("asteroid_shot")
                    i.split()
                    s.kill()

        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
    




if __name__ == "__main__":
    main()
