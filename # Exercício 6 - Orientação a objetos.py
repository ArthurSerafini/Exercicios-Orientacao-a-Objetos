# Exercício 6 - Orientação a objetos

'''
Crie uma classe Aluno, que possui como atributo um nome e cpf. 
Crie outra classe chamada Equipe, que possui como atributo uma lista de participantes do tipo Aluno e outro
atributo chamado projeto.
Crie uma terceira classe chamada GerenciadorEquipes. Essa classe possui como atributo uma lista de todas as equipes
formadas. Ela deverá possuir o método criarEquipe, que recebe uma lista de alunos de uma equipe e diz se a equipe pode ser
formada ou não. 
Caso não haja nenhum aluno da equipe a ser formada em uma outra equipe com o mesmo projeto, então a equipe é criada e 
acrescentada à lista. Caso contrário é informada que a equipe não pode ser criada.

'''

class Aluno:                                                    # Criação da classe Aluno
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def verAluno(self):                                         # Esse método é necessário para que não retorne um endereço
        return f"{self.nome}, {self.cpf}"                       # de memória, e sim o nome e CPF do aluno


class Equipe:                                                  # Criação da classe Equipe
    def __init__(self, projeto, lista=[]):
        self.lista = list(lista)
        self.projeto = projeto
        
    def verEquipe(self):                                        # Esse método é necessário para que não retorne um endereço
        return f"{self.projeto}, {self.lista}"                  # de memória, e sim o projeto e a lista de alunos

class GerenciadorDeEquipes:
    def __init__(self, listaEquipes = []):
        self.listaEquipes = dict(listaEquipes)                  # Criação de um dicionário onde as chaves são o nome do projeto

    def criarEquipe(self, projeto, listaAlunos=[]):             # Criação da equipe a partir de um projeto e lista de alunos
        pessoaRepetida = False                                  # Variável para ver se tem alguma pessoa repetida
        for i in listaAlunos:                                   # Verifica se os alunos instancionada no metodo criarEquipe
            for j in self.listaEquipes.values():                # Já estão na lista de equipes
                pessoaRepetida = pessoaRepetida or i in j       # Se aluno estiver na lista de equipes, pessoaRepetida = True
        
        if pessoaRepetida == False:                             # Se pessoaRepetida = False, adiciona equipe
            self.listaEquipes[projeto] = listaAlunos
            print(f"Equipe criada")

        else:                                                   # Se pessoaRepetida = True, não cria equipe
            print(f"Equipe não pôde ser criada, um dos participantes já está em uma equipe")
        
    def listarEquipes(self):                                    # Método para mostrar equipes criadas
        print(self.listaEquipes)


# TESTES

gerenciador = GerenciadorDeEquipes()
gerenciador.criarEquipe("Matemática", [Aluno("Carlos", "444.222.111-09").verAluno(), Aluno("Sheila", "444.262.000-09").verAluno(), Aluno("Tadeu", "111.232.111-09").verAluno()])
gerenciador.criarEquipe("Português", [Aluno("Jonas", "444.222.111-09").verAluno(), Aluno("Tomas", "444.262.000-09").verAluno(), Aluno("Jeniffer", "111.232.111-09").verAluno()])
gerenciador.criarEquipe("Geografia", [Aluno("Roberta", "124.222.111-09").verAluno(), Aluno("Manoela", "434.172.000-09").verAluno(), Aluno("Sheila", "444.262.000-09").verAluno()])
gerenciador.criarEquipe("Geografia", [Aluno("Roberta", "124.222.111-09").verAluno(), Aluno("Manoela", "434.172.000-09").verAluno(), Aluno("Rosângela", "333.111.000-02").verAluno()])
gerenciador.listarEquipes()