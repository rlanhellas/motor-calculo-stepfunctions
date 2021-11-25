import json

def lambda_handler(event, context): 
    print('Realizando calculo da taxa ...')
    print(event)
    valor_transacao = event['valor_transacao']
    catalogo_valor = float(event['dynamoResult']['item']['catalogo']['M']['valor']['N'])
    piso = float(event['dynamoResult']['item']['catalogo']['M']['piso']['N'])
    teto = float(event['dynamoResult']['item']['catalogo']['M']['teto']['N'])
    taxa = round(valor_transacao * (catalogo_valor/100),2)
    taxa = teto if taxa > teto else (piso if taxa < piso else taxa)
    print(f'taxa calculado = {taxa}')
    return taxa