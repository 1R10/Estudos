# Números amigos até 10000
def d(n):
    soma = 0
    for k in range(1,n):
       if n % k == 0:
          soma += k          
    return soma

for n in range(10000):
    divN = d(n)
    if (n < divN) and (d(divN) == n):
        print(f'amigos: {n} {divN}')
