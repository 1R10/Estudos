import math
co = float(input('Cateto 1: '))
ca = float(input('Cateto 2: '))
hipotenusa = round(math.hypot(co, ca), 2)
print(f'Hipotenusa: {hipotenusa}')