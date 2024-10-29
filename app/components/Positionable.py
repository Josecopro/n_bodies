from dataclasses import dataclass, field
from typing import List, Union

@dataclass
class Positionable:
    Name: str
    Position: List[Union[int, float]] = field(default_factory=lambda: [0, 0])
