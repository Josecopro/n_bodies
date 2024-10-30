from dataclasses import dataclass
from components.Orbit import Orbit
from components.GravitationalForce import GravitationalForce   
import math
from dataclasses import dataclass, field


@dataclass
class Body:
    Name: str
    Position: list # [x, y]
    Velocity: list = field(default_factory=[0.0,0.0]) # [vx, vy]
    Mass: int = 0
    #Orbit: Orbit (Tenemos que definir la implementacion de la orbita para cuando creeemos la instancia podamos usarla bien)
    Radius: float = 1
    #IsinQuadTree: bool (No se si el scope de esta variable se debe manejar aqui, ustedes lo deciden)

    def __init__(self, Name:str, x: float, y: float, vx: float, vy: float, mass: float):
        self.Name = Name
        self.Position = [x, y]
        self.Velocity = [vx, vy]
        self.mass = mass

    def update_velocity(self, ax: float, ay: float, dt: float):
        """
        Actualiza la velocidad del cuerpo en función de la aceleración y el tiempo.
        
        :param ax: Aceleración en el eje X
        :param ay: Aceleración en el eje Y
        :param dt: Paso de tiempo
        """
        self.Velocity[0] += ax * dt
        self.Velocity[1] += ay * dt

    def update_position(self, dt: float):
        """
        Actualiza la posición del cuerpo en función de la velocidad y el tiempo.
        
        :param dt: Paso de tiempo
        """
        self.Position[0] += self.Velocity[0] * dt
        self.Position[1] += self.Velocity[1] * dt

