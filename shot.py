import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    """Class to represent shoots that player can shoot to destroy asteroids."""

    def __init__(self, x: int | float, y: int | float):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
