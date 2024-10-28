from dataclasses import dataclass
from components.Body import Body
#from Asteroid import Asteroid
#from Star import Star
from components.QuadTree import QuadTree
import components.Area
import pygame


@dataclass
class Space:
    Bodies: list
    QuadTree: QuadTree

    def AddBody(self, body: Body):
        self.Bodies.append(body)
        self.QuadTree.insert(body)

    def RemoveBody(self, body: Body):
        self.Bodies.remove(body)
        self.QuadTree.remove(body)

    def StartSimulation(self, WindowHeight: int, WindowWidth: int, bodies: list, capacity: int):

        # Configuración de Pygame
        pygame.init()
        width, height = WindowHeight, WindowWidth
        Area = Area(width, height, (0, 0, 0))

        # Parámetros de la simulación
        dt = 0.1   # Paso de tiempo

        # Loop principal
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Crear QuadTree y agregar los cuerpos
            quadtree = QuadTree(Area, capacity)
            for body in bodies:
                quadtree.insert(body)

            # Calcular fuerzas en cada cuerpo usando el QuadTree
            for body in bodies:
                fx_total, fy_total = 0, 0
                for other in bodies:
                    if other != body:
                        fx, fy = body.calculate_force(other)
                        fx_total += fx
                        fy_total += fy

                # Calcular aceleración y actualizar velocidad y posición del cuerpo
                ax = fx_total / body.mass
                ay = fy_total / body.mass
                body.update_velocity(ax, ay, dt)
                body.update_position(dt)

            # Dibujar el espacio y cuerpos
            Area.draw()
            for body in bodies:
                pygame.draw.circle(Area.screen, (255, 255, 255), (int(body.Position[0]), int(body.Position[1])), 3)

            # Actualizar pantalla
            Area.update()

        pygame.quit()