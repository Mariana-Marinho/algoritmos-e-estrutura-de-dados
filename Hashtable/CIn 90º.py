class HashTable:
    def __init__(self):
        self.tabela_hash = []

    def hashvalue(self, nome):
        value = sum(ord(i) - ord('A') + 1 for i in nome) % 10
        return value

    def insert(self, nome):
        value = self.hashvalue(nome)

        if len(self.tabela_hash) <= value:
            for i in range(len(self.tabela_hash), value + 1):
                self.tabela_hash.append([])

        self.tabela_hash[value].append(nome)

    def print_hash(self):
        for value, name in enumerate(self.tabela_hash):
            if name:
                print(f'{value}: {" ".join(name)}')


hash_table = HashTable()

n = int(input())
for _ in range(n):
    name = input()
    hash_table.insert(name)

hash_table.print_hash()
