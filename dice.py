import random

def dice():
    number = random.randint(1 , 6)
    print(f'O numero que caiu foi {number}')
    
while True:
    print('O dado ira rolar')
    dice()
    resposta = input('Quer rolar outro dado? [s] [n]')
    if resposta == 'n':
        break