'''
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''

lado_quad = float(input('Digite o valor do lado do quadrado: '))
area_quad = lado_quad ** 2
dobro_area = area_quad * 2

print(f'A área do quadrado é {area_quad}. \nO dobro da área é {dobro_area}.')
