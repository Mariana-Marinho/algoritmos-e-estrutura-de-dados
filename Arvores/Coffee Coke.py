class No:
    def __init__(self, cpf, nome, altura=0):
        self.nome = nome
        self.cpf = cpf
        self.altura = altura
        self.direita = None
        self.esquerda = None
        self.acima = None


def get_min(no):
    atual = no
    while atual.esquerda is not None:
        atual = atual.esquerda
    return atual


class Arvore:
    def __init__(self):
        self.raiz = None

    def set_no(self, cpf, nome):
        if self.raiz is None:
            self.raiz = No(cpf, nome)
        else:
            self.set_no_recursivo(cpf, nome, self.raiz)

    def set_no_recursivo(self, cpf, nome, no):
        if cpf < no.cpf:
            if no.esquerda:
                self.set_no_recursivo(cpf, nome, no.esquerda)
            else:
                no.esquerda = No(cpf, nome)
                no.esquerda.acima = no

        elif cpf > no.cpf:
            if no.direita:
                self.set_no_recursivo(cpf, nome, no.direita)
            else:
                no.direita = No(cpf, nome)
                no.direita.acima = no

    def get_altura(self, cpf):
        altura = 0
        no = self.raiz

        while no is not None:
            if cpf < no.cpf:
                no = no.esquerda
            elif cpf > no.cpf:
                no = no.direita
            else:
                return altura
            altura += 1

        return -1

    def get_no(self, nome):
        if self.raiz is None:
            return None
        return self.get_no_recursivo(nome, self.raiz)

    def get_no_recursivo(self, nome, no):
        if no is None:
            return None
        if no.nome == nome:
            return no

        no_esquerda = self.get_no_recursivo(nome, no.esquerda)
        if no_esquerda:
            return no_esquerda

        no_direita = self.get_no_recursivo(nome, no.direita)
        if no_direita:
            return no_direita

        return None

    def get_remove(self, cpf):
        return self.remove(cpf, self.raiz)

    def remove(self, cpf, no=None):
        if no is None:
            return no

        if cpf < no.cpf:
            no.esquerda = self.remove(no.esquerda, cpf)
        elif cpf > no.cpf:
            no.direita = self.remove(no.direita, cpf)
        else:
            if no.esquerda is None:
                sucessor = no.direita
                no = None
                return sucessor
            elif no.direita is None:
                sucessor = no.esquerda
                no = None
                return sucessor

            sucessor = get_min(no.direita)
            no.cpf = sucessor.cpf
            no.nome = sucessor.name
            no.direita = self.remove(no.direita, sucessor.cpf)

        return no

    def set_nova_raiz(self, no):
        """nao ta certo"""
        if no is None or no.acima is None:
            return

        mae = no.acima
        avo = mae.acima

        if avo is None:
            no.acima = None
            if no.cpf > mae.cpf:
                no.direita = mae
            else:
                no.esquerda = mae
            mae.acima = no
            self.raiz = no
        else:
            if mae == avo.esquerda:
                avo.esquerda = no
            else:
                avo.direita = no

            no.acima = avo

            if no == mae.esquerda:
                mae.esquerda = no.direita
                if no.direita is not None:
                    no.direita.acima = mae
                no.direita = mae
            else:
                mae.direita = no.esquerda
                if no.esquerda is not None:
                    no.esquerda.acima = mae
                no.esquerda = mae

            mae.acima = no

    def get_reacao(self, nome, frase):
        if frase == 'disse que achou a coca saborosa.':
            no = self.get_no(nome)
            altura = self.get_altura(no.cpf)
            self.set_nova_raiz(no)
            print(f'{nome} virou o principal suspeito e estava no nível {altura}.')

        elif frase == 'doou uma coca café para a Taylor!':
            no = self.get_no(nome)
            altura = self.get_altura(no.cpf)
            self.remove(no.cpf)
            print(f'{nome} deixou de ser o principal suspeito e estava no nível {altura}.')

    def get_raiz(self):
        raiz = self.raiz.nome
        return raiz


comando = input().split('---')[1]
arvore = Arvore()
nomes_cpfs = []

if comando == ' SUSPEITOS ':
    while True:
        comando = input().split()
        if comando[0] == 'ADD':
            _, CPF, NOME = comando
            arvore.set_no(CPF, NOME)
            nomes_cpfs.append([CPF, NOME])
        else:
            break

while True:
    reacao = input()
    if reacao == 'FIM':
        break
    else:
        espaco = reacao.find(' ')
        NOME = reacao[0:espaco]
        reacao = reacao[espaco + 1:]

        arvore.get_reacao(NOME, reacao)

RAIZ = arvore.get_raiz()
print(f'{RAIZ} foi declarado o ladrão da coca!')
