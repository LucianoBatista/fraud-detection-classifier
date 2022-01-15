# Tera Third Challenge

About do projeto!


# Data Dictionary

- **step** (Passo): representa o total de horas transcorrido desde o início da simulação. Esta feature vai variar entre 1 e 744 (30 dias);
- **type** (Tipo): tipo de transação (depósito, saque, débito, pagamento e transferência);
- **amount** (Quantia): total que foi transacionado;
- **nameOrig** (ClienteOrigem): cliente que iniciou a transação
- **oldbalanceOrg** (SaldoInicialOrigem): saldo da conta de origem antes da transação;
- **newbalanceOrig** (SaldoFinalOrigem): saldo da conta de origem após a transação;
- **nameDest** (ClienteDestino): cliente de destino da transação;
- **oldbalanceDest** (SaldoInicialDestino): saldo da conta de destino antes da transação;
- **newbalanceDest** (SaldoFinalDestino): saldo da conta de destino após a transação;
- **isFraud** (ÉFraude): flag que define se a transação é fraudulenta ou não. Nesta simulação o objetivo da fraude é assumir a conta do usuário, esvaziá-la transferindo para outra conta e então sacando o dinheiro.
- **isFlaggedFraud** (SinalizadaComoFraude): automaticamente marcadas pelo banco como fraude por tentarem transferir mais de 200.000 em uma única transação.

# Doubts

- Dados simulados, mas compreendem de fato a realidade? Detalhes dessa simulação?
- 