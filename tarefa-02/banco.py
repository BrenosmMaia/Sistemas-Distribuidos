from cliente import Cliente
from xmlrpc.server import SimpleXMLRPCServer
import threading
from xmlrpc.client import ServerProxy
import re

class Banco:
    def __init__(self, nome: str):
        """Inicializa um objeto Banco com um nome e um dicionário vazio de contas."""
        self.nome = nome
        self.contas = {}
        self.lock = threading.Lock()

    def criar_cliente(self, nome: str):
        """Cria um novo cliente e retorna o objeto Cliente."""
        cliente = Cliente(nome)
        return cliente
    
    def criar_conta(self, cliente: str, numero_conta: str, saldo_inicial: float = 0):
        """Cria uma nova conta no banco com um saldo inicial e adiciona a conta ao cliente."""
        self.contas[numero_conta] = {'cliente': cliente, 'saldo': saldo_inicial}

    def depositar(self, numero_conta: str, valor: float):
        """Deposita um valor em uma conta."""
        if numero_conta in self.contas:
            self.contas[numero_conta]['saldo'] += valor
        else:
            raise ValueError("Conta não encontrada")
        
    def subtrair(self, numero_conta: str, valor: float):
        "Subtrai um valor em uma conta."""
        if numero_conta in self.contas:
            self.contas[numero_conta]['saldo'] -= valor
        else:
            raise ValueError("Conta não encontrada")

    def transferir(self, banco_origem: str, conta_origem: str, banco_destino: str, conta_destino: str, valor: float):
        """Transfere um valor de uma conta para outra."""
        global lista_bancos
        with self.lock:
            self.subtrair(conta_origem, valor)
            if banco_origem == banco_destino:
                self.depositar(conta_destino, valor)
            else:
                match = re.search(r'\d{1,4}$', banco_destino)
                port =  int(match.group()) + 8000
                other_bank = ServerProxy(f"http://localhost:{port}")
                other_bank.depositar(conta_destino, valor)
        return [i.contas for i in lista_bancos]


def cria_bancos_e_contas(n_bancos: int, n_clientes:int):
    global lista_bancos, lista_clientes
    for i in range(n_bancos):
        lista_bancos.append(Banco("banco_"+str(i)))
        for j in range(n_clientes):
            cliente = Cliente("c"+str(j)+"_"+lista_bancos[i].nome)
            lista_clientes.append(cliente.nome)
            lista_bancos[i].criar_conta(cliente.nome, str(str(i).zfill(3)+str(j).zfill(3)), 100)
    print("Situação Inicial das Contas:")
    for i in lista_bancos:
        print(i.contas)
    print("\n")


def roda_servidor(banco, port):
    server = SimpleXMLRPCServer(("localhost", port), allow_none=True)
    server.register_function(banco.transferir)
    server.register_function(banco.depositar)
    print(f"Servidor do banco {banco.nome} iniciado na porta {port}...")
    server.serve_forever()


def cria_servidor(n_bancos):
    servers = []
    for i in range(n_bancos):
        port = 8000 + i
        server = threading.Thread(target=roda_servidor, args=(lista_bancos[i], port))
        servers.append(server)
        server.start()
    for server in servers:
        server.join()

n_clientes = 6
n_bancos = 6
lista_bancos = []
lista_clientes = []

cria_bancos_e_contas(n_bancos, n_clientes)
cria_servidor(n_bancos) 
