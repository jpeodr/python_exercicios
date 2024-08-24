cardapio = {
        "Salgado": 4.50,
        "Lanche": 6.50,
        "Suco": 3.00,
        "Refrigerante": 3.50,
        "Doce": 1.00
    }

cliente1 = ["Salgado", "Lanche"]
cliente2 = ["Doce", "Refrigerante", "Salgado"]


def calcular_total(lista_do_cliente):
    total = 0
    for i in lista_do_cliente:
        valor_produto = cardapio[i]
        total = total + valor_produto
    return total
    

print(f"Total gasto pelo cliente 1: {calcular_total(cliente1)}")
print(f"Total gasto pelo cliente 2: {calcular_total(cliente2)}")
    