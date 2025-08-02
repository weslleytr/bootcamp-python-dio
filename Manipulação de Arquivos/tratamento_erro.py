from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open('meu-arquivo.py', 'r')
except FileNotFoundError as e:
    print('Arquivo não encontrado. Verifique o caminho e o nome do arquivo.')
    print(f'Erro: {e}')
except IsADirectoryError as e:
    print('O caminho especificado é um diretório, não um arquivo.')
    print(f'Erro: {e}')
except IOError as e:
    print('Erro de entrada/saída ao tentar abrir o arquivo.')
    print(f'Erro: {e}')
except Exception as e:
    print('Ocorreu um erro inesperado.')
    print(f'Erro: {e}')


# try:
#     arquivo = open(ROOT_PATH / 'novo-diretorio')
# except IsADirectoryError as e:
#     print('O caminho especificado é um diretório, não um arquivo: {e}')