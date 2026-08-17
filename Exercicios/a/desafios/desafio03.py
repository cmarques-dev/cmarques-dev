class Churrasco:
    def __init__(self, titulo, pessoas):
        self.titulo = titulo
        self.qtd_pessoas = pessoas

    def analisar(self):
        qtd_carne = self.qtd_pessoas * 0.4
        total = 82.40 * qtd_carne
        custo_individual = total / self.qtd_pessoas
        print(f"Analisando o {self.titulo}, possui {self.qtd_pessoas} participantes.\nCada participante comera 0.4kg de carne e 1kg custa R$82.40.\nO recomendado e comprar {qtd_carne}kg de carne.\nO custo total sera de R${total:.2f}\nO custo individual sera de R${custo_individual:.2f}.")

churras = Churrasco("Da galera", 15)
churras.analisar()