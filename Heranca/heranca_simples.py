class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Motor ligado")

    def __str__(self):
        return self.cor

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        self.carregado = carregado
        super().__init__(cor, placa, numero_rodas)

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} está carregado")


moto = Motocicleta("azul", "ABC-1234", 2)
print(f"Motocicleta: {moto.cor}, {moto.placa}, {moto.numero_rodas} rodas")
moto.ligar_motor()

carro = Carro("vermelho", "XYZ-5678", 4)
print(f"Carro: {carro.cor}, {carro.placa}, {carro.numero_rodas} rodas")
carro.ligar_motor()

caminhao = Caminhao("verde", "FGH-7890", 6, False)
print(f"Caminhão: {caminhao.cor}, {caminhao.placa}, {caminhao.numero_rodas} rodas")
caminhao.ligar_motor()
caminhao.esta_carregado()