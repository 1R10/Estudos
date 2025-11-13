import requests
from encontraCEP import cidade

clima_key = '03c6b6e0248b3a9b794cd9328cd5d674'
clima_link = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={clima_key}&lang=pt_br&units=metric').json()

temperaturas = f'''
Mínima:           {clima_link["main"]["temp_min"]}C°
Máxima:           {clima_link["main"]["temp_max"]}C°
Sensação térmica: {clima_link["main"]["feels_like"]}C°
'''

print(temperaturas)