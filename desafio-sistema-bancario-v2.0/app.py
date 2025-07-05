menu = """
Bem-vindo ao sistema de saque!
[U] Criar Usuário
[C] Criar Conta
[S] Saque
[D] Depositar
[E] Extrato
[Q] Sair
O que deseja fazer?
""";

# CONSTANTS
LIMITE_SAQUE = 3;
SAQUE_MAXIMO = 500;
usuarios = [];
contas = [];
# VARIABLES
saldo_total = 0;
num_saques = 0;
extrato_total = "";

def sacar(*, saldo, valor_saque, extrato, limite, numero_saques):
    if numero_saques >= limite:
        return saldo, extrato, numero_saques, "Limite de saques atingido."
    elif valor_saque > SAQUE_MAXIMO:
        return saldo, extrato, numero_saques, f"Valor máximo para saque é {SAQUE_MAXIMO}."
    elif valor_saque > saldo:
        return saldo, extrato, numero_saques, "Saldo insuficiente."
    else:
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        numero_saques += 1
        return saldo, extrato, numero_saques, f"Saque de R$ {valor_saque:.2f} realizado com sucesso."



def depositar(saldo, valor_deposito, extrato):
    if valor_deposito <= 0:
        return saldo, extrato, "Valor de depósito deve ser positivo."
    saldo += valor_deposito;
    extrato += f"Depósito: R$ {valor_deposito:.2f}\n";
    return saldo, extrato, f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso."


def exibir_extrato(saldo, *, extrato):
    if extrato:
        print("\n========== EXTRATO ==========")
        print(extrato)
    else:
        print("\nNenhuma transação realizada.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("==============================\n")


def criar_usuario(nome, data_nascimento, cpf, endereco):
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        return "Usuário já cadastrado com este CPF."
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(novo_usuario)
    return "Usuário cadastrado com sucesso."

def criar_conta (agencia, numero_conta, usuario):
    if not any(user["cpf"] == usuario for user in usuarios):
        return "Usuário não encontrado. Crie um usuário primeiro."
    if agencia != "0001":
        return "Agência inválida. Apenas '0001' é permitida."
    numero_conta = len(contas) + 1
    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
    }
    contas.append(nova_conta)
    return f"Conta criada com sucesso. Número da conta: {numero_conta}"

while True:

    option = input(menu).upper();

    # CRIAR USUÁRIO
    if option == 'U':
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
        cpf = input("Digite o CPF: ")
        endereco = input("Digite o endereço: ")
        
        mensagem = criar_usuario(
            nome=nome, 
            data_nascimento=data_nascimento, 
            cpf=cpf, 
            endereco=endereco
        )
        print(mensagem)
        print(usuarios)
        continue;

    # CRIAR CONTA
    elif option == 'C':
        agencia = input("Digite o número da agência (apenas '0001' é permitido): ")
        usuario = input("Digite o CPF do usuário: ")

        mensagem = criar_conta(
            agencia=agencia,
            numero_conta=None,  # Será gerado automaticamente
            usuario=usuario
        )
        print(mensagem)
        continue;

    # SAQUE
    if option == 'S':
        valor_saque = float(input("Digite o valor do saque: "))
        saldo_total, extrato_total, num_saques, mensagem = sacar(
            saldo=saldo_total,
            valor_saque=valor_saque,
            extrato=extrato_total,
            limite=LIMITE_SAQUE,
            numero_saques=num_saques
        )
        print(mensagem)
        continue;


    # DEPOSITO
    elif option == 'D':
        valor_deposito = float(input("Digite o valor do depósito: "));
        saldo_total, extrato_total, mensagem = depositar(
            saldo_total, 
            valor_deposito, 
            extrato_total
        )
        print(mensagem)
        continue;
    
    # EXTRATO
    elif option == 'E':
        exibir_extrato(
            saldo=saldo_total, 
            extrato=extrato_total
        )
    
    # SAIR
    elif option == 'Q':
        print("Saindo...");
        break;

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida. Tente novamente.");
