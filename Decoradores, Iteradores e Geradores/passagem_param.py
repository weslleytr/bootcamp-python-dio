def mensagem(nome):
    print ('executando nome')
    return f'Olá {nome}'

def mensage_longa(nome):
    print ('executando nome longo')
    return f'Olá {nome}, tudo bem com você?'

def executar(funcao, nome):
    print('Executando a função...')
    return funcao(nome)


print(executar(mensagem,'João'))
print(executar(mensage_longa,'João'))