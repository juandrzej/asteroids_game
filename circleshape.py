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

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
