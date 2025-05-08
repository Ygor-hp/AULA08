from bliblioteca2 import ContaBancaria

conta=ContaBancaria( "001", "ygor","pupança")
conta.ativar_conta()
conta.deposito(2000)
conta.verificar()
conta.sacar(500)
conta.verificar()