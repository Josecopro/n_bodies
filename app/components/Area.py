from dataclasses import dataclass
import pygame

@dataclass
class Area:
    Width: int
    Height: int
    Color: tuple

    def __init__(self, width: int, height: int, color: tuple = (0, 0, 0)):
        self.Width = width
        self.Height = height
        self.Color = color
        self.screen = pygame.display.set_mode((self.Width, self.Height))
        self.display = pygame.display.set_caption("n-body simulation")

    def draw(self):
        self.screen.fill(self.Color)

    def update(self):
        pygame.display.flip()
