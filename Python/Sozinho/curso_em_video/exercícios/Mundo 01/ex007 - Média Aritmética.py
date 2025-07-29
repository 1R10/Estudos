#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota_um   = int(input('Nota um:'))
nota_dois = int(input('Nota dois:'))

media_ari = (nota_um + nota_dois)/2
print(f'A média entre {nota_um} e {nota_dois} é {media_ari}.')
