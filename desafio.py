menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = int(input("Digite o valor para depósito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Valor depositado: R$ {deposito:.2f}")
        else:
            print("Erro: Valor inválido")
        
        
    elif opcao == "s":
        saque = int(input("Digite o valor para saque: "))

        excedeu_saldo = saque > saldo
        
        excedeu_limite = saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente.")

        elif excedeu_limite:
            print(f"O valor do saque ultrapassa o limite de R$ {limite:.2f} , tente novamente com um valor mais baixo.")
        
        elif excedeu_saques:
            print("Limite de saques diários atingido. Tente novamente amanhã.")
        
        elif saque > 0:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque: R$ {saque:.2f}\n"
            print(f"O valor R$ {saque:.2f} foi sacado. Seu saldo atual é R$ {saldo:.2f}")
        
        else:
            print("Erro: Valor inválido")
        
    elif opcao == "e":
        print("\n=========== EXTRATO ===========")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("===============================")

    elif opcao == "q":
        break

    else:
        print("Erro: Opção selecionada inválida.")
