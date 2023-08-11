class No:
    def __init__(self, nome):
        self.proximo = None
        self.anterior = None
        self.nome = nome


class ListaLigada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar_fim(self, nome):
        """ adiciona um nó ao fim da lista """
        novo_no = No(nome)
        if self.inicio is None:
            self.inicio = novo_no
        else:
            self.fim.proximo = novo_no
            novo_no.anterior = self.fim
        self.fim = novo_no

    def achar(self, nome):
        """ procura um nó na lista """
        no_atual = self.inicio
        while no_atual is not None:
            if no_atual.nome == nome:
                return True
            no_atual = no_atual.proximo
        return False

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

    def set_beijo(self, nome):
        if not self.achar(nome):
            self.adicionar_fim(nome)

    def set_superbeijo(self, nome):
        if self.achar(nome):
            self.remover(nome)
        self.adicionar_fim(nome)

    def set_xodo(self, nome):
        self.remover(nome)

    def mostrar_beijo(self):
        if self.inicio is not None:
            no_atual = self.fim
            while no_atual is not None:
                print(no_atual.nome)
                no_atual = no_atual.anterior
        else:
            print('Histórico vazio.')


comando, usuario = input().split()
perfil = ListaLigada()

running = True
while running:
    comando = input()
    if comando == 'MOSTRAR' or comando == 'FIM':
        if comando == 'MOSTRAR':
            perfil.mostrar_beijo()
        else:
            running = False
    else:
        comando, NOME = comando.split()
        if comando == 'BEIJO':
            perfil.set_beijo(NOME)
        elif comando == 'SUPERBEIJO':
            perfil.set_superbeijo(NOME)
        elif comando == 'XODÓ':
            perfil.set_xodo(NOME)

print(f'O histórico final do usuário {usuario} é:')
perfil.mostrar_beijo()
