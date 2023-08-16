class Rede:
    def __init__(self, usuarios, conexoes):
        self.usuarios = usuarios
        self.conexoes = conexoes

    def get_conexoes(self, num_pessoa):
        dados_usuario = None

        for usuario in self.usuarios:
            if usuario["id"] == num_pessoa:
                dados_usuario = usuario
                break

        nome = dados_usuario["nome"]
        amigos = []

        for conexao in self.conexoes:
            if num_pessoa in conexao:
                num_amigo = conexao[0] if conexao[0] != num_pessoa else conexao[1]

                for usuario in self.usuarios:
                    if usuario["id"] == num_amigo:
                        amigos.append(usuario["nome"])

        quantidade = len(amigos)
        amigos = sorted(amigos)
        amigos = ", ".join(amigos)

        return nome, quantidade, amigos


USUARIOS = eval(input())
CONEXOES = eval(input())
NUMERO = eval(input())

rede = Rede(USUARIOS, CONEXOES)
NOME, QUANTIDADE, AMIGOS = rede.get_conexoes(NUMERO)
print(f"O usuário {NOME} tem {QUANTIDADE} conexões, e seus amigos são: {AMIGOS}.")
