import math
fator = 'n'
while True:
    n = int(input('\nQual o número para ver o fatorial? '))
    fatorial = math.factorial(n)
    while n in fatorial:
        fator = n-1
        print(fator)