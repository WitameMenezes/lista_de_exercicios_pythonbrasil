'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''

temp_F = float(input('Digite a temperatura em Fahrenheit: '))
temp_C = 5 * ((temp_F - 32) / 9)

print('A temperatura em graus Fahrenheit informada equivale a {:.1f} Celcius.'.format(temp_C))
