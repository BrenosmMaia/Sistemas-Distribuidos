from cliente import Cliente

class Banco:
    def __init__(self, nome: str):
        """Inicializa um objeto Banco com um nome e um dicionário vazio de contas."""
        self.nome = nome
        self.contas = {}

    def criar_conta(self, cliente: 'Cliente', numero_conta: str, saldo_inicial: float = 0):
        """Cria uma nova conta no banco com um saldo inicial e adiciona a conta ao cliente."""
        self.contas[numero_conta] = {'cliente': cliente.nome, 'saldo': saldo_inicial}

    def depositar(self, numero_conta: str, valor: float):
        """Deposita um valor em uma conta."""
        if numero_conta in self.contas:
            self.contas[numero_conta] += valor
        else:
            raise ValueError("Conta não encontrada")

    def depositar(self, numero_conta: str, valor: float):
        """Deposita um valor em uma conta."""
        if numero_conta in self.contas:
            self.contas[numero_conta]['saldo'] += valor
        else:
            raise ValueError("Conta não encontrada")

    def transferir(self, cliente: 'Cliente', conta_origem: str, banco_destino: 'Banco', conta_destino: str, valor: float):
        """Transfere um valor de uma conta para outra."""
        if cliente.nome == self.contas[conta_origem]['cliente']:
            if conta_origem in self.contas and self.contas[conta_origem]['saldo'] >= valor:
                self.contas[conta_origem]['saldo'] -= valor
                banco_destino.depositar(conta_destino, valor)
            else:
                raise ValueError("Transferência inválida")
        else:
            raise ValueError("A conta de origem não pertence ao solicitante da transferência")