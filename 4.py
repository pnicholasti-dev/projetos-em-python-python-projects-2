total_entregas = 0
while True:
    entregas = int(input("Entregas da Viagem (0 encerra): "))
    if entregas == 0:
        break
    total_entregas += entregas
print("Total de entregas do dia: ", total_entregas)