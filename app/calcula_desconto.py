import json

def lambda_handler(event, context): 
    print('Realizando calculo do desconto ...')
    print(event)
    taxa_calculada = event['resultadoCalculoTaxa']['valorTaxa']
    desconto_percent = float(event['dynamoResult']['item']['oferta']['M']['valor']['N'])
    nova_taxa = round(taxa_calculada * (desconto_percent/100),2)
    print(f'taxa calculado = {nova_taxa}')
    return nova_taxa