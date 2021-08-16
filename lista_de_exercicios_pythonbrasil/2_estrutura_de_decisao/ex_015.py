'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    Dicas:
        Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
        Triângulo Equilátero: três lados iguais;
        Triângulo Isósceles: quaisquer dois lados iguais;
        Triângulo Escaleno: três lados diferentes;
'''

import math

lado1 = float(input('Digite o valor de um lado do triângulo: '))
lado2 = float(input('Digite o valor de um lado do triângulo: '))
lado3 = float(input('Digite o valor de um lado do triângulo: '))

if math.fabs(lado2 - lado3) < lado1 < lado2 + lado3 and math.fabs(lado1 - lado3) < lado2 < lado1 + lado3 and \
        math.fabs(lado1 - lado2) < lado3 < lado1 + lado2:
    print('Os valores de lado {}, {} e {} formam um triângulo.'.format(lado1, lado2, lado3))
    if lado1 == lado2 == lado3:
        triagulo1 = 'Esses valores formam um Triângulo Equilátero'
        print(triagulo1)
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        triangulo2 = 'Esses valores formam um Triângulo Isósceles'
        print(triangulo2)
    else:
        triangulo3 = 'Esses valores formam um Triângulo Escaleno'
        print(triangulo3)
else:
    print('Esses valores não formam um triângulo!')

