menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []  
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        while True:
            try:
                valor_deposito = float(input("Digite o valor a ser depositado: "))
                if valor_deposito > 0:
                    saldo += valor_deposito
                    extrato.append(f"Depósito de R${valor_deposito:.2f}. Saldo atual R$ {saldo:.2f}.")
                    print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso. Novo saldo: R$ {saldo:.2f}")
                    break
                else:
                    print("Operação falhou! O valor informado é inválido.")
                    break
            except ValueError:
                print("Por favor, insira um valor inteiro válido.")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            while True:
                try:
                    valor_saque = float(input("Digite o valor a ser sacado: "))
                    if valor_saque > 0:
                        if valor_saque > saldo:
                            print("Saldo insuficiente. Não é possível realizar o saque.")
                        elif valor_saque > limite:
                            print(f"Valor do saque excede o limite diário de R$ {limite:.2f}.")
                        else:
                            saldo -= valor_saque
                            extrato.append(f"Saque de R$ {valor_saque:.2f}. Saldo atual R$ {saldo:.2f}.")
                            numero_saques += 1
                            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso. Novo saldo: R$ {saldo:.2f}")
                        break
                    else:
                        print("Operação falhou! O valor informado é inválido.")
                    break
                except ValueError:
                    print("Por favor, insira um valor inteiro válido.")
        else:
            print("Limite diário de saques atingido. Tente novamente amanhã.")

    elif opcao == "e":
        print("\n##########Extrato:##########")
        for operacao in extrato:
            print(operacao)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("############################")
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione a operação desejada.")
