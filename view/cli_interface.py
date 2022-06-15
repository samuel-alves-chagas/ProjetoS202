from pprintpp import pprint as pp
from model.motoristaDAO import MotoristaDAO
from model.carroDAO import CarroDAO
from utils.utils import divider, generateOptionStr


def view(connection):

    motoristaDAO = MotoristaDAO(connection)
    carroDAO = CarroDAO(connection)

    print('Está preparado para disputar grandes rachas entre os personagens de velozes e furiosos?')
    print('Siga os passos abaixo para verificar quem seria o grande vencedor\n')

    while 1:
        option = input(generateOptionStr())
        divider()

        if option == '1':
            print('Você escolheu listar os pilotos cadastrados:')

            results = motoristaDAO.read_all()
            if len(results) > 0:
                print('Estes são todos os pilotos cadastrados até agora')
                data = []
                for record in results:
                    data.append(record['m']._properties)

                for record in data:
                    pp(record)

            else:
                print('Nenhum piloto foi cadastrado até o momento')

            divider()

        elif option == '2':
            print('Você escolheu listar os carros cadastrados:')

            results = carroDAO.read_all()
            if len(results) > 0:
                print('Estes são todos os carros cadastrados até agora:')
                data = []
                for record in results:
                    data.append(record['c']._properties)

                for record in data:
                    pp(record)
            else:
                print('Nenhum carro foi cadastrado até o momento')

            divider()

        elif option == '3':
            print('Você escolheu cadastrar um novo competidor, preencha os dados abaixo')
            nome = input('   O nome do piloto: ')
            cnh = input('   O número da CNH: ')
            idade = input('   A idade: ')
            isCalvo = input('   Ele é calvo? (S=sim, N=não) ')
            habilidade = input(
                '   Qual o nível de habilidade dele de 0 a 10? ')

            motorista = {
                'nome': nome,
                'cnh': cnh,
                'idade': int(idade),
                'calvo': True if isCalvo == 'S' else False,
                'habilidade': float(habilidade)
            }

            motoristaDAO.create(motorista)
            print('\nCompetidor cadastrado!')

            divider()

        elif option == '4':
            print('Você escolheu cadastrar um novo carro, preencha os dados abaixo')
            modelo = input('   O modelo do carro: ')
            cor = input('   Sua cor: ')
            cavalos = input('   A potência em cavalos: ')
            isTurbo = input('   Possui turbo? (S=sim, N=não) ')

            carro = {
                'modelo': modelo,
                'cor': cor,
                'cavalos': int(cavalos),
                'turbo': True if isTurbo == 'S' else False
            }

            carroDAO.create(carro)
            print('\nCarro cadastrado!')

            divider()

        elif option == '5':
            print('Você escolheu tornar um dos motoristas cadastrados calvo')

            results = motoristaDAO.read_all()
            if len(results) > 0:
                print('Esses são os motoristas cadastrados atualmente:')
                data = []
                for record in results:
                    data.append(record['m']._properties['nome'])

                for record in data:
                    pp(record)

            else:
                print('Porém nenhum piloto foi cadastrado até o momento')

            nome = input(
                'Qual deles deve receber essa bencão? ')

            motorista = {
                'nome': nome,
                'calvo': True
            }

            motoristaDAO.update_baldness(motorista)
            print('Agora o piloto', nome, 'está mais aerodinâmico!!')
            # pp(aux)

            # carro = {
            #     'modelo': 'Corvette',
            #     'turbo': True
            # }

            # aux = carroDAO.update_turbo(carro)
            # pp(aux)

            divider()

            # aux = motoristaDAO.read_all()
            # pp(aux)
            # aux = carroDAO.read_all()
            # pp(aux)
            # divider()

            # carro = {
            #     'modelo': 'Corvette',
            #     'cor': 'prata',
            #     'cavalos': 217,
            #     'turbo': False
            # }
            # carroDAO.create(carro)

        # elif option == '3':
        #     motorista = {
        #         'nome': 'Samuel',
        #         'calvo': True
        #     }

        #     aux = motoristaDAO.update_baldness(motorista)
        #     pp(aux)

        #     carro = {
        #         'modelo': 'Corvette',
        #         'turbo': True
        #     }

        #     aux = carroDAO.update_turbo(carro)
        #     pp(aux)

        #     divider()

        # elif option == '4':
        #     motorista = {
        #         'nome': 'Samuel'
        #     }
        #     motoristaDAO.delete(motorista)

        #     carro = {
        #         'modelo': 'Corvette'
        #     }
        #     carroDAO.delete(carro)

        #     aux = motoristaDAO.read_all()
        #     pp(aux)
        #     aux = carroDAO.read_all()
        #     pp(aux)

        #     divider()

        else:
            break
