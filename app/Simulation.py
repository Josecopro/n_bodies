import subprocess
import sys
import os
import pygame
from components.Space import Space
from components.Body import Body

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))




Simulation = Space()
bodies = [
    Body(Name= "queso", x=100, y=100, vx=0, vy=0, mass=500000),
    Body(Name ="Quesito", x=200, y=200, vx=0, vy=0, mass=50000),
        
    ]
Simulation.StartSimulation(800,600,bodies, 4 )
