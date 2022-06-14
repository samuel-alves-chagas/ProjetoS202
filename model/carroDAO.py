class CarroDAO(object):

    def __init__(self, connection):
        self.db = connection

    def create(self, carro):
        return self.db.execute_query(
            'CREATE (c:Carro {modelo:$modelo, cor:$cor, cavalos:$cavalos, turbo:$turbo}) return c',
            {'modelo': carro['modelo'], 'cor': carro['cor'], 'cavalos': carro['cavalos'], 'turbo': carro['turbo']})
