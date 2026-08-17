class Gamer:
    def __init__(self, nome, nickname):
        self.nome = nome
        self.nick = nickname
        self.jogos_favoritos = list()

    def add_favoritos(self, jogo):
        self.jogos_favoritos.append(jogo)
        self.jogos_favoritos.sort()
        print(f"O jogo {jogo} foi adicionado a lista de favoritos com sucesso!")

    def ficha(self):
        print(f"\n----- Jogador: {self.nick} -----")
        print(f"Nome real: {self.nome}")
        print(f"Jogos favoritos: ")
        for jogo in self.jogos_favoritos:
            print(f"- {jogo}")

acc = Gamer("Joao", "joaoxz")
acc.add_favoritos("God of War")
acc.add_favoritos("The Batman")
acc.ficha()