from classes.transporte import Transporte

class Moto(Transporte):
    frete = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)
        self.distancia = distancia

    def cal_frete(self):
        return f"R$ {Moto.frete * self.distancia:.2f}."