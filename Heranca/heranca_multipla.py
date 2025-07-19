class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass

# gato = Gato(4, "preto")
# print(gato)

ornitorrinco = Ornitorrinco(numero_patas=2,
                            cor_pelo="marrom",
                            cor_bico="azul")
print(ornitorrinco)