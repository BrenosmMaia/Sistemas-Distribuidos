from xmlrpc.client import ServerProxy

# Cria o cliente RPC
with ServerProxy('http://localhost:8080') as proxy:
    print("Cliente RPC criado")
    # Realizando transferência
    contas = proxy.transferir('Maria', '456', 'Banco_1', '123', 50)
    print("SUCESSO")
    print("Situação das contas após a tranferência:\n")
    print(contas)