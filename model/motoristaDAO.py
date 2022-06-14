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
