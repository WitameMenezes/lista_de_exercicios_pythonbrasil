'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''

temp_C = float(input('Digite a temperatura em Celcius: '))
temp_F = (temp_C * 9/5) + 32

print('A temperatura em Celcius informada equivale a {:.1f} graus Fahrenheit.'.format(temp_F))
