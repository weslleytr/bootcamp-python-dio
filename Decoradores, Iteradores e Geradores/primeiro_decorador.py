def meu_decorador(funcao):
    def envelope():
        print('Antes da execução da função decorada')
        funcao()
        print('Depois da execução da função decorada')

    return envelope

def hello_world():
    print('Olá, mundo!')

meu_decorador(hello_world)()