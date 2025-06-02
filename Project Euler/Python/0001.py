# Find the sum of all the multiples of Multiples of 3 or 5 bellow 1000
soma = 0
for n in range(0,1000):
    if n % 3 == 0 or n % 5 == 0:
        soma += n
        print(n)
print(soma)
