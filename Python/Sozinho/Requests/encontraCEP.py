import requests

def buscar_dados(cep):
    url = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
    return url





def limpaCEP(cep: int):
    if cep !=int or len(cep) !=8:
        return False
    return True

def mostra_cep(cep):
    for dados in cep:
        print(f'{dados}: {cep[dados]}')



































def exibir_endereço(url):    
    for dado in url:
        print(f'{dado}: {url[dado]}')
        