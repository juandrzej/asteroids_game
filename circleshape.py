import pygame
from typing import Self


class CircleShape(pygame.sprite.Sprite):
    """Base class for game objects"""

    def __init__(self, x: int | float, y: int | float, radius: float):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen: pygame.Surface) -> None:
        # sub-classes must override
        pass

    def update(self, dt: float) -> None:
        # sub-classes must override
        pass

    def collision(self, other: Self) -> bool:
        distance: float = self.position.distance_to(other.position)
        radiuses: float = self.radius + other.radius
        return distance <= radiuses
