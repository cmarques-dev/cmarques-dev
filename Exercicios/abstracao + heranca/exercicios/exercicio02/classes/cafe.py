from classes.bebida_quente import BebidaQuente

class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return "2. Coando o cafe com a agua."

    def servir(self):
        return "3. Servindo cafe na xicara pequena."