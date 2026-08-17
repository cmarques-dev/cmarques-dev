from classes.poligono import Poligono

class Quadrado(Poligono):
    def __init__(self, comprimento_lado):
        super().__init__(4)
        self.compri_lado = comprimento_lado

    def perimetro(self):
        return 4 * self.compri_lado

    def area(self):
        return self.compri_lado ** 2