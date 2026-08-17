from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

    def ferver(self):
        return "1. O liquido esta a 100 graus, esta fervido."

    def preparar(self):
        print("Iniciando o preparo...\n")
        print(self.ferver())
        print(self.misturar())
        print(self.servir())
        print("\nBebida pronta!")