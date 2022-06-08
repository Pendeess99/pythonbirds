class Pessoa:
    def __init__(self, *filhos,nome=None, idade=23333):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    gabriel = Pessoa(nome='gabriel')
    mendes = Pessoa(gabriel, nome='Mendes')
    print(Pessoa.cumprimentar(mendes))
    print(id(mendes))
    print(mendes.cumprimentar())
    print(mendes.nome)
    print(mendes.idade)
    for filho in mendes.filhos:
        print(filho.nome)
    print(mendes.filhos)