soma = 0

while True:
    n = int(input('Digite um valor. (Para encerrar digite 999): '))
    soma += n
    if n == 999: break
print(f'O resultado da soma dos números digitados foi: {soma-999}')
    