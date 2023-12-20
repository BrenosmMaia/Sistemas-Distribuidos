## Como usar o sistema?

1. Escolha a quantidade de clientes no arquivo `banco.py`, linha 84
2. Escolha a quantidade de bancos no arquivo `banco.py`, linha 85
3. Preencha a lista de trânsferências, no arquivo `simulacao.py` mantendo o padrão das tuplas
4. Execute o arquivo `banco.py`
5. Execute o arquivo `simulacao.py`, em outro terminal

## Informações Gerais

Configuração Padrão:
 - 6 bancos com 6 clientes cada
 - cada conta começa com 100 já depositado

### Lista de Transferências

O valor `('banco_3', '003000', 'banco_1', '001001', 100)` significa "transferência do banco_3, conta '003000', para o banco_1, conta '001001', no valor de 100.
  
A numeração de contas segue o padrão {numero_do_banco}{numero_da_conta} sendo cada parte com 3 digitos. 
