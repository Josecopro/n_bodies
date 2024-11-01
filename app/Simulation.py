import subprocess
import sys
import os
import pygame
from components.Space import Space
from components.Body import Body

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


pygame.init()

WindowDimensions = pygame.display.Info()


pygame.quit()

print(WindowDimensions.current_w, WindowDimensions.current_h)

Simulation = Space()
bodies = [
    Body(Name= "queso", x=100, y=100, vx=0, vy=0, mass=500000),
    Body(Name ="Quesito", x=200, y=200, vx=0, vy=0, mass=50000),
        
    ]
Simulation.StartSimulation( WindowDimensions.current_w, WindowDimensions.current_h,   bodies, 4 )

