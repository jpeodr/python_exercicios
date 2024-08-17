# Calculadora interativa

import os

menu = """
---------------------
Selecione a opção:
      
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
5 - Potenciação
6 - N1 raiz de N2

0 - Sair
---------------------
"""
while True:
    print(menu)
    opcao = input("Digite a OPERAÇÃO desejada: ")
    if opcao == "0":
        print("Programa encerrado")
        break
    try:
        n1 = float(input("Digite o PRIMEIRO número: "))
        n2 = float(input("Digite o SEGUNDO número: "))
    except ValueError:
        print("Número inválido!")
        continue
    if opcao == "1":
        resultado = n1 + n2
        print(f"A SOMA entre os valores é: {resultado}")
    if opcao == "2":
        resultado = n1 - n2
        print(f"A SUBTRAÇÃO entre os valores é: {resultado}")
    if opcao == "3":
        resultado = n1 * n2
        print(f"A MULTIPLICAÇÃO entre os valores é: {resultado}")
    if opcao == "4":
        resultado = n1 / n2
        print(f"A DIVISÃO entre os valores é: {resultado}")
    if opcao == "5":
        resultado = n1 ** n2
        print(f"A POTENCIAÇÃO entre os valores é: {resultado}")
    if opcao == "6":
        raiz = n1 * (1/n2)
        print(f"A RAIZ entre os valores é: {raiz}")
    input("...")