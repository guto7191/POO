class Conta:

    def __init__(self, numero: int, titular: str, saldo: float, limite: float) -> None:
        print("Inicializado")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def depositar(self, valor: float) -> None:
        self.saldo += valor

    def sacar(self, valor: float) -> None:
        test = self.validar_valor_de_saque(valor)
        if not(self.validar_valor_de_saque(valor)):
            print(f"Valor inválido!")
            return False
        else:
            self.saldo -= valor
            return True
    
    def validar_valor_de_saque(self, valor) -> bool:
        if valor > self.saldo:
            return False
        else: 
            return True

    def extrato(self) -> None:
        print(f"número {self.numero}\nsaldo: {self.saldo}")

    def transferir(self, destino: any, valor: float) -> bool:
        retirou = self.sacar(valor)
        if(retirou == False):
            return False
        else:
            destino.depositar(valor)
            return True
