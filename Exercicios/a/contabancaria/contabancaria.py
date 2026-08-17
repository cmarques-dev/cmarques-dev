class ContaBancaria:
     """
     Cria uma conta bancaria e permite fazer saques e depositos
     """
     def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso! Saldo atual de {self.saldo}")

     def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R$ {self.saldo:.2f} de saldo."

     def depositar(self, valor):
         self.saldo += valor
         print(f"Voce depositou R${valor:.2f} com sucesso!\nAgora voce tem R${self.saldo:.2f} de saldo total.")

     def sacar(self, valor):
         if valor > self.saldo:
             print(f"Saque de R${valor:.2f} foi negado, saldo insuficiente!")
         else:
             self.saldo -= valor
             print(f"Voce sacou R${valor:.2f} com sucesso!\nAgora voce tem R${self.saldo:.2f} de saldo total.")

c1 = ContaBancaria(1, "Gustavo", 300)
c1.depositar(500)
c1.sacar(1000)
print(c1)