from dataclasses import dataclass
from Body import Body
from Asteroid import Asteroid
from Star import Star
from QuadTree import QuadTree



@dataclass
class Space:
    Bodies: list
    QuadTree: QuadTree

    def AddBody(self, body: Body):
        self.Bodies.append(body)
        self.QuadTree.insert(body)