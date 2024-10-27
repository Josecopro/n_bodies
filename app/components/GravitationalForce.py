from dataclasses import dataclass
from app.components.Body import Body

@dataclass
class GravitationalForce:
    
    GravityConstant: float
    Cutoff: float
    Dt: float
    Bodies: list[Body]

    def Calculate(self):
        pass