primeiro_termo = int(input('Digite o valor do primeiro termo da P.A: '))
razao          = int(input('Digite a razão da P.A: '))
decimo_termo   = primeiro_termo + (10 - 1) * razao

for n in range(primeiro_termo, decimo_termo + razao, razao):
    print(f'{n}', end=' -> ')