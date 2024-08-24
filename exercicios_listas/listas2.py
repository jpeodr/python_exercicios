numeros_pares = []
for x in range(5):
    if x % 2 == 0:
        numeros_pares.append(x)
print(numeros_pares)

numeros_pares = [x for x in range(5) if x % 2 == 0]
print(numeros_pares)