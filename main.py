import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main() -> None:
    # Starting game, clock, dt, screen and display
    pygame.init()
    clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0.0
    screen: pygame.surface.Surface = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )
    pygame.display.init()

    # Creating asteroids, updatable and drawable groups
    asteroids: pygame.sprite.Group = pygame.sprite.Group()
    updatable: pygame.sprite.Group = pygame.sprite.Group()
    drawable: pygame.sprite.Group = pygame.sprite.Group()
    shots: pygame.sprite.Group = pygame.sprite.Group()

    # Matching groups and starting instances
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Shot.containers = (updatable, drawable, shots)

    while True:
        # Exit game if user uses exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update objects on the screen each frame
        screen.fill("black")
        updatable.update(dt)

        # Draw all objects on the screen each frame
        for obj in drawable:
            obj.draw(screen)

        # Ending the game if player collides with any of the asteroids
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                return
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.kill()

        # Basically screen update
        pygame.display.flip()

        # Limit FPS to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
