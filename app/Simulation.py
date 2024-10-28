import subprocess
import sys
import os
import pygame
import components.Space as Space
from components.Body import Body

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



def GetWindow():
    WindowInformation = pygame.display.Info()
    return WindowInformation.current_w, WindowInformation.current_h


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    try:
        import pygame
    except ImportError:
        print("pygame not found, installing...")
        install("pygame")

if __name__ == "__main__":
    main()

    Simulation = Space()
    bodies = [
        Body(Name= "queso", x=100, y=100, vx=0, vy=0, mass=500000),
        Body(Name ="Quesito", x=200, y=200, vx=0, vy=0, mass=50000),
        
        ]
    Simulation.StartSimulation(GetWindow()[0],GetWindow()[1],bodies, 4 )