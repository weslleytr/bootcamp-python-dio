menu = """
Bem-vindo ao sistema de saque!
[S] Saque
[D] Depositar
[E] Extrato
[Q] Sair
O que deseja fazer?
""";

# CONSTANTS
LIMITE_SAQUE = 3;
SAQUE_MAXIMO = 500;

# VARIABLES
saldo = 0;
num_saques = 0;
extrato = "";

while True:

    option = input(menu).upper();

    # SAQUE
    if option == 'S':
        if num_saques >= LIMITE_SAQUE:
            print("Limite de saques atingido.");
            continue;

        valor_saque = float(input("Digite o valor do saque: "));
        if valor_saque > SAQUE_MAXIMO:
            print(f"Valor máximo para saque é {SAQUE_MAXIMO}.");
            continue;

        if valor_saque > saldo:
            print("Saldo insuficiente.");
            continue;

        saldo -= valor_saque;
        num_saques += 1;
        extrato += f"Saque: R$ {valor_saque:.2f}\n";
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.");

    # DEPOSITO
    elif option == 'D':
        valor_deposito = float(input("Digite o valor do depósito: "));
        if valor_deposito <= 0:
            print("Valor de depósito deve ser positivo.");
            continue;

        saldo += valor_deposito;
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n";
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.");
    
    # EXTRATO
    elif option == 'E':
        print("\nExtrato:");
        print(extrato if extrato else "Nenhuma transação realizada.");
        print(f"Saldo atual: R$ {saldo:.2f}");
    
    # SAIR
    elif option == 'Q':
        print("Saindo...");
        break;

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida. Tente novamente.");
