class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Não posso voar!")


def plano_voo(obj):
    obj.voar()

plano_voo(Pardal())
plano_voo(Avestruz())