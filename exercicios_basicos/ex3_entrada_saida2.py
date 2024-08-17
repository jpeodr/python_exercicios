import os

# Informar o valor de três variáveis
# Produto, Valor do produto, Quantidade
# Usar a função de saída e mostre os valores

produto = input("Nome do produto: ")
quantidade = input("Quantidade de produtos: ")
valor_produto = float(input("Valor do produto R$: "))

# Comando para limpar a tela (Necessário 'import os')
os.system('cls')

# Saída de dados
print("-------------------------")
print("-- Produto registrado! --")
print("Produto: ", produto)
print("Quantidade: ", quantidade)
print(f'Valor: R$: {valor_produto:.2f}') # Print f para formatar melhor os dados 

# Tipo de dado da variável
print(" ")
print("-------------------------")
print("Tipo 'valor_produto':", type(valor_produto))