while True:
    numero = int(input('\nDigite um número:'))
    divisao = 0

    for n in range(1, numero+1):
        if numero % n == 0: 
            divisao += 1
            print(n,'<<<')
        else: print(n)

    if divisao != 2: print(f'O número não é primo e foi dividido {divisao} vezes.')
    else: print('O número é primo')

    continuar = input('Deseja continuar?(s/n)').lower().strip()
    if continuar != 's': break
   