def my_generator(numeros: list[int]):
    contador = 0
    while contador < len(numeros):
        yield numeros[contador]
        contador += 1

for i in my_generator(numeros=[0,5,7,9]):
    print(i)