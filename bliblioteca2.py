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
        self.area = 0
        self.perimetro = 0

    def calcularArea(self):
        pass

    def calcularPerimetro(self):
        pass


class Retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcularArea(self):
        self.area = self.base * self.altura
        print(f"A área do retângulo é {self.area}")

    def calcularPerimetro(self):
        self.perimetro = 2 * (self.base + self.altura)
        print(f"O perímetro do retângulo é {self.perimetro}")


class Triangulo(Forma):
    def __init__(self, base, altura, lado2, lado3):
        super().__init__()
        self.base = base
        self.altura = altura
        self.lado2 = lado2
        self.lado3 = lado3

    def calcularArea(self):
        self.area = (self.base * self.altura) / 2
        print(f"A área do triângulo é {self.area}")

    def calcularPerimetro(self):
        self.perimetro = self.base + self.lado2 + self.lado3
        print(f"O perímetro do triângulo é {self.perimetro}")

"""
"""
class Atleta:
    def __init__(self,aposentado,peso):
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
            print("o atleta está aposentado")

        else:
            print("o atleta aquece")

class Corredor(Atleta):
    def __init__(self,aposentado,peso):
        super().__init__(aposentado,peso)

    def corre(self):
        if not self.aposentado:
            self.aquecer=True
            print("corredor esta aquecido,por tanto ele esta correndo")

        else:
            print("corredor esta aposentado")
class Nadador(Atleta):
    def __init__(self,aposentado,peso):
        super().__init__(aposentado,peso)
    def nadar(self):
        if not self.aquecer:
            self.aquecer=True
            print("o nadador esta aquecido,ele ja pode nadar")
        else:
            print("nadador esta aposentado ele não pode mas nadar")
class Ciclista(Atleta):
    def __init__(self,aposentado,peso):
        super().__init__(aposentado,peso)
    def pedalar(self):
        if not self.aquecer:
            self.aquecer=True
            print("O ciclista está pedalando.")
        else:
            print("O ciclista está aposentado.")
class Triatleta(Corredor,Nadador,Ciclista):
    def __init__(self,aposentado,peso):
        super().__init__(aposentado,peso)
    def poliatleta(self):
        if not self.aquecer:
            self.aquecer=True
            print("ele é um triatleta.")
        else:
            print("ele não e um triatleta.")
"""
class Atleta:
    def __init__(self, aposentado, peso):
        self.peso = peso
        self.aposentado = aposentado
        self.esta_aquecido = False

    def aquecer(self):
        if not self.aposentado:
            self.esta_aquecido = True
            print("O atleta está aquecendo.")
        else:
            print("O atleta está aposentado e não pode aquecer.")


class Corredor(Atleta):
    def corre(self):
        if self.aposentado:
            print("O corredor está aposentado e não pode correr.")
        elif not self.esta_aquecido:
            print("O corredor precisa aquecer antes de correr.")
        else:
            print("O corredor está correndo.")


class Nadador(Atleta):
    def nadar(self):
        if self.aposentado:
            print("O nadador está aposentado e não pode nadar.")
        elif not self.esta_aquecido:
            print("O nadador precisa aquecer antes de nadar.")
        else:
            print("O nadador está nadando.")


class Ciclista(Atleta):
    def pedalar(self):
        if self.aposentado:
            print("O ciclista está aposentado e não pode pedalar.")
        elif not self.esta_aquecido:
            print("O ciclista precisa aquecer antes de pedalar.")
        else:
            print("O ciclista está pedalando.")


class Triatleta(Corredor, Nadador, Ciclista):
    def poliatleta(self):
        if self.aposentado:
            print("O triatleta está aposentado e não compete mais.")
        else:
            print("O triatleta participa das três modalidades.")


