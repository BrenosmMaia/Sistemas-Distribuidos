from xmlrpc.client import ServerProxy
import re

lista_transferencias = [
    ('banco_0', '00', 'banco_1', '10', 50),
    ('banco_0', '00', 'banco_0', '01', 50),
    ('banco_2', '23', 'banco_1', '11', 100),
]


def simulacao(lista_transferencias: list):
    '''Executa o experimento com n_clientes, n_bancos e lista_transferencias'''
    for transferencia in lista_transferencias:
        numbers = re.findall(r'\d+', transferencia[0])
        numbers = int(''.join(numbers))
        port = 8080 + numbers
        with ServerProxy(f'http://localhost:{port}') as proxy:
            print(f"Cliente RPC criado na porta {port}")
            print(transferencia)
            contas = proxy.transferir(transferencia[0], transferencia[1], transferencia[2], transferencia[3], transferencia[4])
            print("SUCESSO")
            print("Situação das contas após a tranferência:")
            for i in contas:
                print(i)
            print("\n")
    
    print("Todas as transferencias foram executadas com sucesso")


simulacao(lista_transferencias)


