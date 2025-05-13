"""class ContaBancaria:

    def __init__(self,numero,nome,tipo,limite=0.0):
        self.numero=numero
        self.saldo=0.0
        self.nome=nome
        self.tipo=tipo
        self.status=True
        self.limite=limite


    def deposito(self,valor):

        if self.status:
            self.saldo+=valor
            print(f"Receba seu Deposito:{valor:.2f}.Realizado")

        else:
            print("Deposito não realizado")

    def  sacar(self,valor):

        if self.status and 0< valor <=self.saldo:
            self.saldo-=valor
            print(f"Seu Saque de {valor:.2f}. foi Realizado")

        if 0 < valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f"seu limite de saldo:{valor:.2f}")

        else:
            print("Saque não Realizado.")

    def verificar(self):
        print(f"Verificação de Saldo:{self.saldo:.2f} ")
        return self.saldo

    def desativar_conta(self):
        if self.saldo==0:
            self.status=False
            print("sua conta esta desativada .")
        else:
            print("Sua conta esta ativa.")

    def ativar_conta(self):
        if self.saldo>=0:
            self.status=True
            print("Sua conta esta ativa.")"""


"""class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer...")
        
    def dormindo(self):
        print(f"{self.nome} está dormindo....")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"O {self.nome} foi miando...")


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f"O {self.nome} esta latindo...")

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def mugir(self):
        print(f"A {self.nome} esta mugindo....mu mu mu mu ")

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def guinchar(self):
        print(f"O {self.nome} está guichando....")"""

"""class Ingresso:
    def __init__(self,valor):
        self.valor=valor

    def imprimavalor(self):
        print(f"O valor do ingresso normal é de {self.valor}")

class Vip(Ingresso):

    def __init__(self,valor):
        super().__init__(valor)
        self.valor*=1.5

        print(f"O valor do vip é de {valor}")"""

"""class Forma:
    def __init__(self):
        self.area=0
        self.perimetro=0

    def calculararea(self):
            pass

    def calculaperimtro(self):
            pass



class Retangulo(Forma):
    def __init__(self):
        super().__init__()
        

    def calculaArea(self,base,altura):
        self.area=base * altura
        print(f"a area e de {self.area}")
    

    def calculaperimtro(self,base,altura):
        self.perimetro=2*(altura+base)
        print(f"o perimetro e de {self.perimetro}")

class Triangulo(Forma):
    def __init__(self,altura,base,largura):
        super().__init__(area,perimetro)
        self.altura=altura
"""

class Atleta:
    def __init__(self,aposentado,peso=0.0):
        self.peso=peso
        self.aposentado=aposentado
        self.aquecer=False

    def aquecer(self):
        if not self.aposentado:
            self.aquecer=True
            print("o atleta aquece")
        else:
            print("o atleta não aquece")
    def aposentado(self):
        if not self.aquecer:
            self.aquecer=True
            print("o atleta esta aposentado")

        else:
            print("o atleta aquece")




