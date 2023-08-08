# Exercício 2 - Orientação a Objetos

'''
Classe Funcionário: Implemente a classe Funcionário.

Um funcionário tem um nome e um salário. 
Escreva um construtor com dois parâmetros (nome e salário) e o 
método aumentarSalario(porcentualDeAumento) que aumente o salário 
do funcionário em uma certa porcentagem. 
Exemplo de uso:
h a r r y = f u n c i o n á r i o ( " H a r r y " , 2 5 0 0 0 )
harry.aumentarSalario(10)

Faca um programa que teste o método da classe.

'''

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self, porcentagem):
        self.salario = self.salario + self.salario*(porcentagem/100)

    def getSalario(self):
        print(f"Salario: {self.salario}")

funcionario1 = Funcionario("Henry", 10000)
funcionario1.aumentarSalario(20)
funcionario1.getSalario()
