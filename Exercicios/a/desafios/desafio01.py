class Funcionarios:
    def __init__(self, nome, cargo, setor):
        self.nome = nome
        self.cargo = cargo
        self.setor = setor

    def __str__(self):
        return f"Muito prazer! Meu nome e {self.nome}, atuo como {self.cargo} e faco parte do setor {self.setor}."

f1 = Funcionarios("Joao", "Auxiliar", "Comercial")
print(f1)