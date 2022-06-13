import os
from dotenv import load_dotenv
from controller.database import Graph
from view.cli_interface import view

# Buscando as variáveis de ambiente
load_dotenv()

connection = Graph(
    uri=os.environ['DB_URI'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD']
)

view(connection)

connection.close()
