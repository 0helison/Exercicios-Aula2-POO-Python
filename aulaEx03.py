class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    def somar(self):
        return self.valor1 + self.valor2
    def subtrair(self):
        return self.valor1 - self.valor2
    def multiplicar (self):
        return self.valor1 * self.valor2
    def dividir(self):
        return self.valor1 / self.valor2

calcular = Calculadora(20, 5)
print(f"A soma dos valores é igual a {calcular.somar()}")
print(f"A subtração dos valores é igual a {calcular.subtrair()}")
print(f"O produto dos valores é igual a {calcular.multiplicar()}")
print(f"A divisão dos valores é igual a {calcular.dividir()}")