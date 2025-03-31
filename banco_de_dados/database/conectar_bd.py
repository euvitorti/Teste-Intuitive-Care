import psycopg2
from db_config.db_config import db_config

def conectar_banco_de_dados():
    """
    Cria uma conexão com o banco de dados.
    """
    try:
        return psycopg2.connect(**db_config)
    except psycopg2.Error as e:
        raise Exception(f"Erro ao conectar ao banco: {str(e)}")
