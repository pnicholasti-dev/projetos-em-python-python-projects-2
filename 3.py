total = 0

while True:
    valor = float(input("Digite o valor da compra (0 para encerrar): "))

    if valor == 0:
        break

    total += valor

print("Total do dia: R$ ", total)