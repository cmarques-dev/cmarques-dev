from classes.bebida_quente import BebidaQuente

class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return "2. Mergulhando sache de ervas na agua."

    def servir(self):
        return "3. Servindo na caneca de porcelana com limao."