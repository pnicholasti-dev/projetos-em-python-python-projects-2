lotes = int(input("Quantos lotes chegaram ? "))
estoque = 0
for i in range (1, lotes + 1):
    quantidade = float(input("quantidade do lote: "))
    estoque += quantidade
print("Total de itens no estoque: ", estoque)