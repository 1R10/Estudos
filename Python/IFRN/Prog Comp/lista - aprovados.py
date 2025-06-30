from random import randint

# Cores para aprovado/reprovado
verde    = '\033[92m'
vermelho = '\033[91m'
branco   = '\033[0m'
azul     = '\033[94m'

# Listas
lstnomes = ['Scooby-Doo'       , 'Fred Flintstone', 'Zé Colmeia' , 'Dom Pixote'     , 
            'Muttley'          , 'Binicão'        , 'Tutubarão'  , 'Capitão Caverna', 
            'Formiga Atômica'  , 'Jonny Quest'    , 'Space Ghost', 'Manda-Chuva'    , 
            'Barney Rubble'    , 'Salsicha'       , 'Falcão Azul', 'Batatinha'      , 
            'Penélope Charmosa', 'Pepe Legal'     , 'Catatau'    , 'Dick Vigarista' ]

lstnotas      = []
lstnotasoma   = []
lstmedia      = []

# Dar 3 notas para cada nome
for nome in range(len(lstnomes)):
    lstnotas.append([randint(0,100),
                     randint(0,100),
                     randint(0,100)])

# Somar estas notas   
for pos in range(len(lstnotas)):
    lstnotasoma.append(sum(lstnotas[pos]))

# Fazer as médias
for pos in range(len(lstnotasoma)):
    lstmedia.append(round(lstnotasoma[pos]/3))

# Dar o veredito
for pos in range(len(lstnomes)):
    if lstmedia[pos] >= 60: 
        aprovado = f'{verde}aprovado{branco}'
    else:
        aprovado = f'{vermelho}reprovado{branco}'
    print(f'{azul}{lstnomes[pos]}{branco} foi {aprovado} com {lstmedia[pos]}  ')
