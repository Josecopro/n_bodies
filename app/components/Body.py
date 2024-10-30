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

    def calculate_force(self, other):
        """
        Calcula la fuerza gravitacional entre este cuerpo y otro cuerpo `other`.

        :param other: Otro objeto de tipo Body
        :return: Fuerza en los ejes x e y como una tupla (fx, fy)
        """
        G = 6.67430e-11  # Constante de gravitación universal
        dx = other.Position[0] - self.Position[0]
        dy = other.Position[1] - self.Position[1]
        distance = math.sqrt(dx**2 + dy**2)

        # Evitar división por cero al calcular la fuerza
        if distance == 0:
            return (0, 0)

        # Ley de gravitación universal: F = G * (m1 * m2) / r^2
        force = G * (self.mass * other.mass) / (distance**2)

        # Descomponer la fuerza en componentes x e y
        fx = force * (dx / distance)
        fy = force * (dy / distance)

        return (fx, fy)
