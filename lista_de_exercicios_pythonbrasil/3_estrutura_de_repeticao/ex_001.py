'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

notas = float(input('Digite uma nota entre 0 e 10: '))

while notas < 0 or notas > 10:
    print('Valor inválido!')
    notas = float(input('Digite uma nota entre 0 e 10: '))
else:
    print('Valor válido! Programa encerrado com sucesso!')
