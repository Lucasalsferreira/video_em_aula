import math
num1 = float(input('Me fale o valor do cateto oposto: '))
num2 = float(input('Me fale o valor do cateto adjacente: '))
hyp = math.hypot(num1, num2)
print('O valor da hyp é {:.2f}'.format(hyp))


