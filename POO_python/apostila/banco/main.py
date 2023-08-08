from conta import Conta

# Quando instanciamos um objeto e atrbuimos ele a uma variável estamos passando o 
# endereço desse obj na memória 

conta_1 = Conta('123-4', 'João', 120.0, 1000.0)
conta_2 = Conta('123-5', 'Maria', 1200.0, 1000.0)
 
"""conta_1.depositar(20.0)
conta_1.extrato()

conta_2.sacar(15)
conta_2.extrato()
"""
conta_1.transferir(conta_2, 5.0)

conta_1.extrato()
conta_2.extrato()