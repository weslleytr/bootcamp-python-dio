class Estudante:
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"Nome: {self.nome}, Número: {self.numero}, Escola: {Estudante.escola}"
    

def get_values(*obj):
    for o in obj:
        print(f"Nome: {o.nome}, Número: {o.numero}, Escola: {Estudante.escola}")

# Criando instâncias da classe Estudante
estudante1 = Estudante("Weslley", 1)
estudante2 = Estudante("Maria", 2)

# Exibindo os atributos de cada instância
get_values(estudante1, estudante2)

Estudante.escola = "Python"  # Alterando a escola para todos os estudantes
estudante3 = Estudante("João", 3)

get_values(estudante1, estudante2, estudante3)