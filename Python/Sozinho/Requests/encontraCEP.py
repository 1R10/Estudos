import requests

def encontrarCEP(cep):
    url = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
    cidade = url['localidade']
    return url, cidade





def exibir_endereço(url):    
    for dado in url:
        print(f'{dado}: {url[dado]}')
        