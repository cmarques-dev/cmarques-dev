class Livro:
    def __init__(self, nome, paginas):
        self.titulo = nome
        self.total_paginas = paginas
        self.pagina_atual = 1
        print(f"Voce abriu o livro {self.titulo} que tem {self.total_paginas}. Voce agora esta na pagina {self.pagina_atual}.")

    def avancar_pagina(self, qtd = 1):
        cont = 0
        for pg in range (0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pag {self.pagina_atual} ->")
                cont += 1
        print(f"Voce avancou {cont} paginas e agora esta na pagina {self.pagina_atual}.")
        if self.fim_do_livro():
            print(f"Voce ja chegou ao fim do livro, nao e mais possivel avancar paginas.")

    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False
        
livro1 = Livro("Gato de Botas", 20)
livro1.avancar_pagina(10)
livro1.avancar_pagina(5)
livro1.avancar_pagina(20)