def bubble_sort(lista):
    for j in range(len(lista)):
        for i in range(len(lista)-1):
            # primeiro ordena por letra
            if lista[i][0] > lista[i+1][0]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

            # se as letras forem iguais ordena por número
            elif lista[i][0] == lista[i+1][0] and lista[i][1] > lista[i+1][1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

    return lista


n = int(input())
poltronas = input().split()

poltronas = bubble_sort(poltronas)
vencedor = poltronas[n-1]

print(f'O vencedor está na fila {vencedor[0]} poltrona {vencedor[1]}!')
