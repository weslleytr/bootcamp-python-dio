import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Example of writing to a CSV file
# try:
#     with open(ROOT_PATH / 'dados.csv', 'w', newline='', encoding='utf-8') as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(['Nome', 'Idade', 'Cidade'])  # Cabeçalho
#         escritor.writerow(['Alice', 30, 'São Paulo'])  # Linha de dados
#         escritor.writerow(['Bob', 25, 'Rio de Janeiro'])  # Outra linha       
# except IOError as e:
#     print(f"Erro ao criar o arquivo: {e}")

# Reading the CSV file
# try:
#     with open(ROOT_PATH / 'dados.csv', 'r', newline='', encoding='utf-8') as arquivo:
#         leitor = csv.reader(arquivo)     
#         for row in leitor:
#             print(row)
# except IOError as e:
#     print(f"Erro ao criar o arquivo: {e}")

# Example of reading a CSV file with DictReader
try:
    with open(ROOT_PATH / 'dados.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['Nome'], row['Idade'], row['Cidade'])
except IOError as e:
    print(f"Erro ao criar o arquivo: {e}")