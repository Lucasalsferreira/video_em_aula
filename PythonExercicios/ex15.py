d = float(input('quantos dias foi alugado: '))
km = float(input('quantos km foi percorrido: '))
sd = d * 60
skm = km * 0.15
st = sd + skm
print('O valor do dia em aluguel {}'.format(sd))
print('O valor do km percorrido {}'.format(skm))
print('O valor total é {}'.format(st))
