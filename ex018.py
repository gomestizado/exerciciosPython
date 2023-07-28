from math import cos, sin, tan, radians

angulo = int(input('Digite o ângulo: '))

radiano = radians(angulo)

print('\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sin(radiano), cos(radiano), tan(radiano)))
