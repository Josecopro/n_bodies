from dataclasses import dataclass
from Area import Area 
from Body import Body

@dataclass
class QuadTree:
    boundary: Area
    capacity: int
    bodies: list
    divided: bool

    def __init__(self, boundary: Area, capacity: int):
        self.boundary = boundary      # El área rectangular que representa este nodo del QuadTree
        self.capacity = capacity      # Máxima cantidad de cuerpos antes de subdividir
        self.bodies = []              # Lista de cuerpos contenidos en este nodo
        self.divided = False          # Bandera para saber si se ha subdividido

    def subdivide(self):
        # Crear cuatro subregiones (NE, NW, SE, SW) dividiendo el `boundary`
        Width, Height = self.boundary.Width / 2, self.boundary.Height / 2
        x, y = self.boundary.Width, self.boundary.Height

        # Definir los límites para cada cuadrante y crear nuevos QuadTrees
        ne = Area(Width, Height, self.boundary.Color)
        nw = Area(Width, Height, self.boundary.Color)
        se = Area(Width, Height, self.boundary.Color)
        sw = Area(Width, Height, self.boundary.Color)

        # Asignar subárboles a cada cuadrante
        self.northeast = QuadTree(ne, self.capacity)
        self.northwest = QuadTree(nw, self.capacity)
        self.southeast = QuadTree(se, self.capacity)
        self.southwest = QuadTree(sw, self.capacity)

        self.divided = True

    def insert(self, body: Body):
        # Verificar si el cuerpo está dentro de los límites del nodo actual
        if not self.contains(body):
            return False

        # Agregar cuerpo si aún no ha alcanzado la capacidad máxima
        if len(self.bodies) < self.capacity:
            self.bodies.append(body)
            return True
        else:
            # Si se excede la capacidad, subdividir y redistribuir
            if not self.divided:
                self.subdivide()

            # Intentar insertar en uno de los cuadrantes
            if self.northeast.insert(body): return True
            if self.northwest.insert(body): return True
            if self.southeast.insert(body): return True
            if self.southwest.insert(body): return True

    def contains(self, body: Body):
        # Verificar si el cuerpo está dentro del área de este nodo
        x, y = body.Position[0], body.Position[1]
        return (0 <= x < self.boundary.Width) and (0 <= y < self.boundary.Height)