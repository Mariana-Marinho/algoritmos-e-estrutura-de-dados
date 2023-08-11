def merge(direita, esquerda):
    ordenada = []

    while direita and esquerda:
        if direita[0] > esquerda[0]:
            ordenada.append(esquerda.pop(0))
        else:
            ordenada.append(direita.pop(0))

    while direita:
        ordenada.append(direita.pop(0))

    while esquerda:
        ordenada.append(esquerda.pop(0))

    return ordenada


def merge_sort(lista):
    if len(lista) == 1:
        return lista

    meio = len(lista) // 2
    dir = lista[:meio]
    esq = lista[meio:]

    dir = merge_sort(dir)
    esq = merge_sort(esq)

    ordenada = merge(dir, esq)
    return ordenada


filmes = input().split(',')
entrada = input().split(',')
filmes.extend(entrada)

filmes = merge_sort(filmes)
mediana = len(filmes) // 2
filme = filmes[mediana]

print(f'Os amigos decidiram assistir a {filme} que estava na posição {mediana+1} da lista.')
