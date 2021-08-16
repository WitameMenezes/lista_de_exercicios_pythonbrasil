'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a) o produto do dobro do primeiro com metade do segundo .
    b) a soma do triplo do primeiro com o terceiro.
    c) o terceiro elevado ao cubo.
'''

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
num_3 = float(input('Digite o terceiro número: '))

calc_a = (num_1 * 2) * (num_2 / 2)
calc_b = (num_1 * 3) + num_3
calc_c = (num_3) ** 3

print('O produto do dobro do primeiro com metade do segundo é {:.1f}.'.format(calc_a))
print('A soma do triplo do primeiro com o terceiro é {:.1f}'.format(calc_b))
print('O terceiro elevado ao cubo é {:.1f}'.format(calc_c))
