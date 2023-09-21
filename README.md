# Sistemas-Distribuidos

## Como usar o sistmema?

1. Clone o repositório
2. Entre na pasta tarefa-01
3. Escolha a quantidade de clientes no arquivo `banco.py`, linha 80
4. Escolha a quantidade de bancos no arquivo `banco.py`, linha 81
5. Preencha a lista de trânsferências, no arquivo `simulacao.py` mantendo o padrão das tuplas
6. Execute o arquivo `banco.py`
7. Execute o arquivo `simulacao.py`, em outro terminal

## Informações Gerais

Configuração Padrão:
 - 3 bancos com 4 clientes cada
 - cada conta começa com 100 já depositado

### Lista de Transferências

O valor `('banco_0', '00', 'banco_1', '10', 50)` significa "transferência do banco_0, conta '00', para o banco_1, conta '10', no valor de 50.
  
A numeração de contas segue o padrão {numero_do_banco}{numero_da_conta} com índice começando no zero. Ou seja, com 3 bancos e 4 clientes, a "ultima" conta é a '23' (banco 2, conta 3) 

Em uma configuração com 10 bancos e 5 clientes, uma tranferência válida seria `('banco_9', '94', 'banco_5', '50', 100)`, que significa "transferência do banco_9, conta '94', para o banco_4, conta '50', no valor de 100
