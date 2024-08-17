# Faça um programa para verificar se a pessoa é MAIOR de idade


idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 60:
    print("Você é MAIOR de idade!")
elif idade >= 60:
    print("Você é VELHO!")
else:
    print("Você é MENOR de idade!")

print("Programa encerrado.")