def meu_decorador(funcao):
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

result = hello_world('Jonas')
print(result)