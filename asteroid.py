import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    """Class for asteroid objects."""

    def __init__(self, x: int | float, y: int | float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
