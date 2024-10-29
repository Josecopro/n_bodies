from dataclasses import dataclass, field
from typing import List, Union

@dataclass
class Vector:
    Position: Positionable

    def __post_init__(self):
        if len(self.Position) != 2:
            raise ValueError("Position debe tener exactamente dos elementos.")
        if not all(isinstance(coord, (int, float)) for coord in self.Position):
            raise TypeError("Cada elemento de Position debe ser de tipo int o float.")
        if any(isinstance(coord, bool) for coord in self.Position):
            raise TypeError("Los valores de Position no pueden ser booleanos.")

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("La suma solo se puede hacer con otro objeto Vector.")
        return Vector([a + b for a, b in zip(self.Position, other.Position)])

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("La resta solo se puede hacer con otro objeto Vector.")
        return Vector([a - b for a, b in zip(self.Position, other.Position)])

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("La multiplicación solo se puede hacer con un número (int o float).")
        if scalar == 0:
            raise ValueError("El escalar no puede ser cero en la multiplicación (resultaría en el vector cero).")
        return Vector([a * scalar for a in self.Position])

    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("La división solo se puede hacer con un número (int o float).")
        if scalar == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        return Vector([a / scalar for a in self.Position])

    def __repr__(self):
        return f"Vector(Position={self.Position})"
