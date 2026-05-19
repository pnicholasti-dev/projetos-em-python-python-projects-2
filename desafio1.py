print("1- Cadastro de alunos")
print("2- Cadastro de professores")
print("3- Setor financeiro")

opcao = int(input("Escolha uma opção: "))
match opcao:
    case 1:
        print("---CADASTRO DE ALUNOS---")
        nome = input("Nome: ")
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        media = (n1 + n2)/2
        if media > 70:
            print("Aprovado")
        elif media >= 40 and media >= 60:
            print("Recuperação")
        else:
            print("Reprovado")
    
    case 2:
        print("---CADASTRO DE PROFESSORES---")
        nome = input("Nome: ")
        titulação = input("Titulação: ").lower()
        if titulação == "doutorado" or titulação == "mestrado":
            print("Pode orientar projetos")
        else:
            print("Titulação inválida")

    case 3:
        print("\---SETOR FINANCEIRO---")
        categoria = input("Categoria(aluno/professor): ").lower()
        if categoria == "aluno":
            mensalidade = 500
            valor_pago = float(input("Valor pago: "))
            if valor_pago >= mensalidade:
                print("Pagamento realizado com suceso")
            else:
                print("Valor inválido")
        elif categoria == "professor":
            salario = float(input("Salário base: "))
            horas_extra = int(input("Horas extras: "))
            valor_hora = salario/160
            pagamento_extra = horas_extra * (valor_hora * 1,5)
            total = salario + pagamento_extra
            print("Total a receber: ", total)
        else:
            print("Categoria inválida")

    case _:
        print("Opção inválida")
        print("Titulação inválida")


