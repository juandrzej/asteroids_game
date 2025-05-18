import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main() -> None:
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Starting game, clock, dt, screen and display
    pygame.init()
    clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0.0
    screen: pygame.surface.Surface = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )
    pygame.display.init()

    # Creating asteroids, updatable and drawable groups, starting player instance
    asteroids: pygame.sprite.Group = pygame.sprite.Group()
    updatable: pygame.sprite.Group = pygame.sprite.Group()
    drawable: pygame.sprite.Group = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Exit game if user uses exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for ast in asteroids:
            if ast.collision(player):
                print("Game over!")
                return

        # Basically screen update
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
