# Exercício 1 - Orientação a objetos

'''
1. Classe Triangulo: Crie uma classe que modele um triangulo:

Atributos: LadoA, LadoB, LadoC
Métodos: calcular Perímetro, getMaiorLado;

Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um
triangulo. Depois, deve criar um objeto com as medidas e imprimir sua área e maior lado.'''

class Triangulo:
    def __init__(self, LadoA, LadoB, LadoC):
        self.LadoA = LadoA
        self.LadoB = LadoB
        self.LadoC = LadoC

    def calcularPerimetro(self):
        print(self.LadoA + self.LadoB + self.LadoC)
    
    def getMaiorLado(self):
        if self.LadoA == self.LadoB and self.LadoA == self.LadoC:
            print(self.LadoA)
        else:
            if self.LadoA > self.LadoB and self.LadoA > self.LadoC:
                print(self.LadoA)
            if self.LadoB > self.LadoA and self.LadoB > self.LadoC:
                print(self.LadoB)
            if self.LadoC > self.LadoA and self.LadoC > self.LadoB:
                print(self.LadoC)

cateto1 = float(input("Digite o valor do cateto 1: "))
cateto2 = float(input("Digite o valor do cateto 2: "))
cateto3 = float(input("Digite o valor do cateto 3: "))

triangulo1 = Triangulo(cateto1, cateto2, cateto3)
triangulo1.calcularPerimetro()
triangulo1.getMaiorLado()