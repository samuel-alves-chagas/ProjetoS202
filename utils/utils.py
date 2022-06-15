import random

inputs = {
    1: '1. Para listar todos os pilotos já cadastrados no sistema de rachas',
    2: '2. Para listar todos os carros já cadastrados',
    3: '3. Para listar as relações entre os pilotos e os carros',
    4: '4. Para adicionar um novo piloto à lista de possíveis competidores',
    5: '5. Para adicionar um novo carro ao sistema',
    6: '6. Para adicionar uma nova relação entre piloto e carro',
    7: '7. Para tornar um dos pilotos já cadastrados calvo',
    8: '8. Para adicionar turbo a um dos carros do sistema',
    9: '9. Para remover um piloto ou carro do sistema',
    10: '10. DISPUTA DE RACHA!!!\n',
}


def generateOptionStr():
    opts = ''

    for option in inputs:
        opts = opts + inputs[option] + '\n'

    return opts


def divider():
    print('\n', 80*'_', '\n')


def probabilidadeDeVencer(piloto, carro):
    calculoBase = piloto['habilidade'] * carro['cavalos']
    calculoComTurbo = calculoBase * 1.25 if carro['turbo'] else calculoBase
    if piloto['calvo'] and random.randint(0, 10) > 8:
        return calculoComTurbo * 2
    else:
        return calculoComTurbo
