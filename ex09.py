class Triangulo():
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
    def perimetro(self):
        total = l1 + l2 + l3
        print(f"O perímetro do triângulo informado é igual a {total}")

l1 = float(input("Digite o lado 1 do triângulo: "))
l2 = float(input("Digite o lado 2 do triângulo: "))
l3 = float(input("Digite o lado 3 do triângulo: "))

triangulo = Triangulo(l1, l2, l3)
triangulo.perimetro()