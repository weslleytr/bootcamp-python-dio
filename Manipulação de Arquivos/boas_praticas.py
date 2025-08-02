from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Manipulação de Arquivos - Boas Práticas
try:
    with open(ROOT_PATH / 'test.txt', 'r') as arquivo:
        print("Trabalhando com o arquivo:")
        print(arquivo.read())
except IOError as e:
    print('Erro de entrada/saída ao tentar abrir o arquivo.')
    print(f'Erro: {e}')

# Exemplo de escrita em arquivo
try:
    with open(ROOT_PATH / 'test.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Escrevendo no arquivo de teste.')
        print("Arquivo escrito com sucesso.")
except IOError as e:
    print('Erro de entrada/saída ao tentar escrever no arquivo.')
    print(f'Erro: {e}')

# Exemplo de leitura com codificação específica
try:
    with open(ROOT_PATH / 'test.txt', 'r', encoding='ascii') as arquivo:
        print(arquivo.read())
except IOError as e:
    print('Erro de entrada/saída ao tentar escrever no arquivo.')
    print(f'Erro: {e}')