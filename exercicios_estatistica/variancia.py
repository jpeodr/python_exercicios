
lista = [-10, -5, 0, 5, 10, 15, 20, 25, 30, 40, 45, 50, 60, 70, 80, 90, 100]

def variancia(lista):
    contador = 0
    media = sum(lista) / len(lista)
    n = len(lista)
    for i in lista:
        s2 = ((i - media) ** 2)
        contador = contador + s2

    return contador / n



print(variancia(lista))