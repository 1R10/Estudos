soma = 0
for s in range(0, 500):
    if s%2 != 0:
        #print(s)
        soma += s
print(f' \nA soma entre todos os números ímpares entre 1 e 500 é {soma}')
'''
for s in range(0, 500):
    if s%2 != 0 and s/3 == 0:
        print(s)
        soma += s
print(f' \nA soma entre todos os números ímpares entre 1 e 500 divisíveis por 3 é {soma}')
'''