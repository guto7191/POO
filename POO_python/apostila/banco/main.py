from conta import Conta

conta = Conta('123-4', 'João', 120.0, 1000.0)

conta.depositar(20.0)
conta.extrato()

conta.sacar(15)
conta.extrato()
