import random
aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))

lista_alunos = [aluno1, aluno2, aluno3, aluno4]
print(lista_alunos)
lista_alunos.sort()

print(f'A ordem dos alunos será:{lista_alunos}')