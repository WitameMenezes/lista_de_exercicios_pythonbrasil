'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

letra = str(input('Digite uma letra qualquer: ')).upper()

if letra.isalpha():
    if letra == 'A':
        print('A letra é uma vogal!')
    elif letra == 'E':
        print('A letra é uma vogal!')
    elif letra == 'I':
        print('A letra é uma vogal!')
    elif letra == 'O':
        print('A letra é uma vogal!')
    elif letra == 'U':
        print('A letra é uma vogal!')
    else:
        print('A letra é uma consoante!')
else:
    print('Você não digitou uma letra!')
