from dataclasses import dataclass

@dataclass
class GravitationalForce:
    
    GravityConstant: float
    Cutoff: float
    Dt: float
    Bodies: List[Body]

    def Calculate(self):
        pass