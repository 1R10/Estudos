while True:

    n1 = int(input('\nDigite um termo para a sequencia de fibonacci: '))
    elementos = int(input('Quantos elementos você deseja ver? '))

    for e in range(0, elementos + 1):
        print(n1)
        n2 = n1 + n1
        print(n2)
        n3 = n1 + n2
        print(n3)
        n1 = n2 + n3
        print(n1)
        n2 = n1 + n3
        print(n2)
