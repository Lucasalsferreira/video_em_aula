import random
n1 = str(input('Escolha o primeiro aluno: '))
n2 = str(input('Escolha o segundo aluno: '))
n3 = str(input('Escolha o terceiro aluno: '))
n4 = str(input('Escolhao quarto aluno: '))
lista = [n1, n2, n3, n4]
escolha = random.choice(lista)
print('O nome escolhido é {}'.format(escolha))
