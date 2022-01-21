import random

def dice(value):
    number = random.randint(1 , value)
    print(f'O numero que caiu foi {number}')
    
while True:
    lados  = input('Vai querer o dado de quantos lados? ')
    print('O dado ira rolar')
    dice(int(lados))
    resposta = input('Quer rolar outro dado? [s] [n] ')
    if resposta == 'n':
        print('Fim do Programa:')
        break