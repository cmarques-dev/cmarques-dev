from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.lados = qtd_lados

        @abstractmethod
        def perimetro():
            pass

        @abstractmethod
        def area():
            pass