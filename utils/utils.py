inputs = {
    1: '1. Para listar todos os pilotos já cadastrados no sistema de rachas',
    2: '2. Para listar todos os carros já cadastrados',
    3: '3. Para adicionar um novo piloto à lista de possíveis competidores',
    4: '4. Para adicionar um novo carro ao sistema',
    5: '5. Para tornar um dos pilotos já cadastrados calvo',
    6: '6. Para adicionar turbo a um dos carros do sistema',
    7: '7. Para remover um piloto ou carro do sistema',
    8: '8. DISPUTA DE RACHA!!!\n',
}


def generateOptionStr():
    opts = ''

    for option in inputs:
        opts = opts + inputs[option] + '\n'

    return opts


def divider():
    print('\n', 80*'_', '\n')
