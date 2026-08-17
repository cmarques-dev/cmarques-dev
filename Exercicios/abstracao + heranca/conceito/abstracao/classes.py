from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod #Informa que todas as subclasses tenham essa funcao de forma obrigatoria, entratanto nao define a forma de fazer,
    # cada subclasse tera sua forma de fazer.
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O aluno {self.nome} fez matricula.")

    def estudar(self):
        print(f"O aluno {self.nome} esta estudando na turma {self.turma}.")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"O funcionario(a) {self.nome} bateu ponto.")

    def estudar(self):
        print(f"O funcionario {self.nome} esta estudando sobre cargo {self.cargo}.")

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O Professor {self.nome} deu aula.")

    def estudar(self):
        print(f"O prof. {self.nome} esta estudando sobre {self.especialidade}.")