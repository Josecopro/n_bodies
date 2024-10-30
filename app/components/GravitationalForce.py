from dataclasses import dataclass

@dataclass
class GravitationalForce:
    
    GravityConstant: float
    Cutoff: float
    Dt: float
    Bodies: list

    def Calculate(self):
        pass