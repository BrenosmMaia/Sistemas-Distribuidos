from xmlrpc.client import ServerProxy
import re
import numpy as np
import time

lista_transferencias = [
    ('banco_3', '003000', 'banco_1', '001001', 100),
    ('banco_1', '001002', 'banco_5', '005005', 10),
    ('banco_2', '002004', 'banco_1', '001002', 50),
    ('banco_4', '004002', 'banco_0', '000000', 40),
    ('banco_0', '000004', 'banco_1', '001005', 70),
    ('banco_0', '000002', 'banco_2', '002002', 10),
    ('banco_3', '003003', 'banco_0', '000000', 10),
    ('banco_0', '000002', 'banco_0', '000000', 30),
    ('banco_3', '003005', 'banco_1', '001003', 30),
    ('banco_2', '002003', 'banco_4', '004001', 70),
    ('banco_3', '003002', 'banco_4', '004001', 40),
    ('banco_4', '004002', 'banco_0', '000001', 10),
    ('banco_0', '000003', 'banco_1', '001002', 90),
    ('banco_3', '003000', 'banco_2', '002003', 20),
    ('banco_5', '005005', 'banco_3', '003004', 70),
    ('banco_3', '003002', 'banco_2', '002005', 10),
    ('banco_0', '000003', 'banco_3', '003005', 20),
    ('banco_3', '003005', 'banco_4', '004002', 70),
    ('banco_4', '004003', 'banco_4', '004000', 90),
    ('banco_4', '004005', 'banco_2', '002001', 100)
]

def simulacao(lista_transferencias: list):
    '''Executa o experimento com n_clientes, n_bancos e lista_transferencias'''

    tempos = []
    inicio_total = time.time()
    for transferencia in lista_transferencias:
        numbers = re.findall(r'\d+', transferencia[0])
        numbers = int(''.join(numbers))
        port = 8000 + numbers
        with ServerProxy(f'http://localhost:{port}') as proxy:
            print(f"Cliente RPC criado na porta {port}")
            print(transferencia)
            inicio = time.time()
            contas = proxy.transferir(transferencia[0], transferencia[1], transferencia[2], transferencia[3], transferencia[4])
            fim = time.time()
            tempos.append(fim - inicio)
            print("SUCESSO")
            #print("Situação das contas após a tranferência:")
            #for i in contas:
            #    print(i)
            print("\n")

    fim_total = time.time()
    tempo_total = fim_total - inicio_total
    
    saldo_final = sum(valor['saldo'] for conta in contas for valor in conta.values())
    saldo_inicial = sum(len(conta) for conta in contas)*100 #assume que o valor inicial das contas é 100

    if np.isclose(saldo_final, saldo_inicial):
        print("Todas as transferencias foram executadas com sucesso")
    else:
        print("Erro: Soma do saldo das contas final não é igual ao inicial")

    tempo_medio_por_operacao = sum(tempos) / len(tempos)
    throughput = len(tempos) / tempo_total

    print(f"Tempo médio por operação: {round(tempo_medio_por_operacao, 4)} segundos")
    print(f"Throughput: {round(throughput, 4)} operações por segundo")


simulacao(lista_transferencias)


