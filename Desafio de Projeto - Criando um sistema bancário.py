menu = """Escolha uma opção:
    1 - Depositar
    2 - Sacar
    3 - Visualizar extrato
    4 - Informações
    0 - Sair/Finalizar
"""  
contador_saque = int()
Deposito = float()
saque = float()
outro_saque = int()
saque_1 = float()
saque_2 = float()
saque_3 = float()
saldo = float()

while True:
    opcao = int(input(menu))

    if opcao == 1:
        Deposito += float(input("Qual o valor a ser depositado?\n"))
        saldo += Deposito
        print("Valor depositado!!!\n")
    
        if Deposito <= 0:
            print("Este valor não pode ser depositado!!!\n")
            Deposito = 0

    elif opcao == 2:
        while outro_saque == 0:
            if contador_saque < 3:
                print(f"Saques realizados hoje: {contador_saque}")
                saque = float(input("Qual o valor a ser sacado? (Saques permitidos até R$500.00)\n"))
        
                if saque > 500.00 or saque <= 0 or saque > saldo:
                    print("Saque não permitido!!!")
                    print("Acesse 'Informações' para saber mais\n")
                else:
                    saldo -= saque
                    print("Valor sacado!!!\n")
                    contador_saque += 1
            else:
                print("Limite diário de saques já atingido!!!\n")
                print("Acesse 'Informações' para saber mais\n")
                break

            if contador_saque == 1:
                saque_1 = saque
            elif contador_saque == 2:
                saque_2 = saque
            elif contador_saque == 3:
                saque_3 = saque

            print("Gostaria de fazer outro saque?\n")
            print("   SIM - Digite 0\n") 
            outro_saque = int(input("   NÃO - Digite 1\n"))       

    elif opcao == 3:
        print("============EXTRATO============\n")
        if saque == 0 and Deposito == 0:
            print("Não foram realizadas movimentações.")
        else:
            if saque_1 > 0:
                print("Os valores dos saques foram:\n")
                print(f"R${float(saque_1):.2f}\n")
            
            if saque_2 > 0:
                print(f"R${float(saque_2):.2f}\n")
            
            if saque_3 > 0:           
                print(f"R${float(saque_3):.2f}\n")

            print("O valor dos depósitos foi:\n") 
            print(Deposito)
            print(" ")
            
            print("O valor do seu saldo é de:\n")
            print(saldo)
            print(" ")

    elif opcao == 4:
        print("O limite de saques é de 3 vezes ao dia.")
        print("Nenhum saque pode ultrapassar os R$500.00.")
        print("Não se pode depositar ou sacar R$0.00 ou valores negativos.")
        print("Você não pode sacar um valor maior do que seu saldo.")
        print("Lembre-se de sempre sair do sistema quando terminar as operações.\n")

    else:
        print("Obrigado por usar nosso serviço!!!")
        break