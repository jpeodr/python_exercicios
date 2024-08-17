#Faça a soma de dois valores e mostre o resultado
try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    resultado = n1 + n2
    print(f"A soma entre {n1} e {n2} é  = {resultado}")
except ValueError:
    print(" ")
    print("-------------------------------")
    print("ENTRADA INVÁLIDA! Utilize um número INTEIRO.")
