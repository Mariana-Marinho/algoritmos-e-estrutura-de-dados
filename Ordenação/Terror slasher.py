"""TUDO ERRADO"""

def heap_sort_max(lista):
    n = len(lista)
    comparacao = 0

    for i in range(n//2 - 1, -1, -1):
        comparacao = heapify(lista, n, i, comparacao)
    for i in range(n-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        comparacao = heapify(lista, i, 0, comparacao)

    return comparacao


def heapify(lista, n, i, c):
    c += 1

    maior = i
    esquerda = 2*i + 1
    direita = 2*i + 2

    if esquerda < n and lista[i] < lista[esquerda]:
        maior = esquerda
    if direita < n and lista[maior] < lista[direita]:
        maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        c += 2
    heapify(lista, n, maior, c)

    return c


def particao(lista, menor, maior):
    pivo = lista[maior]
    i = menor-1

    for j in range(menor, maior):
        pass

    return pivo


def quick_sort(lista, menor, maior, c):
    c += 1
    if menor < maior:
        pivo = particao(lista, menor, maior)
        quick_sort(lista, menor, pivo-1, c)
        quick_sort(lista, menor+1, maior, c)


def selection_sort(lista):
    pass


def shell_sort(lista):
    pass


prob = input().split()

pessoas = [('isabela', heap_sort_max(prob)),
           ('mateus', quick_sort(prob)),
           ('joaquim', selection_sort(prob)),
           ('bianca', shell_sort(prob))]
pessoas = sorted(pessoas, key=lambda x: x[1])
print(pessoas)
