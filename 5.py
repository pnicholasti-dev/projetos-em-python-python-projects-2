total_vendas = 0
while True:
    print("\n=== CAIXA DA LOJA===")
    print("1- Feijão (R$ 8,00)")
    print("2- Arroz (R$ 6,50)")
    print("3- Farinha (R$ 5,00)")
    print("4- Total de vendas")
    print("5- Encerrar caixa")
    print("0- Sair")

    opcao = int(input("Escolha: "))
    match opcao:
        case 1:
            total_vendas += 8.00
            print("Feijão vendido!")

        case 2:
            total_vendas += 6.50
            print("Arroz vendido!")
        
        case 3:
            total_vendas += 5.00
            print("Farinha vendida!")
        
        case 4:
            print("Total R$: ", total_vendas)

        case 5:
            print("Operação de caixa encerrada")

        case _:
            print("Opção inválida!")