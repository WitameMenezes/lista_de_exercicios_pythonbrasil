'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
M - Masculino, Sexo Inválido.
'''

sexo = str(input('Digite "F" para Faminino ou "M" para Masculino: ')).upper()

if sexo == 'F':
    print('O sexo da pessoa é Feminino.')
elif sexo == 'M':
    print('O sexo da pessoa é Masculino.')
else:
    print('Sexo Invalido!')
