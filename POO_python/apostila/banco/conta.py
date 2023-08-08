class Conta:

    def __init__(self, numero: int, titular: str, saldo: float, limite: float) -> None:
        print("Inicializado")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def depositar(self, valor: float) -> None:
        self.saldo += valor

    def sacar(self, valor: float) -> bool:
        if self.validar_valor_de_saque(valor):
            print("Valor inválido")
        else:
            self.saldo -= valor
    
    def validar_valor_de_saque(self, valor) -> bool:
        if valor > self.saldo:
            return False
        else: 
            return True

    def extrato(self):
        print(f"número {self.numero}\nsaldo: {self.saldo}")