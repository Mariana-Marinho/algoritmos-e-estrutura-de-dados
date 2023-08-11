class No:
    def __init__(self, nome, dinheiro):
        self.proximo = None
        self.anterior = None
        self.nome = nome
        self.dinheiro = dinheiro


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        self.valor = 0

    def adicionar_fim(self, nome, dinheiro):
        """ adiciona um nó ao fim da lista """
        novo_no = No(nome, dinheiro)
        if self.inicio is None:
            self.inicio = novo_no
        else:
            self.fim.proximo = novo_no
            novo_no.anterior = self.fim
        self.fim = novo_no
        self.tamanho += 1

    def remover(self, nome):
        """ remove um nó da lista """
        no_atual = self.inicio

        while no_atual is not None:

            if no_atual.nome == nome:
                if no_atual.anterior is not None:
                    # se tiver algum nó antes
                    no_atual.anterior.proximo = no_atual.proximo
                else:
                    # se não tiver algum nó antes
                    self.inicio = no_atual.proximo

                if no_atual.proximo is not None:
                    # se tiver nó depois
                    no_atual.proximo.anterior = no_atual.anterior
                else:
                    # se não tiver nó depois
                    self.fim = no_atual.anterior

                return True
            no_atual = no_atual.proximo

    def set_fila(self, nome, dinheiro):
        """ poe a pessoa no fim da fila """
        self.adicionar_fim(nome, dinheiro)

    def get_primeiro(self):
        """ retorna o nome e pagamento do primeiro e o remove da fila """
        primeiro = self.inicio
        self.remover(primeiro.nome)
        return primeiro.nome, primeiro.dinheiro

    def get_ultimo(self):
        """ retorna o nome e pagamento do ultimo da fila"""
        ultimo = self.fim
        return ultimo.nome, ultimo.dinheiro

    def get_valor(self, caixa):
        """ retorna o valor arrecadado de cada caixa"""
        return f'Caixa {caixa}: R$ {self.valor}'


caixa_1 = Fila()
caixa_2 = Fila()

running = True
while running:
    COMANDO = input().split()

    if COMANDO[0] == 'ENTROU:':
        COMANDO, NOME, CAIXA, DINHEIRO = COMANDO
        print(f'{NOME} entrou na fila {CAIXA}')
        if CAIXA == '1':
            caixa_1.set_fila(NOME, float(DINHEIRO))
        else:
            caixa_2.set_fila(NOME, float(DINHEIRO))

    elif COMANDO[0] == 'PROXIMO:':
        COMANDO, CAIXA = COMANDO

        if CAIXA == 1 and caixa_1.tamanho == 0 and caixa_2.tamanho > 0:
            # se o caixa chamou proximo mas a fila tá vazia
            n = int(caixa_2.tamanho / 2) + (caixa_2.tamanho%2>0) # arredondar para cima
            for i in range(n):
                # acha o último da fila e o aloca para o começo da outra
                NOME, DINHEIRO = caixa_2.get_ultimo
                caixa_1.set_fila(NOME, float(DINHEIRO))

        elif CAIXA == 2 and caixa_2.tamanho == 0 and caixa_1.tamanho > 0:
            # se o caixa chamou proximo mas a fila tá vazia
            n = int(caixa_1.tamanho / 2) + (caixa_1.tamanho % 2 > 0)  # arredondar para cima
            for i in range(n):
                # acha o último da fila e o aloca para o começo da outra
                NOME, DINHEIRO = caixa_1.get_ultimo
                caixa_2.set_fila(NOME, float(DINHEIRO))

        if CAIXA == 1:
            NOME, DINHEIRO = caixa_1.get_primeiro()
            caixa_1.valor += DINHEIRO
        else:
            NOME, DINHEIRO = caixa_2.get_primeiro()
            caixa_2.valor += DINHEIRO
        print(f'{NOME} foi chamado para o caixa {CAIXA}')


    else:
        running = False

arrecadado_1 = caixa_1.get_valor(1)
arrecadado_2 = caixa_2.get_valor(2)
print(f'{arrecadado_1}, {arrecadado_2}')