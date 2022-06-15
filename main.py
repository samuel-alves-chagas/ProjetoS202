import os
from dotenv import load_dotenv
from controller.database import Graph
from view.cli_interface import view

# Buscando as variáveis de ambiente
# load_dotenv()

connection = Graph(
    # uri=os.environ['DB_URI'],
    # user=os.environ['DB_USER'],
    # password=os.environ['DB_PASSWORD']
    uri= "bolt://18.234.240.18:7687",
    user= "neo4j",
    password= "fighter-competition-market"
)

view(connection)

connection.close()
