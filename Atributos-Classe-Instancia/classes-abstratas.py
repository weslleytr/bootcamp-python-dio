from abc import ABC, abstractmethod

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleRemotoTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")

    def desligar(self):
        print("Desligando a TV")

    @property
    def marca(self):
        print("LG")

class ControleRemotoArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o ar-condicionado")

    def desligar(self):
        print("Desligando o ar-condicionado")

    @property
    def marca(self):
        print("LG")

# Exemplo de uso das classes abstratas

controle_tv = ControleRemotoTV()
controle_tv.ligar()
controle_tv.desligar()
controle_tv_marca = controle_tv.marca

controle_ac = ControleRemotoArCondicionado()
controle_ac.ligar()
controle_ac.desligar()
controle_ac_marca = controle_ac.marca