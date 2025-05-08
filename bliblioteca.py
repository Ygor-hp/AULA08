


class Pessoa:
    def __init__(self,nome,idade,peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.falando=False
        self.dormindo=False
        self.comendo=False

    def falar(self):

        if self.falando==True:
            print("ele ja esta falando")
        elif self.comendo == True:
            print(f" {self.nome} não pode comer, esta falanndo")
        elif self.dormindo == True:
            print(f" {self.nome} não pode dormi pois esta falando")
        else:
            print(f"{self.nome} começou a falar.")

    def parafalar(self):

        if self.falando==True:
            self.falando = False
            print(f"{self.nome} parou de falar")
        else:
            print("ele não esta falando")

    def comer(self,comida):

        if self.comendo==True:
            print("ja esta comendo")
        elif self.dormindo==True:
            print(f"{self.nome} não pode dormi , pois ja esta comendo.")
        elif self.falando==True:
            print(f"{self.nome} não pode falar, pois esta comendo.")
        else:
            print(f"{self.nome} comeu muita {comida}")

    def para_comer(self):
        if self.comendo == True:
            self.comendo=False
            print(f"{self.nome} parou de comer.")
        else:
            print("ele não ta comendo")

    def dormir(self):
        if self.dormindo==True:
            print("ja esta dormindo")
        elif self.comendo==True:
            print(f"{self.nome} não pode comer,pois ja esta dormindo")
        elif self.falando == True:
            print(f"{self.nome} não pode falar,pois esta dormindo.")
        else:
            print(f"{self.nome} começo a dormir")

    def acorda(self):
        if self.falando == True:
            self.falando =  False
            print(f"{self.nome} acordado")
        else:
            print("ja esta acordado")









