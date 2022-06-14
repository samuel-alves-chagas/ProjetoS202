class CarroDAO(object):

    def __init__(self, connection):
        self.db = connection

    def create(self, carro):
        return self.db.execute_query(
            'CREATE (c:Carro {modelo:$modelo, cor:$cor, cavalos:$cavalos, turbo:$turbo}) return c',
            {'modelo': carro['modelo'], 'cor': carro['cor'], 'cavalos': carro['cavalos'], 'turbo': carro['turbo']})

    def read_all(self):
        return self.db.execute_query('MATCH (c:Carro) RETURN c')

    def update_turbo(self, carro):
        return self.db.execute_query(
            'MATCH (c:Carro {modelo:$modelo}) SET c.turbo = $turbo RETURN c',
            {'modelo': carro['modelo'], 'turbo': carro['turbo']}
        )
