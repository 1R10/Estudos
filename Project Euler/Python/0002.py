fibo_um   = 1
fibo_dois = 2
soma = 0

while fibo_dois <= 4000000:
    if fibo_dois % 2 == 0:
        soma += fibo_dois
    fibo_sequente = fibo_dois + fibo_um
    fibo_um = fibo_dois
    fibo_dois = fibo_sequente
print(soma)
