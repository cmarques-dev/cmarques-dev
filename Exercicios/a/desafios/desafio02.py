class Produtos:
    def __init__(self, nome, preco):
        self.produto = nome
        self.preco = preco
        print(f"O produto {self.produto} de preco {self.preco} foi cadastrado com sucesso!")

    def etiqueta(self):
        print("*"*50)
        print(f"\nProduto: {self.produto}")
        print(f"Valor: R${self.preco:.2f}\n")
        print("*"*50)

p1 = Produtos("Guarda-Chuva", 50)
p1.etiqueta()