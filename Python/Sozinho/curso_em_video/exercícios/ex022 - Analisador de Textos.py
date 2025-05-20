# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.
nome = str(input('Escreva seu nome completo: '))

print(f'Nome maiúsculo: {nome.upper()}')
print(f'Nome minúsculo: {nome.lower()}')
print(f'Letras totais: {len(nome) - nome.count((' '))}')
print(f'Letras do primeiro nome: {nome.find(' ')}')
