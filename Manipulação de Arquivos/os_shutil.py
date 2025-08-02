import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

os.mkdir(ROOT_PATH / 'novo-diretorio')  # Cria um novo diretório

arquivo = open(ROOT_PATH / 'novo.txt', 'w')  # Cria um novo arquivo de texto

arquivo.close()  # Fecha o arquivo

os.rename(ROOT_PATH / 'novo.txt', ROOT_PATH / 'rename.txt')  # Renomeia o arquivo

os.remove(ROOT_PATH / 'rename.txt')  # Remove o arquivo renomeado

shutil.move(ROOT_PATH / 'novo.txt', ROOT_PATH / 'novo-diretorio' / 'novo.txt')  # Move o arquivo para o novo diretório
