# jogo da adivinhação
from random import randint
print('\n')
print('**************************************')
print('Seja bem vindo ao jogo de adivinhação!')
print('**************************************')
# pular linha
print('\n')
print('Você tem 3 tentativas!')

numero_secreto = randint(1, 10)
numero_escolhido = 0
tentativas = 3
status = True

try:
    while numero_secreto != int(numero_escolhido):        
        numero_escolhido = input('Escolha um número de 1 a 10: ')
        tentativas -= 1
        print(f'Você tem mais: {tentativas} tentativas!')
        if int(numero_escolhido) == numero_secreto:
            print(f'Parabéns você acertou! O numero secreto era {numero_secreto}!')
        elif int(numero_escolhido) < numero_secreto:
                print(f'Numero escolhido {numero_escolhido} é menor que o numero secreto!')
        elif int(numero_escolhido) > numero_secreto:
            print(f'Numero escolhido {numero_escolhido} é maior que o numero secreto!')
        if tentativas < 1:
            numero_escolhido = numero_secreto
            print(f'Fim das tentativas! numero secreto era: {numero_secreto}!')
except ValueError:
    print('Você não digitou um número entre 1 a 10!')

