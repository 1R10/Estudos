soma = 2 + 3
for n in range(4, 2000000):
    ndiv = 0
    print(n)
    for div in range(2,n//2 +1):
        if n % div == 0:
            ndiv += 1
            break
        if ndiv == 0:
            soma += 1
        if n % 10000 == 0:
            print(n)
print(soma)
