#1) Quantos pedidos houve em cada data/hora/minuto?
d_DataHora = {}
with open("apache.logs", "r") as apache:
    for linha in apache:
        tamanho_DataHora = linha.find(']') - linha.rfind('[') # 27


        


