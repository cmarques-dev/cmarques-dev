from classes.transporte import Transporte

class Drone(Transporte):
    frete = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)
        self.distancia = distancia

    def cal_frete(self):
        if self.distancia <= 10:
            return f"R$ {Drone.frete * self.distancia:.2f}."
        else:
            return "A distancia maxima e de 10km."