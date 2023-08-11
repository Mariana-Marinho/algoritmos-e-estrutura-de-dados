class No:
    def __init__(self, nome):
        self.nome = nome
        self.esquerda = None
        self.direita = None
        self.altura = 1


class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, nome):
        if self.buscar(nome) is not None:
            print(f'{nome} JA EXISTE')
            return False
        else:
            self.raiz = self._inserir(self.raiz, nome)
            print(f'{nome} INSERIDO')
            return True

    def _inserir(self, no, nome):
        if no is None:
            return No(nome)

        if nome < no.nome:
            no.esquerda = self._inserir(no.esquerda, nome)
        else:
            no.direita = self._inserir(no.direita, nome)

        no.altura = 1 + max(_altura(no.esquerda), _altura(no.direita))

        return _balancear(no)

    def deletar(self, nome):
        if self.buscar(nome) is None:
            print(f'{nome} NAO ENCONTRADO')
        else:
            self.raiz = self._deletar(self.raiz, nome)
            print(f'{nome} REMOVIDO')

    def _deletar(self, no, nome):
        if no is None:
            return no

        if nome < no.nome:
            no.esquerda = self._deletar(no.esquerda, nome)
        elif nome > no.nome:
            no.direita = self._deletar(no.direita, nome)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            else:
                sucessor = _encontrar_minimo(no.direita)
                no.nome = sucessor.nome
                no.direita = self._deletar(no.direita, sucessor.nome)

        no.altura = 1 + max(_altura(no.esquerda), _altura(no.direita))

        return _balancear(no)

    def buscar(self, nome):
        return self._buscar_recursivo(self.raiz, nome)

    def _buscar_recursivo(self, no, nome):
        if no is None or no.nome == nome:
            return no
        if nome < no.nome:
            return self._buscar_recursivo(no.esquerda, nome)
        else:
            return self._buscar_recursivo(no.direita, nome)

    def pre_ordem(self):
        if self.raiz is None:
            print('ARVORE VAZIA')
            print("FIM. ALTURA: -1")
        else:
            resultado = []
            self._pre_ordem(self.raiz, resultado)
            print(' -> '.join(resultado), f'-> FIM. ALTURA: {self.raiz.altura - 1}')

    def _pre_ordem(self, no, resultado):
        if no is not None:
            resultado.append(no.nome)
            self._pre_ordem(no.esquerda, resultado)
            self._pre_ordem(no.direita, resultado)


def _encontrar_minimo(no):
    atual = no
    while atual.esquerda is not None:
        atual = atual.esquerda
    return atual


def _altura(no):
    if no is None:
        return 0
    return no.altura


def _balanceamento(no):
    if no is None:
        return 0
    return _altura(no.esquerda) - _altura(no.direita)


def _rotacao_esquerda(z):
    y = z.direita
    t2 = y.esquerda

    y.esquerda = z
    z.direita = t2

    z.altura = 1 + max(_altura(z.esquerda), _altura(z.direita))
    y.altura = 1 + max(_altura(y.esquerda), _altura(y.direita))

    return y


def _rotacao_direita(no_z):
    no_y = no_z.esquerda
    t3 = no_y.direita

    no_y.direita = no_z
    no_z.esquerda = t3

    no_z.altura = 1 + max(_altura(no_z.esquerda), _altura(no_z.direita))
    no_y.altura = 1 + max(_altura(no_y.esquerda), _altura(no_y.direita))

    return no_y


def _balancear(no):
    balanceamento = _balanceamento(no)

    if balanceamento > 1:
        if _balanceamento(no.esquerda) >= 0:
            return _rotacao_direita(no)
        else:
            no.esquerda = _rotacao_esquerda(no.esquerda)
            return _rotacao_direita(no)

    elif balanceamento < -1:
        if _balanceamento(no.direita) <= 0:
            return _rotacao_esquerda(no)
        else:
            no.direita = _rotacao_direita(no.direita)
            return _rotacao_esquerda(no)

    return no


arvore = Arvore()
running = True

while running:
    COMANDO = input().split()
    OPERACAO = COMANDO[0]
    if len(COMANDO) > 1:
        NOME = COMANDO[1]
    else:
        NOME = ""

    if OPERACAO == "INSERIR":
        arvore.inserir(NOME)
    elif OPERACAO == "DELETAR":
        arvore.deletar(NOME)
    elif OPERACAO == "FIM":
        arvore.pre_ordem()
        running = False
