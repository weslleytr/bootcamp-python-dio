arquivo = open('C:\\Projetos\\Bootcamp Python - DIO\\Manipulação de Arquivos\\test.txt', 'w')

arquivo.write('Manipulando arquivos no Python\n')  # Escreve uma string no arquivo

arquivo.writelines(["\n","Escrevendo","\n", "um","\n", "novo","\n", "texto"])  # Escreve uma lista de strings

arquivo.close()