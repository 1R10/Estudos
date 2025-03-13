import random

pc = random.randint(0,10)
while True:
    parImpar = str(input('Par ou impar? (p/i)')).strip().lower()
    if parImpar != 'p' or parImpar != 'i':
        print(f'{parImpar} Digite P ou I.')