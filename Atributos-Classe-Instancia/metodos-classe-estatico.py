class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def get_idade_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18
    

p1 = Pessoa.get_idade_data_nascimento(2001, 4, 30, "Weslley")  # Exemplo de uso

print(p1.nome)

print(Pessoa.maior_de_idade(p1.idade))  # Exemplo de uso do método estático
print(Pessoa.maior_de_idade(17))  # Exemplo de uso do método estático