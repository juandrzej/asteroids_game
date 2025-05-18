import pygame
import random
from typing import Self
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    """Class for asteroid objects."""

    def __init__(self, x: int | float, y: int | float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_radius: float = self.radius - ASTEROID_MIN_RADIUS
        asteroid1: Asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2: Asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        angle: float = random.uniform(20, 50)
        asteroid1.velocity = self.velocity.rotate(angle) * 1.2
        asteroid2.velocity = self.velocity.rotate(-angle) * 1.2
