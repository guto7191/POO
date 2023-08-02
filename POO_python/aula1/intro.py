class MinhaClasse:

    def __init__(self, atributo):
        self.atributo = atributo 

    def metodo(self):
        print('Teste_1')

    def metodo2(self, num, mult):
        print(f"valor  = {num*mult}")

    def print_atributo(self):
        print(self.atributo)

frase = "Teste atributo" 

obj = MinhaClasse(frase)

obj.metodo()
obj.metodo2(4,5)
obj.print_atributo()