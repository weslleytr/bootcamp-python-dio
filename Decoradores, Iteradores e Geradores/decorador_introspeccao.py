import functools


def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print('Antes da execução da função decorada')
        funcao(*args, **kwargs)
        print('Depois da execução da função decorada')
        return funcao(*args, **kwargs)

    return envelope

@meu_decorador
def hello_world(nome):
    print(f'Olá, mundo, {nome}!')
    return nome.upper()

print(hello_world.__name__)