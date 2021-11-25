import json

def lambda_handler(event, context): 
    print('Verifica o tipo do calculo: AVULSO ou PLANO.')
    print(event)
    try:
        event['dynamoResult']['item']['catalogo']['M']['pacote']
        event['dynamoResult']['item']['catalogo']['M']['grupo']
        return "PLANO"
    except KeyError:
        return "AVULSO"    