from pprintpp import pprint as pp
from model.motoristaDAO import MotoristaDAO
from model.carroDAO import CarroDAO
from utils.utils import divider, generateOptionStr, probabilidadeDeVencer


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
            print('Você escolheu listar as relações entre os pilotos e os carros:')        
            results = motoristaDAO.read_all_relationship()
            if len(results) > 0:              
                print('Estas são todas as relações entre os pilotos e os carros cadastrados até agora:')
                for record in results:
                    pp(record)
                    for carro in results[record]:
                        pp(' ->  ' + carro['c']._properties['modelo'])
            else:
                print('Nenhuma relação entre pilotos e carros foi cadastrada até o momento')
            divider()

        elif option == '4':
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

        elif option == '5':
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
        
        elif option == '6':
            print('Você escolheu cadastrar uma nova relação entre um piloto e um carro, preencha os dados abaixo')
            nome = input('   O nome do piloto: ')
            modelo = input('   O modelo do carro: ')

            motoristaDAO.create_relationship(nome, modelo)
            print('\nRelação entre piloto e carro cadastrada!')

            divider()


        elif option == '7':
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
            divider()

        elif option == '8':
            print('Você escolheu tunar um dos carros')

            results = carroDAO.read_all()
            if len(results) > 0:
                print('Esses são os carros disponíveis:')
                data = []
                for record in results:
                    data.append(record['c']._properties['modelo'])

                for record in data:
                    pp(record)

            else:
                print('Porém nenhum carro foi cadastrado até o momento')

            modelo = input(
                'Qual deles deve ganhar um pouco mais de torque? ')

            carro = {
                'modelo': modelo,
                'turbo': True
            }

            carroDAO.update_turbo(carro)
            print('O carro', modelo, 'foi tunado')
            divider()

        elif option == '9':
            print('Você escolheu excluir um item do sistema')

            aux = input(
                'Você deseja excluir um carro, um piloto ou a relação? (C=carro, P=piloto, R=relação) ')

            if aux == 'C':
                results = carroDAO.read_all()
                if len(results) > 0:
                    print('Esses são os carros cadastrados:')
                    data = []
                    for record in results:
                        data.append(record['c']._properties['modelo'])

                    for record in data:
                        pp(record)

                    modelo = input('Qual deles deverá ser removido? ')
                    carro = {
                        'modelo': modelo
                    }
                    motoristaDAO.delete_relationship_by_model(carro['modelo'])
                    carroDAO.delete(carro)
                    

                    print('O modelo', modelo, 'foi removido')

                else:
                    print('Não há nenhum carro no sistema, cancelando operação')

            elif aux == 'P':
                results = motoristaDAO.read_all()
                if len(results) > 0:
                    print('Esses são os motoristas cadastrados:')
                    data = []
                    for record in results:
                        data.append(record['m']._properties['nome'])

                    for record in data:
                        pp(record)

                    nome = input('Qual deles deverá ser removido? ')
                    motorista = {
                        'nome': nome
                    }
                    motoristaDAO.delete_relationship_by_name(motorista['nome'])
                    motoristaDAO.delete(motorista)

                    print('O motorista', motorista, 'foi removido do sistema')
                else:
                    print(
                        'Não há nenhum piloto cadastrado no sistema, cancelando operação')
            elif aux == 'R':
                results = motoristaDAO.read_all_relationship()
                if len(results) > 0:              
                    print('Estas são todas as relações entre os pilotos e os carros cadastrados até agora:')
                    for record in results:
                        pp(record)
                        for carro in results[record]:
                            pp(' ->  ' + carro['c']._properties['modelo'])
                    nome = input('Quem é o dono do carro? ')
                    modelo = input('Qual o modelo do carro? ')

                    motoristaDAO.delete_unique_relationship(nome, modelo)

                    print('A relação foi removida do sistema')
                else:
                    print('Nenhuma relação entre pilotos e carros foi cadastrada até o momento')
            else:
                print('Não foi selecionada uma opção válida, cancelando operação')
            divider()

        elif option == '10':
            print('Você escolheu DISPUTAR UM RACHA')

            motoristas = motoristaDAO.read_all()
            carros = carroDAO.read_all()
            if len(motoristas) > 0  and len(carros) > 0:
                print('Esses são os motoristas cadastrados:')
                data = []
                for record in motoristas:
                    data.append(record['m']._properties['nome'])

                for record in data:
                    pp(record)

                piloto1 = input('Qual deles deverá ser o piloto n° 1? ')
                for record in motoristas:
                    if record['m']._properties['nome'] == piloto1:
                        piloto1 = record['m']._properties

                piloto2 = input('E o piloto n° 2? ')
                for record in motoristas:
                    if record['m']._properties['nome'] == piloto2:
                        piloto2 = record['m']._properties
                
                carros_1 = motoristaDAO.read_owernship(piloto1['nome'])
                if(len(carros_1) > 0):
                    print('Esses são os carros cadastrados do piloto n° 1 :')
                    data = []
                    for record in carros_1:
                        data.append(record['c']._properties['modelo'])

                    for record in data:
                        pp(record)

                    carro1 = input(
                        'Qual deles deverá ser o carro do piloto n° 1? ')
                    for record in carros_1:
                        if record['c']._properties['modelo'] == carro1:
                            carro1 = record['c']._properties
                else:
                    print('Não há nenhum carro cadastrado para o piloto n° 1')
                    break

                carros_2 = motoristaDAO.read_owernship(piloto2['nome'])
                if(len(carros_2) > 0):
                    print('Esses são os carros cadastrados do piloto n° 2 :')
                    data = []
                    for record in carros_2:
                        data.append(record['c']._properties['modelo'])

                    for record in data:
                        pp(record)

                    carro2 = input(
                        'Qual deles deverá ser o carro do piloto n° 2? ')
                    for record in carros_2:
                        if record['c']._properties['modelo'] == carro2:
                            carro2 = record['c']._properties
                else:
                    print('Não há nenhum carro cadastrado para o piloto n° 2')
                    break

                pb1 = probabilidadeDeVencer(piloto1, carro1)
                pb2 = probabilidadeDeVencer(piloto2, carro2)

                print('\n\nA corrida foi bem disputada, mas por habilidade (ou calvicie)')
                if(pb1 > pb2):
                    print('O piloto', piloto1['nome'], 'venceu!')
                elif (pb2 > pb1):
                    print('O piloto', piloto2['nome'], 'venceu!')
                else:
                    print('Os dois pilotos empataram e isso é quase impossível!!')
                print(pb1, pb2)
            else:
                print(
                    'Porém não há pilotos ou carros cadastrados :(')

            divider()
        else:
            break
   