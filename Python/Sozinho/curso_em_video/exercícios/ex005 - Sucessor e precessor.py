#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um valor: '))
antes  = n - 1
depois = n + 1

print(f'\n Número antecessor: {antes}\nNúmero: {n}\nNúmero sucessor: {depois}')
print(f'Números em ordem:\n{antes}, {n}, {depois}')
