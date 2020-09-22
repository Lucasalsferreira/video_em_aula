import math
num = float(input('Digite um grau para saber os valores: '))
co = math.cos(math.radians(num))
sen = math.sin(math.radians(num))
tan = math.tan(math.radians(num))
print('O valor de co{:.2f} sen{:.2f} tan{:.2f}'.format(co, sen, tan))

