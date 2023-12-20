from xmlrpc.client import ServerProxy
import re
import numpy as np
import time

lista_transferencias = [
    ('banco_0', '00', 'banco_1', '10', 50),
    ('banco_0', '00', 'banco_0', '01', 50),
    ('banco_2', '22', 'banco_1', '11', 100),
]


def simulacao(lista_transferencias: list):
    '''Executa o experimento com n_clientes, n_bancos e lista_transferencias'''

    tempos = []
    inicio_total = time.time()
    for transferencia in lista_transferencias:
        numbers = re.findall(r'\d+', transferencia[0])
        numbers = int(''.join(numbers))
        port = 8080 + numbers
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


