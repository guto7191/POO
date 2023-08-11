import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprimir(self):
        print(f"Abertura: {self.data_abertura}")
        print("Transações: ")
        
        for i in self.transacoes:
            print(f"- {i}")
    


