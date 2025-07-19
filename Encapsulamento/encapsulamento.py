class Conta:
    def __init__(self, numero_agencia, saldo=0):
        self._saldo = saldo
        self.numero_agencia = numero_agencia

    def depositar(self, valor):
        self._saldo += valor
    
    def sacar(self, valor):
        self._saldo -= valor

    def get_saldo(self):
        return self._saldo

conta = Conta("1234", 1000)
conta.depositar(500)
print(conta.get_saldo())
print(conta.numero_agencia)