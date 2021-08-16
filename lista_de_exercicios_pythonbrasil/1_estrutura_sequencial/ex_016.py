'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.
'''

import math

area_pintar = float(input('Digite a area, em metros quadrados, a ser pintada: '))
qtde_litros = area_pintar / 3
qtde_latas = math.ceil(qtde_litros / 18)
custo_tinta = qtde_latas * 80

print('A quantidade de latas tinta a serem compradas é de {} latas. E isso custará R$ {}.'.format(qtde_latas, custo_tinta))
