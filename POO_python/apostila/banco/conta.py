from typing import Type
from historico import Historico
from datetime import datetime

class Conta:

    def __init__(self, numero: int, cliente: any, saldo: float, limite: float = 1000) -> None:
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.historico = Historico()
        self.limite = limite
        self.data = datetime.now()
        
    def registrar_no_historico(self, tipo_de_registro: int, valor: float, destino = None):
        if tipo_de_registro == 1:
            var = datetime.now()
            self.historico.transacoes.append(f"Depósito de {valor} : {var}")
        elif tipo_de_registro == 2:
            var = datetime.now()
            self.historico.transacoes.append(f"Saque de {valor} : {var}")
        elif tipo_de_registro == 3:
            var = datetime.now()
            self.historico.transacoes.append(f"Transferência de {valor} para {destino} : {var}")
        elif tipo_de_registro == 4:
            var = datetime.now()
            self.historico.transacoes.append(f"Tirou o estrato - saldo de {valor}")


    def depositar(self, valor: float) -> None:
        self.saldo += valor
        self.registrar_no_historico(1, valor)

    def sacar(self, valor: float) -> None:
        test = self.validar_valor_de_saque(valor)
        if not(self.validar_valor_de_saque(valor)):
            print(f"Valor inválido!")
            return False
        else:
            self.saldo -= valor
            self.registrar_no_historico(2, valor)
            return True
    
    def validar_valor_de_saque(self, valor) -> bool:
        if valor > self.saldo:
            return False
        else: 
            return True

    def extrato(self) -> None:
        print(f"número {self.numero}\nsaldo: {self.saldo}")
        self.registrar_no_historico(4, self.saldo)

    def transferir(self, destino: any, valor: float) -> bool:
        retirou = self.sacar(valor)
        if(retirou == False):
            return False
        else:
            destino.depositar(valor)
            self.registrar_no_historico(3, valor, destino.numero)
            return True
