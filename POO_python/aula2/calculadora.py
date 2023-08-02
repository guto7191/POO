class Calculadora:
    
    def calcular(self, op, num1, num2):
        if op == '+':
            return self.__somar(num1,num2)
        elif op == '-':
            return self.__subtrair(num1,num2)
        else:
            print("Operação inválida!!")
    
    def __somar(self, num1, num2):
        return num1+num2
    
    def __subtrair(self, num1, num2):
        return num1 - num2



calculadora = Calculadora()

print(calculadora.calcular('+',5,5))
print(calculadora.calcular('-',5,5))