def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('Antes da execução da função decorada')
        funcao(*args, **kwargs)
        print('Depois da execução da função decorada')

    return envelope

@meu_decorador
def hello_world(nome):
    print(f'Olá, mundo, {nome}!')

hello_world('Jonas')