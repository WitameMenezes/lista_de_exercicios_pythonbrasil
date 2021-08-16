'''
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte
fórmula: (72.7*altura) - 58.
'''

altura = float(input('Digite a sua altura em centímetros: '))
peso_ideal = (72.2 * altura / 100) - 58

print('O seu peso ideal, de acordo com sua altura é {:.1f}.'.format(peso_ideal))
