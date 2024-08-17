# Leia a entrada do usuário
entrada = input("Digite um texto: ")

# Escreva primeiro caractere da string
print(f"O primeiro caractere da string é {entrada[0]}")

# Escreva os 3 primeiros caracteres do texto
print(f"Os 3 primeiros caracteres do texto é: {entrada[:3]}")

# Escreva os 3 últimos caracteres do texto
print(f"Os 3 últimos caracteres da string é {entrada[-3:]}")

# Escreva a string ao contrário
print(f"A string ao contrário é: {entrada[::-1]}") 

# Divida a string por espaço
entrada_dividida = entrada.split(" ")
print(f"A string dividida por espaço é: {entrada_dividida}")

# Escreva o primeiro pedaço da string
print(f"O primeiro pedaço da string é: {entrada_dividida[0]}")

# Escreva o tamanho da string
print(f"O tamanho da string é {len(entrada)}")