'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

seu_nome = str(input('Digite seu nome: '))
turno_de_estudo = str(input('Digite o seu turno de estudo: M - Matutino | V - Verpertino | N - Noturno: ')).upper()

if turno_de_estudo == 'M':
    print('Bom dia, {}. Bons estudos!'.format(seu_nome))
elif turno_de_estudo == 'V':
    print('Boa tarde, {}. Bons estudos!'.format(seu_nome))
elif turno_de_estudo == 'N':
    print('Boa noite, {}. Bons estudos!'.format(seu_nome))
else:
    print('Valor Invalido!')
