from pprintpp import pprint


class MotoristaDAO(object):

    def __init__(self, connection):
        self.db = connection

    def create(self, motorista):
        return self.db.execute_query(
            'CREATE (m:Motorista {nome:$nome, cnh:$cnh, idade:$idade, calvo:$calvo, habilidade:$habilidade}) return m',
            {'nome': motorista['nome'], 'cnh': motorista['cnh'], 'idade': motorista['idade'],
                'calvo': motorista['calvo'], 'habilidade': motorista['habilidade']}
        )

    def read_all(self):
        return self.db.execute_query(
            'MATCH (m:Motorista) RETURN m'
        )

    def update_baldness(self, motorista):
        return self.db.execute_query(
            'MATCH (m:Motorista {nome:$nome}) SET m.calvo = $calvo RETURN m',
            {'nome': motorista['nome'], 'calvo': motorista['calvo']}
        )

    def delete(self, motorista):
        return self.db.execute_query(
            'MATCH (m:Motorista {nome:$nome}) DELETE m',
            {'nome': motorista['nome']}
        )

    def create_relationship(self, nome, modelo):
        return self.db.execute_query(
            'MATCH (m:Motorista {nome:$nome}), (c:Carro {modelo:$modelo}) CREATE (m)-[r:POSSUI]->(c) RETURN r',
            {'nome': nome, 'modelo': modelo}
        )

    def delete_relationship_by_name(self, nome):
        return self.db.execute_query(
            'MATCH (m:Motorista {nome:$nome})-[r:POSSUI]->(c:Carro) DELETE r',
            {'nome': nome}
        )

    def delete_relationship_by_model(self, modelo):
        return self.db.execute_query(
            'MATCH (m:Motorista)-[r:POSSUI]->(c:Carro {modelo:$modelo}) DELETE r',
            {'modelo': modelo}
        )

    def delete_unique_relationship(self, nome, modelo):
        return self.db.execute_query(
            'MATCH (m:Motorista {nome:$nome})-[r:POSSUI]->(c:Carro {modelo:$modelo}) DELETE r',
            {'nome': nome, 'modelo': modelo}
        )

    def read_relationship(self, nome):
        return self.db.execute_query(
            'MATCH (m:Motorista {nome:$nome})-[r:POSSUI]->(c:Carro) RETURN r',
            {'nome': nome}
        )

    def read_all_relationship(self):
        pilots = self.read_all()
        results = {}

        for pilot in pilots:
            pilotName = pilot['m']._properties['nome']
            results[pilotName] = (self.read_owernship(pilotName))

        return results

    def read_owernship(self, nome):
        results = self.db.execute_query(
            'MATCH (m:Motorista {nome:$nome})-[r:POSSUI]->(c:Carro) RETURN c',
            {'nome': nome})
        return results
