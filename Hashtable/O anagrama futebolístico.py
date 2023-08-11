class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = []

    def insert(self, nome):
        value = self.hashvalue(nome)

        for i, grupinho in enumerate(self.buckets):
            if self.hashvalue(grupinho[0]) == value:
                # se huver colisão
                if sorted(nome) == sorted(grupinho[0]):
                    grupinho.append(nome)
                    print(f'{nome} entrou no grupinho')
                    return
                else:
                    print(f'{nome} tentou se entrosar, mas foi descoberto')
                    return

            elif self.hashvalue(grupinho[0]) > value:
                # se o nome a ser inserido tem que vir antes
                self.buckets.insert(i, [nome])
                print(f'{nome} criou um grupinho')
                return

        self.buckets.append([nome])
        print(f'{nome} criou um grupinho')
        return

    def hashvalue(self, nome):
        value = sum(ord(i) for i in nome)
        return value % self.size

    def print_tabela(self):
        print(f'Grupinhos:{str(self.buckets)}')


n = int(input())
tabela_hash = HashTable(n)
for _ in range(n):
    jogador = input()
    tabela_hash.insert(jogador)

tabela_hash.print_tabela()
