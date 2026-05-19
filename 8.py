quantidade = int(input("Quantas viagens foram realizadas? "))
total_entregas = 0
for i in range (1, quantidade +1):
    entregas = int(input("Entregas na viagem: "))
    total_entregas += entregas

media = total_entregas / quantidade

print("Total de entregas: ", total_entregas)
print("Média por viagem: ", media)