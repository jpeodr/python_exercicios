# While
# Faça um loop para uma contagem até algum número
limite = int(input("Defina um limite: "))
contador = int(input("Digite um número: "))
while contador <= limite:
    print(f"Iteração: {contador}")
    contador += 1
print(contador)