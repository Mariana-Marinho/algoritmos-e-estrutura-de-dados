class No:
    def __init__(self, nome):
        self.filho_direita = None
        self.filho_esquerda = None
        self.nome = nome


class Arvore:
    def __init__(self):
        self.raiz = None

    def set_arvore(self, nome):
        """
        função que preenche a árvore binária
        :param nome: nome da mulher
        :return: não retorna nada
        """
        pessoa = No(nome)

        if self.raiz is None:
            self.raiz = pessoa

        else:
            atual = self.raiz

            while atual is not None:

                if nome < atual.nome:
                    # se o nó novo for ficar do lado esquerdo
                    if atual.filho_esquerda is None:
                        atual.filho_esquerda = pessoa
                        atual = None
                    else:
                        atual = atual.filho_esquerda

                elif nome > atual.nome:
                    # se o nó novo for ficar na direta
                    if atual.filho_direita is None:
                        atual.filho_direita = pessoa
                        atual = None
                    else:
                        atual = atual.filho_direita

    def get_arvore(self, nome):
        """
        printa em ordem
        :param nome: Nó que representa a mãe
        :return: printa a mãe e seus filhos
        """
        mae = nome

        if mae is None:
            # condiçãe de parada da recursão do fim
            return

        filho_esquerda = mae.filho_esquerda
        filho_direita = mae.filho_direita

        if filho_esquerda is not None or filho_direita is not None:
            # se tiver filhos
            if filho_esquerda is not None and filho_direita is not None:
                print(f'{mae.nome} é mãe de {filho_esquerda.nome} e {filho_direita.nome}.')

            elif filho_esquerda is not None:
                print(f'{mae.nome} é mãe de {filho_esquerda.nome}.')

            elif filho_direita is not None:
                print(f'{mae.nome} é mãe de {filho_direita.nome}.')

        self.get_arvore(filho_esquerda)  # printar o lado esquerdo da árvore
        self.get_arvore(filho_direita)  # printar o lado direito da árvore


familia = input().split()
arvore = Arvore()

for nome in familia:
    arvore.set_arvore(nome)

arvore.get_arvore(arvore.raiz)  # pritna a árvore a partir da raiz
