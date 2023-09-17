from cliente import Cliente
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class Banco:
    def __init__(self, nome: str):
        """Inicializa um objeto Banco com um nome e um dicionário vazio de contas."""
        self.nome = nome
        self.contas = {}

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

    def transferir(self, cliente: str, conta_origem: str, banco_destino: str, conta_destino: str, valor: float):
        """Transfere um valor de uma conta para outra."""
        if banco_destino != self.nome: raise NotImplementedError("Apenas transferencias no mesmo banco")
        
        if cliente == self.contas[conta_origem]['cliente']:
            if conta_origem in self.contas and self.contas[conta_origem]['saldo'] >= valor:
                self.contas[conta_origem]['saldo'] -= valor
                self.depositar(conta_destino, valor)
                return self
            else:
                raise ValueError("Transferência inválida")
        else:
            raise ValueError("A conta de origem não pertence ao solicitante da transferência")


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Instanciando banco
banco_1 = Banco('Banco_1')

# Instanciando cliente
cliente_1 = Cliente('João')
cliente_2 = Cliente('Maria')

# Criando contas
banco_1.criar_conta(cliente_1.nome, '123', 100)
banco_1.criar_conta(cliente_2.nome, '456', 100)

# Cria o servidor
with SimpleXMLRPCServer(('localhost', 8080), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registra a função transferir
    server.register_function(banco_1.transferir)

    # Roda o servidor
    print("Servidor RPC iniciado na porta 8080")
    server.serve_forever()

