import json

defined_props = {}

def lambda_handler(event, context): 
    flags = {}
    formula = event['dynamoResult']['item']['formula']['S']
    print(f'Preparando para calcular taxa com base na fórmula = {formula}')
    print(f'Input = {event}')
    
    if 'flags' in event['dynamoResult']['item']:
        flags = event['dynamoResult']['item']['flags']['S']
        print(f'flags = {flags}')
    
    piso = float(event['dynamoResult']['item']['catalogo']['M']['piso']['N'])
    teto = float(event['dynamoResult']['item']['catalogo']['M']['teto']['N'])
    taxa_calculada = calc(formula, config_defined_props(event))
    print(f'taxa calculada = {taxa_calculada}')
    
    if not 'ignorar_piso_teto' in flags:
      taxa_calculada = teto if taxa_calculada > teto else (piso if taxa_calculada < piso else taxa_calculada)
      print(f'taxa calculada após aplicação do piso/teto = {taxa_calculada}')
    
    return taxa_calculada

def config_defined_props(event):
    if 'init_props' in event['dynamoResult']['item']:
      init_props(event['dynamoResult']['item']['init_props']['S'])
    
    defined_props['evento.valor'] = event['valor_transacao']
    defined_props['catalogo.valor'] = float(event['dynamoResult']['item']['catalogo']['M']['valor']['N'])
    defined_props['oferta.valor'] = float(event['dynamoResult']['item']['oferta']['M']['valor']['N'])
    print(f'Props = {defined_props}')
    return defined_props

def calc(formula, props):
    for prop in props:
        formula = formula.replace(prop, str(props[prop]))
    print(f'Fórmula Parsed = {formula}')
    return eval(formula)

def init_props(props):
    print(f'Iniciando props solicitadas = {props}')
    listprops = props.split(',')
    init_boletos(listprops)
    init_fundos_investimentos(listprops)
    

def init_boletos(listprops):
    print('iniciando prop boletos')
    if 'boletos' in listprops:
        defined_props['boletos.consolidado_diario'] = 400
    
def init_fundos_investimentos(listprops):
    print('iniciando prop fundos_investimentos')
    if 'fundos_investimentos' in listprops:
        defined_props['fundos_investimentos.consolidado_mensal'] = 700
        