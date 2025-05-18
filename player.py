import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS


class Player(CircleShape):
    """Class for player object in game.
    Appear as triangle on screen, behaves like circle on backend"""

    def __init__(self, x: int | float, y: int | float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: int = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward: pygame.Vector2 = pygame.Vector2(0, 1).rotate(self.rotation)
        right: pygame.Vector2 = (
            pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        )
        a: pygame.Vector2 = self.position + forward * self.radius
        b: pygame.Vector2 = self.position - forward * self.radius - right
        c: pygame.Vector2 = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> pygame.Rect:
        return pygame.draw.polygon(screen, "white", self.triangle(), 2)
