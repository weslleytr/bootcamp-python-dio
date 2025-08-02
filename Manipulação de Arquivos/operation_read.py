arquivo = open('C:\Projetos\Bootcamp Python - DIO\Manipulação de Arquivos\example.txt', 'r')

print(arquivo.read())  # Lê todo o conteúdo do arquivo

print(arquivo.readline())  # Lê a primeira linha do arquivo

for line in arquivo:
    print(line)  # Lê linha por linha

print(arquivo.readlines())  # Lê todas as linhas e retorna uma lista

while len(linha := arquivo.readline()):
    print(linha)  # Lê linha por linha e remove espaços em branco

arquivo.close()