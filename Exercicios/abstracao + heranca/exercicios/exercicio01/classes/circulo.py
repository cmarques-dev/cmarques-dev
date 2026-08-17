from classes.poligono import Poligono

class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
       return 2 * 3.14 * self.raio
        
    def area(self):
        return 3.14 * pow(self.raio, 2)