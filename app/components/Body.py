from dataclasses import dataclass
from Orbit import Orbit
from GravitationalForce import GravitationalForce   

@dataclass
class Body:
    Name: str
    Position: list
    Velocity: list
    Mass: float
    Orbit: Orbit
    Radius: float
    #IsinQuadTree: bool (No se si el scope de esta variable se debe manejar aqui, ustedes lo deciden)

    def UpdatePosition(self):
        pass

    def UpdateVelocity(self):
        pass

    def RemoveFromQuadTree(self): #No se si esta funcion deberia estar aqui o en QuadTree.py
        pass
