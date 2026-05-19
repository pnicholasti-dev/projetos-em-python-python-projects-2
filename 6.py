compras = int(input("Quantas compras você fez no dia ? "))
total = 0
for i in range (1, compras + 1):
    valor = float(input("Valor da compra em R$: "))
    total += valor
print("Total faturado: R$", total)