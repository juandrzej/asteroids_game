import pygame


class CircleShape(pygame.sprite.Sprite):
    """Base class for game objects"""

    def __init__(self, x: int | float, y: int | float, radius: int):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: int = radius

    def draw(self, screen: pygame.Surface) -> pygame.Rect:
        # sub-classes must override
        pass

    def update(self, dt: float):
        # sub-classes must override
        pass

    def collision(self, other: pygame.sprite.Sprite) -> bool:
        distance: float = self.position.distance_to(other.position)
        radiuses: float = self.radius + other.radius
        return distance <= radiuses
