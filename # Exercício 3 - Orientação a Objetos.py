# Exercício 3 - Orientação a Objetos

'''
Crie uma classe Livro que possui os atributos nome, qtdPaginas, autor e preço.
Crie os métodos getPreco para obter o valor do preco e o método setPreco para setar
um novo valor do preco.
Crie um codigo de teste

'''

class Livro:
    def __init__(self, nome, qntPaginas, autor, preco):
        self.nome = nome
        self.qntPaginas = qntPaginas
        self.autor = autor
        self.preco = preco

    def getPreco(self):
        print(f"Preço: {self.preco}")

    def setPreco(self, valor):
        self.preco = valor

livro1 = Livro("Poder do Hábito", "200", "Robert", 39.90)
livro1.setPreco(29.9)
livro1.getPreco()