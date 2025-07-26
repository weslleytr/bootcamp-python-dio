def calculadora(operation):
    def soma(a,b):
        return a + b
    
    def subtracao(a,b):
        return a - b
    
    def multiplicacao(a,b):
        return a * b
    
    def divisao(a,b):
        return a / b
    
    match operation:
        case 'soma':
            return soma
        case 'subtracao':
            return subtracao
        case 'multiplicacao':
            return multiplicacao
        case 'divisao':
            return divisao
        case _:
            raise ValueError("Operação inválida")
    

print(calculadora('soma')(5, 3))
print(calculadora('subtracao')(10, 4))
print(calculadora('multiplicacao')(2, 3))
print(calculadora('divisao')(8, 2))