#Gere uma lista contendo os múltiplos de 3 entre 1 e 50
lista = []
for i in range (1, 50): #50 posições
    lista.append(i * 3)
print(lista)

print(" ")

multiplos_3 = [i for i in range(1, 50) if i % 3 == 0] # correto
print(multiplos_3)