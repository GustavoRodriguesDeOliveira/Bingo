from random import randint
from time import sleep
from operator import itemgetter

bingo = {'CLiente 1': randint(1, 100),
        'Cliente 2': randint(1, 100),
        'CLiente 3': randint(1, 100),
        'Cliente 4': randint(1, 100),
        'Cliente 5': randint(1, 100),
        'Cliente 6': randint(1, 100),
        'CLiente 7': randint(1, 100),
        'CLiente 8': randint(1, 100),
        'Cliente 9': randint(1, 100),
        'CLiente 10': randint(1, 100)}
ranking = dict()
print('Valores sorteados: ')
for p, b in bingo.items():
        print(f'{p} tirou {b} no bingo.')
        sleep(2)
ranking = sorted(bingo.items(), key=itemgetter(1), reverse=True)
print(' π³π§π°π§π°π§π°π§π°π§ π³' * 70)
print('π°π°π° GANHADORES DO BINGO DA 3Βͺ IDADE π°π°π°')
for g, j in enumerate(ranking):
        print(f'  {1+g}ΒΊ lugar: {j[0]} com {j[1]}.')
        sleep(2)