# Exercício 5 - Orientação a Objetos

'''
 Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
•Um veículo tem um certo consumo de combusivel (medidos em km / litro) e
uma certa quantidade de combusivel no tanque.
•O consumo é especificado no construtor e o nível de combustivel inicial é 0.
•Forneça um método andar( ) que simule o ato de dirigir o veículo por uma
certa distância, reduzindo o nível de combustivel no tanque de gasolina. Esse
método recebe como parâmetro a distância em km.
•Forneça um método obterGasolina( ), que retorna o nível atual de
combustivel.
•Forneça um método adicionarGasolina( ), para abastecer o tanque.
•Faça um programa para testar a classe Carro. Exemplo de uso:
meuFusca = Carro(15); # 15 quilômetros por litro de combustivel.
meuFusca.adicionarGasolina(20); # abastece com 20 litros de
combustivel.
meuFusca.andar(100); # anda 100 quilômetros.
meuFusca.obterGasolina() # Imprime o combus}vel que resta no
tanque.

'''

class Carro:
    def __init__(self, consumo, nivelCombustivel = 0):
        self.consumo = consumo
        self.nivelCombustivel = nivelCombustivel

    def andar(self, distanciaKM):
        litros = distanciaKM/self.consumo
        self.nivelCombustivel -= litros
        print(f"Andando {distanciaKM} km")

    def abastecerTanque(self, litros):
        self.nivelCombustivel+=litros
        print(f"Abastecendo {litros} litros")

    def getNivelCombustivel(self):
        print(f"Nível de combustível atual: {self.nivelCombustivel} litros")


carro1 = Carro(10)
carro1.getNivelCombustivel()
carro1.abastecerTanque(50)
carro1.getNivelCombustivel()
carro1.andar(100)
carro1.getNivelCombustivel()