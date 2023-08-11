class Pessoa():
    def __init__(self, nome, lista, tamanho):
        self.nome = nome
        self.tamanho = tamanho
        self.lista = lista
        self.fogueiras = 0

    def checar_pulo(self):
        index = 0
        pulando = True
        while pulando:
            self.fogueiras += 1
            valor = self.lista[index]
            if index+valor+1 >= self.tamanho:
                if self.tamanho==1 and valor == 0:
                    self.fogueiras = 0
                return True
            elif self.lista[index+valor] == 0:
                return False
            index += valor

    def get_fogueiras(self):
        return self.fogueiras


for x in range(4):
    TAMANHO = int(input())
    frase = input().split(' ')
    LISTA = [int(x) for x in frase[1:]]
    NOME = frase[0]
    pessoa = Pessoa(NOME, LISTA, TAMANHO)
    ganhou = pessoa.checar_pulo()
    fogueiras = pessoa.get_fogueiras()
    if ganhou:
        print(f'{NOME} conseguiu!')
        print(f'{NOME} precisou pular {fogueiras} fogueiras')
    else:
        print(f'Ah, que pena, {NOME} não conseguiu!')
