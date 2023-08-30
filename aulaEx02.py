class Pessoa:
    def __init__(self, name):
        self.name = name

    def cumprimentar(self):
        print(f"Olá, {self.name}!")


pessoa = Pessoa("João")
pessoa.cumprimentar()