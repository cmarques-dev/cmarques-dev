from classes.transporte import Transporte

class Caminhao(Transporte):
    frete = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)
        self.distancia = distancia

    def cal_frete (self):
        if self.distancia >= 50:
            return f"R$ {Caminhao.frete * self.distancia:.2f}."
        else:
            return "A distancia minima e de 50km."