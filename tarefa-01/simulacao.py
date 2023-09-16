from cliente import Cliente
from banco import Banco

# Instanciando bancos
banco_1 = Banco('Banco_1')
banco_2 = Banco('Banco_2')

# Instanciando cliente
cliente_1 = Cliente('João')
cliente_2 =  Cliente('Maria')

# Criando contas e adicionando ao cliente
banco_1.criar_conta(cliente_1, '123', 100)
banco_2.criar_conta(cliente_2, '456', 100)

print(banco_1.contas)
print(banco_2.contas)

# Realizando transferência
banco_1.transferir(cliente_1, '123', banco_2, '456', 50)

print(banco_1.contas)
print(banco_2.contas)