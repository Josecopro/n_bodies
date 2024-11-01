from dataclasses import dataclass
from components.Area import Area 
from components.Body import Body


class QuadTree:
    def __init__(self, boundary: Area, capacity: int):
        self.boundary = boundary
        self.capacity = capacity
        self.bodies = []
        self.divided = False
        self.center_of_mass = Vector([0, 0])
        self.total_mass = 0.0

    def subdivide(self):
        width, height = self.boundary.Width / 2, self.boundary.Height / 2
        self.northeast = QuadTree(Area(width, height), self.capacity)
        self.northwest = QuadTree(Area(width, height), self.capacity)
        self.southeast = QuadTree(Area(width, height), self.capacity)
        self.southwest = QuadTree(Area(width, height), self.capacity)
        self.divided = True

    def insert(self, body: Body):
        if not self.contains(body):
            return False

        if len(self.bodies) < self.capacity:
            self.bodies.append(body)
            return True
        else:
            if not self.divided:
                self.subdivide()

            if self.northeast.insert(body): return True
            if self.northwest.insert(body): return True
            if self.southeast.insert(body): return True
            if self.southwest.insert(body): return True

    def contains(self, body: Body):
        x, y = body.Position[0], body.Position[1]
        return (0 <= x < self.boundary.Width) and (0 <= y < self.boundary.Height)

    def CalculateCom(self):
        total_mass = 0
        com_position = Vector([0, 0])

        if not self.divided:
            for body in self.bodies:
                total_mass += body.Mass
                com_position += body.Position * body.Mass

            if total_mass > 0:
                com_position /= total_mass
        else:
            for child in [self.northeast, self.northwest, self.southeast, self.southwest]:
                if child and child.bodies:
                    mass, pos = child.CalculateCom()
                    total_mass += mass
                    com_position += pos * mass

            if total_mass > 0:
                com_position /= total_mass

        return total_mass, com_position
