# Exercício 4 - Orientação a Objetos

'''
Implemente uma classe Aluno, que deve ter os seguintes atributos: nome, curso, tempoSemDormir (em horas). 
Essa classe deverá ter os seguintes métodos:
– estudar (que recebe como parâmetro a qtd de horas de estudo e acrescenta tempoSemDormir)
– Dormir (que recebe como parâmetro a qtd de horas de sono e reduz tempoSemDormir)
Crie um código de teste da classe, criando um objeto da classe aluno e usando os métodos estudar e dormir.
Ao final imprima quanto tempo o aluno está sem dormir

'''

class Aluno:
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    def estudar(self, horas):
        self.tempoSemDormir-=horas

    def dormir(self, horas):
        self.tempoSemDormir+=horas

    def getTempoSemDormir(self):
        print(f"Tempo sem dormir {self.tempoSemDormir} horas")


aluno1 = Aluno("Rogério", "Informática", 12)
aluno1.estudar(2)
aluno1.getTempoSemDormir()
aluno1.dormir(4)
aluno1.getTempoSemDormir()