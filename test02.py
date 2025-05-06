from bliblioteca import Pessoa
aluno01=Pessoa("ygor",18,120.00)
aluno02=Pessoa("vitor",20,76)
print(f"o nome ddo aluno é :{aluno01.nome}, ele tem a idade de {aluno01.idade}anos e pesa:{aluno01.peso}")
print(f"o nome ddo aluno é :{aluno02.nome}, ele tem a idade de {aluno02.idade}anos e pesa:{aluno02.peso}")
aluno02.falar()
aluno02.comer("pipoca")
aluno02.dormir()