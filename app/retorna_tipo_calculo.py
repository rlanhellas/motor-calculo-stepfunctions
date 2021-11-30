import json

def lambda_handler(event, context): 
    print('Verifica o tipo do calculo: AVULSO ou PLANO.')
    print(event)
    try:
        pacote = event['dynamoResult']['item']['catalogo']['M']['pacote']
        event['dynamoResult']['item']['catalogo']['M']['grupo']
        if (pacote['S'] == 'ISENTO'):
            return "ISENTO"
        else:
          return "PLANO"
    except KeyError:
        return "AVULSO"    