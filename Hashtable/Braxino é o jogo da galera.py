"""TUDO ERRADO"""


class HashTable:
    def __init__(self, size, maximo):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.max = maximo

    def add(self, valor, partida):
        value = valor % self.size
        vazios = self.max

        for i, grupo in enumerate(self.buckets):
            if grupo:
                vazios -= 1

                if i == value:
                    # se houver colisão
                    if len(grupo) == self.max:
                        print(f'partida: {partida} não foi adicionada por falta de espaço na lista!')
                    else:
                        grupo.append(partida)
                        return
            else:
                if i == value:
                    self.buckets[value] = [partida]

        if vazios == 0:
            print(f'partida: {partida} não foi adicionada por falta de espaço na hashtable!')
            return

        self.buckets.append([partida])
        return

    def rem(self, valor, partida):
        value = valor % self.size
        if self.buckets[value]:
            if partida in self.buckets[value]:
                self.buckets[value].remove(partida)
                return
            print(f'partida: {partida} não foi removida porque não pertencia a lista!')
        else:
            print(f'o sistema não está armazenando partidas nesse horário!')

    def remt(self, valor):
        value = valor % self.size
        self.buckets[value].clear()

    def print_buckets(self):
        for i, partidas in enumerate(self.buckets):
            print(f'Slot {i}: {str(partidas)}' if partidas else f'Slot {i}: Vazio')


if __name__ == '__main__':
    espacos, maximo = input().split(' ')
    espacos = int(espacos)
    maximo = int(maximo)

    tabela_hash = HashTable(espacos, maximo)

    while True:
        comando = input()
        if comando == 'ADD':
            while True:
                entrada = input()
                if entrada == 'DONE':
                    break

                valor_hash, partida_nome = entrada[0], entrada[2:]
                tabela_hash.add(int(valor_hash), partida_nome)

        elif comando == 'REM':
            while True:
                entrada = input()
                if entrada == 'DONE':
                    break

                valor_hash, partida_nome = entrada[0], entrada[2:]
                tabela_hash.rem(int(valor_hash), partida_nome)

        elif comando == "PRINT":
            tabela_hash.print_buckets()

        else:
            # comando == "REMT"
            comando, timestamp = comando.split(' ')
            tabela_hash.remt(int(timestamp))
