from classes.bebida_quente import BebidaQuente

class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return "2. Passando vapor pressurizado pelo bico do leite."

    def servir(self):
        return "3. Servindo na xicara grande, ja com cafe."