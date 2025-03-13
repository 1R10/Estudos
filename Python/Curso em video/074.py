import random

n = (random.randint(0,10), random.randint(0,10), random.randint(0,10),
      random.randint(0,10), random.randint(0,10))
s = sorted(n)
print(f'\nOs números sorteados foram: {s}')
print(f'O menor número foi {s[0]} e o maior foi {s[4]}')

