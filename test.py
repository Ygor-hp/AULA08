class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
    def apresenta(self):
        return f"óla seu nome é {self.nome} e sua idade é {self.idade}"
pessoa1=Pessoa("ana",21)
print(pessoa1.apresenta())