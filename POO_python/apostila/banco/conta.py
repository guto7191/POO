from typing import Type
from historico import Historico

class Conta:

    def __init__(self, numero: int, cliente: any, saldo: float, limite: float = 1000) -> None:
        print("Inicializado")
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.historico = Historico()
        self.limite = limite
        self.data
        
    
    def depositar(self, valor: float) -> None:
        self.saldo += valor
        self.historico.transacoes.append(f"depósito de {valor}")

    def sacar(self, valor: float) -> None:
        test = self.validar_valor_de_saque(valor)
        if not(self.validar_valor_de_saque(valor)):
            print(f"Valor inválido!")
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f"saque de {valor}")
            return True
    
    def validar_valor_de_saque(self, valor) -> bool:
        if valor > self.saldo:
            return False
        else: 
            return True

    def extrato(self) -> None:
        print(f"número {self.numero}\nsaldo: {self.saldo}")
        self.historico.transacoes.append(f"Tirou o estrato - saldo de {self.saldo}")

    def transferir(self, destino: any, valor: float) -> bool:
        retirou = self.sacar(valor)
        if(retirou == False):
            return False
        else:
            destino.depositar(valor)
            self.historico.transacoes.append(f"Transferência de {valor} para {destino.numero}")
            return True
