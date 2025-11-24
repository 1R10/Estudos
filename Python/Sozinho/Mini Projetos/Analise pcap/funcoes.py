import requests, zipfile, struct

#pcap = 'https://malware-traffic-analysis.net/2025/10/08/2025-10-08-initial-infection-traffic-from-Kongtuke-ClickFix-page.pcap.zip'

# Area de links ----------------------------------------------------------------------------------------------

def tratar_url(pcap:str):
    if pcap.find('https://') != 0: 
        pcap = 'https://' + pcap

    if pcap.find('.pcap') < 1: 
        print('O link é inválido.')
        pcap = ''
    
    return pcap

def baixar_pcap(pcap: str):
    try:
        url_pcap = requests.get(pcap)
        with open('arquivo.pcap', 'wb') as arq: 
            arq.write(url_pcap.content) 
            
    except ConnectionError:
        print('Erro de conexão.')
    except Exception as e:
        print(f'Ocorreu um erro no download: {e}') 

def descompactar(pcap:str): 
    try:
        datas  = pcap.split('/') 
        senha  = f'infected_{datas[3]}{datas[4]}{datas[5]}'.encode('utf-8')
        vsenha =  'infected'.encode('utf-8')
    
        with zipfile.ZipFile('arquivo.pcap', 'r') as arq:
            try:
               arq.extractall(pwd = senha) 
            except:
               arq.extractall(pwd = vsenha) 
                
            return arq.namelist()[0] # apenas o primeiro (e neste caso único) arquivo do zip

    except Exception as e:
        print(f'Ocorreu um erro na descompactação: {e}')
        return None

# Area de análise ----------------------------------------------------------------------------------------------

def dict_stats():
    return {
        'tempo_inicial': None,
        'tempo_final': None,
        'maior_tcp': 0,
        'tcp_Nsalvo': 0,
        'soma_udp': 0,
        'qtd_udp': 0,
        'ips_unicos': set(),
        'trafego_pares': {}
    }

def processar_ipv4(dados: bytes, stats:dict, tamanho_capturado: int, tamanho_real: int):
    # parsing do IP, TCP e UDP.
    
    
    # IP
    cabecalho_ip = dados[14 : 34] # 14 (Ethernet) + 20 (cabeçalho mínimo)

    byte_versao_ihl = cabecalho_ip[0]
    blocos_cabecalho = byte_versao_ihl & 15
    cabecalho_ip_len = blocos_cabecalho * 4 # conta de 4 em 4
    len_pacote_completo = struct.unpack('!H', cabecalho_ip[2:4])[0]
    protocolo = cabecalho_ip[9]

    origem = f'{dados[26]}.{dados[27]}.{dados[28]}.{dados[29]}'
    destino = f'{dados[30]}.{dados[31]}.{dados[32]}.{dados[33]}'
    
    # Atualiza ip unico
    stats['ips_unicos'].add(origem)
    stats['ips_unicos'].add(destino)

    # lógica dos pares
    if origem < destino:
        par = (origem, destino)
    else:
        par = (destino, origem)

    if par in stats['trafego_pares']:
        stats['trafego_pares'][par] += 1
    else:
        stats['trafego_pares'][par] = 1

    # TCP
    if protocolo == 6:
        tcp_len = len_pacote_completo - cabecalho_ip_len

        if tcp_len > stats['maior_tcp']: 
            stats['maior_tcp'] = tcp_len
        
        if tamanho_capturado < tamanho_real: 
            stats['tcp_Nsalvo'] += 1

    # UDP
    if protocolo == 17:
        udp_start = 14 + cabecalho_ip_len
        if len(dados) >= udp_start + 6:
            u_len = struct.unpack('!H', dados[udp_start +4: udp_start + 6])[0]
            stats['soma_udp'] += u_len
            stats['qtd_udp'] += 1

def mostrar_resultados(stats:dict):
    
    if stats['qtd_udp'] > 0:
        media_udp = stats['soma_udp'] / stats['qtd_udp']
    else:
        media_udp = 0
    
    maior_par_str = 'Nenhum'
    maior_qtd = 0
    for par, quantidade in stats['trafego_pares'].items():
        if quantidade > maior_qtd:
            maior_qtd = quantidade
            maior_par_str = f'{par[0]} e {par[1]}'

    print(f'\nInício da captura de pacotes: {stats["tempo_inicial"]}'            ,
          f'\nFinal da captura de pacotes: {stats["tempo_final"]}'               ,
          f'\nTamanho do maior TCP pacote capturado: {stats["maior_tcp"]}'       ,
          f'\nPacotes TPCs não salvos: {stats["tcp_Nsalvo"]}'                    ,
          f'\nTamanho médio dos pacotes UDP capturados: {media_udp:.2f}'         ,
          f'\nPar de IP com maior tráfego: {maior_par_str} ({maior_qtd} pacotes)',
          f'\nQuantidade de IPs interagidos: {len(stats["ips_unicos"])}'          )

# Area de análise ----------------------------------------------------------------------------------------------

def analisar_arq_pcap(arquivo_local:str): 
    
    stats = dict_stats()
    
    try:
        if not arquivo_local: 
            return None 

        with open(arquivo_local, 'rb') as arq: 
            arq.read(24) # pula os primeiros 24b de cabeçalho

            while True:
                header = arq.read(16) 
                if len(header) < 16: 
                    break

                segundos = struct.unpack('<I', header[0:4])[0]
                microssegundos = struct.unpack('<I', header[4:8])[0]
                tamanho_capturado = struct.unpack('<I', header[8:12])[0]
                tamanho_real = struct.unpack('<I', header[12:16])[0]
                
                tempo_atual = segundos + (microssegundos / 1000000.0)

                # Atualiza tempo no dicionário
                if stats['tempo_inicial'] == None: 
                    stats['tempo_inicial'] = tempo_atual
                stats['tempo_final'] = tempo_atual

                dados = arq.read(tamanho_capturado)

                
                if len(dados) >= 14 and struct.unpack('!H', dados[12:14])[0] == 2048: # verifica se é IPv4 (Bytes 12-13 == 2048)
                    processar_ipv4(dados, stats, tamanho_capturado, tamanho_real)
        mostrar_resultados(stats)

    except Exception as e:
        print(f'Ocorreu um erro na análise: {e}')

def main(pcap):
    url_tratada = tratar_url(pcap)
    if url_tratada:
        baixar_pcap(url_tratada)
        nome_do_arquivo = descompactar(url_tratada)
        if nome_do_arquivo:
            analisar_arq_pcap(nome_do_arquivo)
