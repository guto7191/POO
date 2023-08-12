from conta import Conta
from cliente import Cliente

# Quando instanciamos um objeto e atrbuimos ele a uma variável estamos passando o 
# endereço desse obj na memória 

cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
cliente2 = Cliente('José', 'Azevedo', '222222222-22')
conta1 = Conta('123-4', cliente1, 1000.0)
conta2 = Conta('123-5', cliente2, 1000.0)

conta1.depositar(100.0)
conta1.sacar(50.0)
conta1.transferir(conta2, 200.0)

conta1.extrato()
conta1.historico.imprimir()

conta2.extrato()
conta2.historico.imprimir()