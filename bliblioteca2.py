class ContaBancaria:

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
            print("Sua conta esta ativa.")



