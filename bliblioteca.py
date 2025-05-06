from AULA08.test02 import aluno02


class Pessoa:
    def __init__(self,nome,idade,peso,valor):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.valor=valor
        self.falando=False
        self.dormindo=False
        self.comendo=False
    def falar(self):
        if self.falando==True:
            print("não pode comer,pois já ésta comendo")
        print(f"{self.nome} começou a falar.")

    def comer(self,comida):
        print(f"{self.nome} comeu muita {comida}")
    def dormir(self):
        print(f"{self.nome} começo a dormir")

