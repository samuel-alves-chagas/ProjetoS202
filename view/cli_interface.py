from pprintpp import pprint as pp
from model.motoristaDAO import MotoristaDAO
from model.carroDAO import CarroDAO
from utils.utils import divider, optionStr


def view(connection):

    motoristaDAO = MotoristaDAO(connection)
    carroDAO = CarroDAO(connection)

    while 1:
        option = input(optionStr)
        divider()
        if option == '1':
            motorista = {
                'nome': 'Samuel',
                'cnh': '772712',
                'idade': 21,
                'calvo': False,
                'habilidade': 7.5
            }

            carro = {
                'modelo': 'Corvette',
                'cor': 'prata',
                'cavalos': 217,
                'turbo': False
            }
            motoristaDAO.create(motorista)
            carroDAO.create(carro)

            divider()

        elif option == '2':
            aux = motoristaDAO.read_all()
            pp(aux)
            aux = carroDAO.read_all()
            pp(aux)
            divider()

        elif option == '3':
            motorista = {
                'nome': 'Samuel',
                'calvo': True
            }

            aux = motoristaDAO.update_baldness(motorista)
            pp(aux)

            carro = {
                'modelo': 'Corvette',
                'turbo': True
            }

            aux = carroDAO.update_turbo(carro)
            pp(aux)

            divider()

        elif option == '4':
            motorista = {
                'nome': 'Samuel'
            }
            motoristaDAO.delete(motorista)

            carro = {
                'modelo': 'Corvette'
            }
            carroDAO.delete(carro)

            aux = motoristaDAO.read_all()
            pp(aux)
            aux = carroDAO.read_all()
            pp(aux)

            divider()

        else:
            break
