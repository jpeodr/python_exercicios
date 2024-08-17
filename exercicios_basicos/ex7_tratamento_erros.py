try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    resultado = n1 / n2
    print("O resultado da divisão é: ", resultado)
except ValueError as erro_valor:
    print("Entrada inválida, coloque o tipo de dado correto.")
    print(erro_valor)
except ZeroDivisionError as erro_divisao_zero:
    print("Erro de divisão por zero.")
    print(erro_divisao_zero)