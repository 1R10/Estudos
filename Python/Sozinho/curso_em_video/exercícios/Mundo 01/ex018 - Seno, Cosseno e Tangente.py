import math
angulo = int(input('Digite um ângulo: '))
senO = round(math.sin(angulo),2)
cosO = round(math.cos(angulo),2)
tang = round(math.tan(angulo),2)

print(f'Seno: {senO}\nCosseno: {cosO}\nTangente: {tang}')